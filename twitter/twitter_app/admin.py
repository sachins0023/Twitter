from django.contrib import admin
from twitter_app.models import User, Tweet
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', )
    ordering = ('name',)
    search_fields = ['name',]
    
admin.site.register(User,UserAdmin)

class TweetAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'user', 'text', 'date_time_created', 'date_time_updated', 'delete_tweet',)
    list_filter = ('delete_tweet',)
    ordering = ('-date_time_updated',)
    search_fields = ['user', 'text',]
    
admin.site.register(Tweet, TweetAdmin)