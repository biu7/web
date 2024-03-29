from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from serializer import *
from rest_framework import generics


class allCatagory(generics.ListCreateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerialize
class allNewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerialize

class allComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialize

class newsList(APIView):
    def get(self,request,num,format=None):
        catagory = Catagory.objects.get(id=num)
        news = catagory.news_set.all()
        ser = NewsSerialize(news,many=True)
        return Response(ser.data)

class newsInfo(APIView):
    def get(self,request,num,format=None):
        news = News.objects.get(id=num)
        ser = NewsSerialize(news)
        return Response(ser.data)

    def delete(self,request,num,format=None):
        news = News.objects.get(id=num)
        news.delete()
        return Response(status=200)

    def post(self,request,num,format=None):
        news = News.objects.get(id=num)
        ser = NewsSerialize(news,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class commentList(APIView):
    def get(self,request,num,format=None):
        news = News.objects.get(id=num)
        comment = news.comment_set.all()
        ser = CommentSerialize(comment,many=True)
        return Response(ser.data)
class commentInfo(APIView):

    def get(self,request,num,format=None):
        comment = Comment.objects.get(id=num)
        ser = CommentSerialize(comment)
        return Response(ser.data)

    def delete(self,request,num,format=None):
        comment = Comment.objects.get(id=num)
        comment.delete()
        return Response(status=200)

    def post(self,request,num,format=None):
        comment = Comment.objects.get(id=num)
        ser = CommentSerialize(comment,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)



