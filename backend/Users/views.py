import jwt
from django.core.validators import validate_email
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import * 
from .models import User
from django_blog.views import VerifyJWTUserAPIView



#User's auth

#All users
class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserRetrieveUpdateDestroySerializer



#Registration new user
class UserRegistrationAPIView(APIView):
	serializer_class = UserRegistrationSerializer

	def post(self, request):
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(status = status.HTTP_400_BAD_REQUEST)



#User authentication
class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			if len(serializer.data) == 0:
				return Response(status = status.HTTP_400_BAD_REQUEST)

			return Response(serializer.data, status = status.HTTP_200_OK)



#Retieve, Update, Destroy user
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserRetrieveUpdateDestroySerializer
	lookup_field = 'id'



class UserChangePasswordAPIView(APIView):
	def patch(self, request, user_id):
		try:
			current_user = User.objects.get(id = user_id)
			if 'password' in request.data:
				current_user.set_password(request.data['password'])
				current_user.save()

				return Response(status = status.HTTP_200_OK)
			return Response(status = status.HTTP_400_BAD_REQUEST)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#User followers, followings
class User_followersViewSet(viewsets.ViewSet):
	serializer_class = User_followersSerializer

	def list_user(self, request, user_id):
		try:
			current_user = User.objects.get(id = user_id)
			serializer = self.serializer_class(current_user.user.all(), many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)

		except:

			return Response(status = status.HTTP_400_BAD_REQUEST)


	def list_user_follower(self, request, user_id_follower):
		try:
			current_follower = User.objects.get(id = user_id_follower)
			serializer = self.serializer_class(current_follower.user_follower.all(), many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)
			
		except:

			return Response(status = status.HTTP_400_BAD_REQUEST)


	def create_delete(self, request):
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			serializer.save()
			if 'error' not in serializer.data:
				return Response(serializer.data, status = status.HTTP_201_CREATED)

			else:
				return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
		else:
			serializer.delete(request.data)
			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)



#User's posts

#All posts of users
class UserPostsListCreateAPIView(APIView):
	serializer_class = UserPostsListSerializer

	def get(self, request):
		try:
			all_user_post = UserPosts.objects.all()
			serializer = self.serializer_class(all_user_post, many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		try:
			serializer = self.serializer_class(data = request.data)

			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status = status.HTTP_201_CREATED)

			return Response(status = status.HTTP_400_BAD_REQUEST)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#All posts of user
class UserPostsListUserAPIView(APIView):
	serializer_class = UserPostsListSerializer
	def get(self, request, user_id):
		try:
			user = User.objects.get(id = user_id)
			serializer = self.serializer_class(user.user_posts.all(),many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#Retieve, Update, Destroy user's post
class UserPostsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserPosts.objects.all()
	serializer_class = UserPostsListSerializer
	lookup_field = 'id'



#Likes of user's post
class UserPostLikesListCreateViewSet(viewsets.ViewSet):
	def list(self, request, post_id):
		try:
			current_post_of_Posts = UserPosts.objects.get(id = post_id)
			current_post_of_PostLikes = UserPostLikes.objects.filter(post = current_post_of_Posts)
			serializer = UserPostLikesListSerializer(current_post_of_PostLikes, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def create_delete(self, request, post_id):
		try:
			validated_data = {'post':post_id, 'user':request.data['id']}
			serializer = UserPostLikesListSerializer(data = validated_data)
			if serializer.is_valid():
				if serializer.check_like(validated_data):
					serializer.delete(validated_data)
					return Response(status = status.HTTP_200_OK)
				else:
					serializer.save()
					return Response(status = status.HTTP_201_CREATED)

			return Response(status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#Comments of user's post
class UserPostCommentsListCreateViewSet(viewsets.ViewSet):
	def list(self, request, post_id):
		try:
			current_post_of_Posts = UserPosts.objects.get(id = post_id)
			current_post_of_PostComments = UserPostComments.objects.all().filter(post = current_post_of_Posts)
			serializer = UserPostCommentsListSerializer(current_post_of_PostComments, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def create_delete(self, request, post_id):
		try:
			validated_data = {'post':post_id, 'user':request.data['post_id'], 'comment':request.data['comment']}
			serializer = UserPostCommentsListSerializer(data = validated_data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status = status.HTTP_201_CREATED)

			return Response(status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def delete(self, request, comment_id):
		try:
			comment = UserPostComments.objects.get(id = comment_id)
			comment.delete()

			return Response(status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)