import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from .models import *


#User's auth
class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

	class Meta:
		model = User
		fields = ['username','email','last_name','first_name','password']



class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField(write_only=True)
	password = serializers.CharField(max_length=128, write_only=True)

	username = serializers.CharField(max_length=255, read_only=True)
	token = serializers.CharField(max_length=255, read_only=True)

	def validate(self, data):
		email = data.get('email',None)
		password = data.get('password',None)


		if email is None:
			return Response(status = status.HTTP_400_BAD_REQUEST)

		if password is None:
			return Response(status = status.HTTP_400_BAD_REQUEST)


		try:
			current_user = User.objects.get(email = email)

			user = authenticate(username = current_user.username, email = email, password = password)


			if user is None:
				return Response(status = status.HTTP_400_BAD_REQUEST)

			elif not user.is_active:
				return Response(status = status.HTTP_400_BAD_REQUEST)


			validated_data = user.token
			validated_data.setdefault('token', jwt.encode(user.token,settings.SECRET_KEY, algorithm = 'HS256'))

			return validated_data


		except:
			return {'error': 'This user did not exist'}



class UserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'last_name', 'first_name']



class User_followersSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		try:
			user = User_followers.objects.create(user = validated_data['user'], user_follower = validated_data['user_follower'])
			return user
		except:
			return {'error':'User do not exist'}


	def delete(self, validated_data):
		try:
			user = User_followers.objects.get(user = validated_data['user'], user_follower = validated_data['user_follower'])
			user.delete()
			return user

		except:
			return {'error':'User do not exist'}


	class Meta:
		model = User_followers
		fields = ['user', 'user_follower']



#User's posts
class UserPostsListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		post = UserPosts.objects.create(**validated_data)
		return post


	class Meta:
		model = UserPosts
		fields = ['id','text','author']



class UserPostLikesListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		post_likes = UserPostLikes.objects.create(**validated_data)
		return post_likes


	def check_like(self, validated_data):
		try:
			post_like = UserPostLikes.objects.get(**validated_data)
			return True
		except:
			return False


	def delete(self, validated_data):
		return UserPostLikes.objects.get(**validated_data).delete() 


	class Meta:
		model = UserPostLikes
		fields = ['id','post','user']



class UserPostCommentsListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		post_likes = UserPostComments.objects.create(**validated_data)
		return post_likes


	def delete(self, comment_id):
		return UserPostComments.objects.get(id = comment_id).delete() 


	class Meta:
		model = UserPostComments
		fields = ['id','post','user','comment']