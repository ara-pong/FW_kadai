from django.db import models


class Entry(models.Model):
    DRINK_CHOICES = [
        ("beer", "ビール"),
        ("sake", "日本酒"),
        ("shochu", "焼酎"),
        ("wine", "ワイン"),
        ("whisky", "ウイスキー"),
        ("cocktail", "カクテル"),
        ("other", "その他"),
    ]

    date = models.DateField()
    name = models.CharField(max_length=100)
    drink_type = models.CharField(max_length=20, choices=DRINK_CHOICES)
    price = models.PositiveIntegerField()
    memo = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.date} - {self.name} - {self.get_drink_type_display()} - {self.price}円"
