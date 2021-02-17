import jwt
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler

from .models import User
from .serializers import UserDetailSerializer, UserSerializer
from django.core.mail import send_mail
from smtplib import SMTPException

@api_view(['POST'])
@permission_classes([AllowAny, ])
def register_user(request):
    user = request.data
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()
        try:
            send_mail(
                'Welcome to MyWall',
                'Your acount has been verified',
                'alatortrix@example.com',
                [serializer.data['email']],
                fail_silently=False,
            )
        except SMTPException:
            print('There was an error sending an email to: ', serializer.data['email']) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email, password=password)
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        serializer = UserDetailSerializer(user)
        new_serializer = {'token': token}
        new_serializer.update(serializer.data)
        user_logged_in.send(
            sender=user.__class__,
            request=request,
            user=user
        )
        return Response(new_serializer, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        res = {'error': 'Check the credentials'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)
 
    
class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserDetailSerializer
