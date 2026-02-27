
from django.contrib import admin
from django.urls import path, include
from users.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import api_check


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', UserCreate.as_view(), name='user_create'),  # Added trailing slash
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),  # Removed duplicate line
    # path('callback/', google_login_callback, name='callback'),
    # path('api/auth/user/', UserDetailView.as_view()),  # Added trailing slash
    # path('api/google/validate_token/', validate_google_token, name='validate-token'),  # Added trailing slash
    path('api/', include('users.urls')),  # Includes users app URLs
    path('api/ping/', api_check, name='api_check'),
]