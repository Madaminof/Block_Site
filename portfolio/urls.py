from django.urls import path
from .views import portfolio_view, contact_view

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('contact/', contact_view, name='contact'),
]
