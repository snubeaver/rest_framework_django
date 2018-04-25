from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
'''
APIView :
http method (get, post, put, patch, delete) unsuitable
when need full control over the logic
processing file with sychronous response or calling other API

ViewSet :

'''

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        apiview = [
            'Uses HTTP method as function',
            'similar to traditional django view',
            'gives u most control over logic',
            'is mapped manually to URLs'
        ]
        # REsponse always shoulf be in dictionary
        return Response({'message':'hello!', 'apiview': apiview})
