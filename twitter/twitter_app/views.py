from django.shortcuts import render
from twitter_app.models import User, Tweet
from twitter_app.serializers import UserSerializer, TweetSerializer, TweetSoftDeleteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET',])
def api_user_list_view(request):
    user = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_user_id_list_view(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)

@api_view(['GET',])
def api_tweet_list_view(request):
    tweet = Tweet.objects.filter(delete_tweet=False)
    if request.method == 'GET':
        serializer = TweetSerializer(tweet, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_tweet_id_list_view(request, id):
    try:
        user = Tweet.objects.get(id=id, delete_tweet=False)
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            serializer = TweetSerializer(user)
            return Response(serializer.data)

@api_view(['POST',])
def api_create_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'Created Successfully'
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def api_create_tweet_view(request):
    if request.method == 'POST':
        print(request.data)
        serializer = TweetSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['Success'] = 'Created Successfully'
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT',])
def api_update_tweet_view(request, id):
    try:
        user = Tweet.objects.get(id=id, delete_tweet=False)
    except Tweet.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'PUT':
            serializer = TweetSerializer(user, data=request.data)
            if serializer.is_valid():
                data = {}
                serializer.save()
                data['Success'] = 'Updated Successfully'
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['PUT',])
def api_soft_delete_tweet_view(request, id):
    try:
        user = Tweet.objects.get(id=id, delete_tweet=False)
    except Tweet.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'PUT':
            serializer = TweetSoftDeleteSerializer(user, data=request.data)
            if serializer.is_valid():
                data = {}
                serializer.save()
                data['Success'] = 'Updated Successfully'
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_406_NOT_ACCEPTABLE)