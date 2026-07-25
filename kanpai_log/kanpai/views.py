from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q, Sum
from .models import Entry
from .forms import EntryForm
from datetime import date


def entry_list(request):
    qs = Entry.objects.all()
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    filter_label = 'すべての記録'

    if year:
        qs = qs.filter(date__year=year)
        filter_label = f'{year}年'
        if month:
            qs = qs.filter(date__month=month)
            filter_label = f'{year}年{int(month):02d}月'
            if day:
                qs = qs.filter(date__day=day)
                filter_label = f'{year}年{int(month):02d}月{int(day):02d}日'

    entries = qs.order_by('-date')
    total = entries.aggregate(total=Sum('price'))['total'] or 0
    current_month_total = Entry.objects.filter(date__year=date.today().year, date__month=date.today().month).aggregate(total=Sum('price'))['total'] or 0

    return render(request, 'kanpai/entry_list.html', {
        'entries': entries,
        'total': total,
        'current_month_total': current_month_total,
        'filter_label': filter_label,
        'year': year or '',
        'month': month or '',
        'day': day or '',
    })


def tsumami_list(request):
    entries = Entry.objects.filter(
        Q(name__icontains='つまみ') | Q(memo__icontains='つまみ')
    ).order_by('-date')
    total = entries.aggregate(total=Sum('price'))['total'] or 0
    current_month_total = Entry.objects.filter(date__year=date.today().year, date__month=date.today().month).aggregate(total=Sum('price'))['total'] or 0

    return render(request, 'kanpai/entry_list.html', {
        'entries': entries,
        'total': total,
        'current_month_total': current_month_total,
        'filter_label': 'つまみ記録',
        'year': '',
        'month': '',
        'day': '',
        'tsumami_page': True,
    })


def tsumami_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        form.fields['drink_type'].widget = form.fields['drink_type'].hidden_widget()
        if form.is_valid():
            entry = form.save(commit=False)
            entry.drink_type = 'other'
            if 'つまみ' not in entry.memo:
                entry.memo = (entry.memo + '\nつまみ').strip()
            entry.save()
            return redirect('tsumami_list')
    else:
        form = EntryForm(initial={'drink_type': 'other'})
        form.fields['drink_type'].widget = form.fields['drink_type'].hidden_widget()

    return render(request, 'kanpai/entry_form.html', {'form': form, 'tsumami_create': True})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'kanpai/entry_detail.html', {'entry': entry})


def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'kanpai/entry_form.html', {'form': form})


def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'kanpai/entry_form.html', {'form': form, 'entry': entry})


def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'kanpai/entry_confirm_delete.html', {'entry': entry})
