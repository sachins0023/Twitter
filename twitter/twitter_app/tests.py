from django.test import TestCase
from twitter_app.models import User, Tweet
# Create your tests here.

class TweetTestCase(TestCase):
    """
    Test Case 1-2: testing whether edited function works, getting short text
    """
    
    def setUp(self):
        user = User.objects.create(email = 'sachinsuresh00@gmail.com', name = 'Sachin Suresh')
        Tweet.objects.create(user=user, text = 'United finally plays exciting football !! Ole is at the wheel.')
        
    def test_case_edited(self):
        tweet = Tweet.objects.get(text = 'United finally plays exciting football !! Ole is at the wheel.')
        self.assertEqual(tweet.edited(), False)
        
    def test_case_get_short_text(self):
        tweet = Tweet.objects.get(text = 'United finally plays exciting football !! Ole is at the wheel.')
        self.assertEqual(tweet.get_short_text(), 'United fin...')