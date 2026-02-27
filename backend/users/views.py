from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings


User = get_user_model()

class UserCreate(generics.CreateAPIView):
    # generic Apiviews abstract alot of things
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def api_check(request):
    return Response({'status':'ok', "message":"API is runing fine"})


class DRFLoginView(APIView):
    """
    Custom login view that works with DRF interface
    POST username/password to get JWT token and login session
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=400)
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)  # Create session for DRF interface
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': user.username
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)