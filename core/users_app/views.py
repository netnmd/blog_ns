from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def activation(request, **kwargs):
    uid = kwargs.get('uid', '')
    token = kwargs.get('token', '')

    response = requests.post('http://127.0.0.1:8000/auth/users/activation', data={
        uid: uid,
        token: token
    })

    return Response(data={"message": "регистрация прошла успешно"}, status=status.HTTP_200_OK)
