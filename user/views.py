from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import registerSerializer
from .models import user
# Create your views here.

class registerView(APIView):
    def post(self,request):
        serializer=registerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'User created successfully',
                'users':serializer.data
            },status=status.HTTP_200_OK)
        
        else:

            return Response({
                'status':400,
                'msg':'something went wrong',
                'users':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        

class loginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        check=user.objects.filter(username=username,password=password).exists()

        if check==True:
            return Response({
                'status':200,
                'msg':'login successfully',
                
            },status=status.HTTP_200_OK)
        
        else:
            return Response({
                'status':400,
                'msg':'Invalid credentials'
            },status=status.HTTP_400_BAD_REQUEST)

