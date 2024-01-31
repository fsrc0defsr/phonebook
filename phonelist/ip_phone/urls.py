from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import PhoneNumberList

urlpatterns = [
    #path('phonebook/', login_required(PhoneNumberList.as_view()), name='phonebook-list'),
    path('phonebook/', PhoneNumberList.as_view(), name='phonebook-list'),

]
