from django.urls import path
from . import views
app_name = "letter"

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('mail_letter/', views.mail_letter, name='mail-letter')
]
