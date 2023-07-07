from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.serializer import ContactUsSerializer
from django.core.mail import send_mail


class ContactUsView(APIView):
    serializer_class = ContactUsSerializer

    def post(self, request):
        srz_data = ContactUsSerializer(data=request.data)
        if srz_data.is_valid():
            email = srz_data.validated_data['email']
            subject = srz_data.validated_data['subject']
            context = srz_data.validated_data['context']
            send_mail(subject, 'from: %s \n context: %s' % (email, context),
                      'contact-us@mail.csco.tech', ['support@mail.csco.tech'], fail_silently=False)
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
