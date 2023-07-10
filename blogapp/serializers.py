from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model # 추가
#from rest_framework.serializers import Modelserializer
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        
        fields = "__all__"
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.ReadOnlyField(source = 'post.headline')
    class Meta:
        model = Category
        fields = "__all__"

class PostBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        exclude = "__all__"        
        
        
class ResponseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields ='__all__'
        
        
class MentalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mental_illness
        fields ='__all__'
            
        
        
                