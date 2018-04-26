from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers


# Create your views here.
'''
APIView :
http method (get, post, put, patch, delete) unsuitable
when need full control over the logic
processing file with sychronous response or calling other API

Viewset :
uses model operation for function/ not http method
list, create, retrieve, update, partial update, destroy
good for standard db
simple CRUD, quick api but cannot customize on logic
'''

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        apiview = [
            'Uses HTTP method as function',
            'similar to traditional django view',
            'gives u most control over logic',
            'is mapped manually to URLs'
        ]
        # REsponse always shoulf be in dictionary
        return Response({'message':'hello!', 'apiview': apiview})

    def post(self, request):
        # request를 serializer에 보냄
        serializer= serializers.HelloSerializer(data=request.data)

        # check if data is valid to serializer
        if serializer.is_valid():
            # once it is sent to serializer we can get data by dic
            name= serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # pk is primary key, identify id of object key
    def put(self, request, pk=None):
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        # return hello message
        aaaviewset = [
        'uses actions [list, create, retrieve, update, parital_update]',
        'automatically maps to urls using router',
        'provide more functionality with less code',
        ]
        return Response({'message':'hello!!!', 'aaaviewset':aaaviewset})

    def create(self, request):
        """Create new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})

        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """
        특정 object get
        """

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({"http_method": 'PUT'})

    def partial_update(self, request, pk=None):
        """
        update part of object
        """
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
