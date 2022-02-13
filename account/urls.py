from django.urls import path, include

from django.contrib.auth import views as auth_views  

from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = "account"

urlpatterns = [
    path('employee/register/', RegisterEmployeeView.as_view(), name='employee-register'),
    
    path('employee/profile/update', EditProfileView.as_view(), name='employer-profile-update'),
    
    path('employer/register/', RegisterEmployerView.as_view(), name='employer-register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)