from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework_jwt.utils import jwt_payload_handler
import jwt
from .serializers import UserSerializer
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
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_details = {
                'name': user.name,
                'token': token,
            }
            user_logged_in.send(
                sender=user.__class__,
                request=request,
                user=user
            )
            return Response(user_details, status=status.HTTP_200_OK)

        except Exception as e:
            res = {'error': 'something went wrong :('}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except ObjectDoesNotExist:
        res = {'error': 'Check the credentials'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)
 
    
class UserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
 
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
 
        return Response(serializer.data, status=status.HTTP_200_OK)
