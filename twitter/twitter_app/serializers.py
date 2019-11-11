from rest_framework import serializers
from twitter_app.models import User, Tweet

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name',)
    
class TweetSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Tweet
        fields = ('short_text', 'user', 'text', 'date_time_created', 'date_time_updated', 'delete_tweet',)