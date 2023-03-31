from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from .serializers import projectserializer,projectserializer1
from rest_framework.response import Response
from .models import project
from Client.models import client
# Create your views here.

class projectView(APIView):
    def post(self,request):
        serializer=projectserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'project created successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:

            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        list=project.objects.all()
        serializer=projectserializer1(list,many=True)
        return Response({
            'status':200,
            'Projects':serializer.data
        },status=status.HTTP_200_OK)
