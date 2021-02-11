from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework_jwt.utils import jwt_payload_handler
import jwt
from .serializers import UserSerializer, UserDetailSerializer
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny, ])
def register_user(request):
    user = request.data
    serializer = UserSerializer(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

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