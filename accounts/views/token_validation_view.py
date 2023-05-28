from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import jwt
from django.conf import settings


class TokenValidationView(APIView):

    def get(self, request):
        print("ppppppppppppppppppppp")
        try:
            token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            expiration_time = decoded_token['exp']
            current_time = int(datetime.now().timestamp())

            if expiration_time < current_time:
                return Response({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'message': 'Token is valid'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.InvalidTokenError:
            return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
