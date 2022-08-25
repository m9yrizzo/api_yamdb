from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ConfirmationCodeSerializer


@api_view(['POST'])
def get_confirmation_code(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    email = serializer.validated_data['email']
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Регистрация', f'Код подтверждения: {confirmation_code}',
        'admin@yambd', [email], fail_silently=False, )
    return Response(serializer.validated_data, status=status.HTTP_200_OK)
