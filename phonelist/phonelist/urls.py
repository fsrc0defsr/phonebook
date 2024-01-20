from django.contrib import admin
from django.urls import path, include
from .views import home, login_view, logout_view, profile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ip_phone.urls')),
    path('accounts/login/', login_view, name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()