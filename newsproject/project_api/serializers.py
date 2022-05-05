from dataclasses import field
from rest_framework import serializers
from newsapp.models import *


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    article_editor = serializers.HyperlinkedRelatedField(many=True,
        view_name='pro_api:api-editor-details', read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='pro_api:api-article-details')

    class Meta:
        model = Article
        # fields = ['id', 'article_name', 'article_editor',
        #           'article_date', 'article_rating', 'article_num_of_views']
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['article_editor'] = EditorSerializer(read_only=True)
        return super().to_representation(instance)


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pro_api:api-user-details')
    class Meta:
        model = CustomUser
        # fields = ['username', 'user_avatar', 'password']
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment_on_article = serializers.HyperlinkedRelatedField(
        view_name='pro_api:api-article-details', read_only=True)

    comment_owner = serializers.HyperlinkedRelatedField(
        view_name='pro_api:api-user-details', read_only=True)

    url = serializers.HyperlinkedIdentityField(view_name='pro_api:api-comment-details')

    class Meta:
        model = Comment
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     self.fields['comment_on_article'] = ArticleSerializer(read_only=True)
    #     self.fields['comment_owner'] = CustomUserSerializer(read_only=True)
    #     return super().to_representation(instance)


class EditorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pro_api:api-editor-details')
    class Meta:
        model = Editor
        fields = '__all__'
