from dataclasses import field
from rest_framework import serializers
from newsapp.models import *


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'article_name', 'article_editor',
                  'article_date', 'article_rating', 'article_num_of_views']
        # fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'user_avatar', 'password']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'
