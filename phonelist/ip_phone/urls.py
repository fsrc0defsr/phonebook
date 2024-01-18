from django.urls import path
from .views import PhoneNumberList

urlpatterns = [
    path('phonebook/', PhoneNumberList.as_view(), name='phonebook-list'),
]
