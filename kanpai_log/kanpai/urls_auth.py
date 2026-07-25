from django.urls import path
from .views_auth import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]
