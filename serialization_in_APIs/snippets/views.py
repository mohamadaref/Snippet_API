from django.shortcuts import render
from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status

class SnippetList(APIView):

    def get(self , request , format = None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets , many = True)
        return Response(serializer.data)

    def post(self , request , format = None):
        serializer = SnippetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self , pk):
        try:
            snippet = Snippet.objects.get(pk = pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self , request , pk , format = None):
        snippet = self.get_object(pk)
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet , many=True)
        return Response(serializer.data)

    def put(self , request , pk , format = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk , format = None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
