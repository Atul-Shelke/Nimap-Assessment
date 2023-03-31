from django.shortcuts import render
from rest_framework import status
from .serializers import clientSerializer,clientSerializer1
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import client
from user.models import user
# Create your views here.
class registerView(APIView):
    def post(self,request):
        serializer=clientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'client successfully created',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:

            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        

    def get(self,request):
        list=client.objects.all()
        serializer=clientSerializer1(list,many=True)
        return Response({
            'status':200,
            'msg':'All client list',
            'data':serializer.data
        },status=status.HTTP_200_OK)
    
class updateView(APIView):
    def patch(self,request,id):
        list=client.objects.get(id=id)
        serializer=clientSerializer(list,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':200,
                'msg':'Record updated successfully',
                'data':serializer.data
            },status=status.HTTP_200_OK)
        
        else:
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data':serializer.errors
            })
    
    def delete(self,request,id):
        list=client.objects.get(id=id)
        list.delete()
        return Response({
            'status':204,
            'msg':'Record deleted successfully'
        })


