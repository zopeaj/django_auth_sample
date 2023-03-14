from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.business.concretes.AuthManager import authManager
# Create your views here.


class RegistrationApiView(APIView):
    def post(self, request, format='json'):
        data = authManager.register(data=request.data)
        if data is not None:
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    def get(sef, request, format='json'):
        user = authManager.confirmUser(data=request.data)
        if data is not None:
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Incorrect username and password"}, status=status.HTTP_400_BAD_REQUEST)
