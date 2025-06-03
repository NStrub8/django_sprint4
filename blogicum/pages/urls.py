from django.urls import path
from .views import AboutPageView, RulesPageView, edit_profile, register

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('rules/', RulesPageView.as_view(), name='rules'),
    path('registration/', register, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
