from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from app.serializers import CustomUserSerializer


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={'request': request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = CustomUserSerializer(user)

                if not created:
                    token.delete()
                    token = Token.objects.create(user=user)
                else:
                    return Response({
                        'message': "Someone else has already logged in with this user",
                    }, status=status.HTTP_400_BAD_REQUEST)

                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': "Login successful",
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': "This user can not log in",
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'message': "User or password incorrect",
        }, status=status.HTTP_400_BAD_REQUEST)
