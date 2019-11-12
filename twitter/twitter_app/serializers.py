from rest_framework import serializers
from twitter_app.models import User, Tweet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'email',)
    
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id','short_text', 'user', 'text', 'date_time_created', 'date_time_updated',)
        
class TweetSoftDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields =('delete_tweet',)