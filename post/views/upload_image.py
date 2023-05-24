from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from post.serializer import ImageSerializer


class UploadImage(APIView):
    serializer_class = ImageSerializer
    authentication_classes = []

    def post(self, request):
        srz_data = ImageSerializer(data=request.data)
        if srz_data.is_valid():
            image = srz_data.create(srz_data.validated_data)
            srz_data.validated_data['image'] = image.image
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)