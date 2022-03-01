from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


from .serializers import * 
from .models import *
from Users.models import User
from django_blog.views import VerifyPostAdminAPIView



#All community
class CommunityListAPIView(APIView):
	serializer_class = CommunityListSerializer
	def get(self, request):
		try:
			communities = Community.objects.all()
			serializer = self.serializer_class(communities, many = True)

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



#Retrieve, Update, Destroy community
class CommunityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Community.objects.all()
	serializer_class = CommunityListSerializer
	lookup_field = 'id'



#Retrieve all community's admins
class CommunityAdminsRetrieveViewSet(viewsets.ViewSet):
	def list(self, request, id):
		current_community = Community.objects.get(id = id)
		serializer_admins = Community_adminsSerializer(current_community.com_admins.all(), many = True)

		return Response(serializer_admins.data, status = status.HTTP_200_OK)



#All category of Community
class CommunityCategoryAPIView(generics.ListAPIView):
	queryset = CommunityCategory.objects.all()
	serializer_class = CommunityCategorySerializer



#Community's followers
class Community_followersViewSet(viewsets.ViewSet):
	serializer_class = Community_followersSerializer

	def list_following(self, request, id):
		try:
			current_user = User.objects.get(id = id)
			serializer = self.serializer_class(current_user.you_follower.all(), many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def list_follower(self, request, id):
		try:
			current_com = Community.objects.get(id = id)
			serializer = self.serializer_class(current_com.com_followers.all(), many = True)
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



#All Communities' posts
class CommunityPostsAPIView(APIView):
	serializer_class = CommunityPostsSerializer

	def get(self, request):
		try:
			all_user_post = CommunityPosts.objects.all()
			serializer = self.serializer_class(all_user_post, many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)

	def post(self, request):
		serializer = self.serializer_class(data = request.data)

		if serializer.is_valid():
			serializer.save()
			if 'error' not in serializer.data:
				return Response(serializer.data, status = status.HTTP_201_CREATED)

		return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)



#All community's posts
class CommunityPostsCommunityAPIView(APIView):
	serializer_class = CommunityPostsSerializer
	def get(self, request, id):
		try:
			communities = CommunityPosts.objects.filter(community = id)
			serializer = self.serializer_class(communities,many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#Retrieve, Update, Destroy community's post
class CommunityPostsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = CommunityPosts.objects.all()
	serializer_class = CommunityPostsSerializer
	lookup_field = 'id'



#Likes of community's post
class CommunityPostLikesListCreateViewSet(viewsets.ViewSet):
	serializer_class = CommunityPostLikesListSerializer
	def list(self, request, id):
		try:
			current_post_of_Posts = CommunityPosts.objects.get(id = id)
			current_post_of_PostLikes = CommunityPostLikes.objects.filter(post = current_post_of_Posts)
			serializer = self.serializer_class(current_post_of_PostLikes, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def create_delete(self, request, id):
			validated_data = {'post':id, 'user':request.data['id']}
			serializer = self.serializer_class(data = validated_data)
			if serializer.is_valid():
				if serializer.check_like(validated_data):
					serializer.delete(validated_data)
					return Response(status = status.HTTP_200_OK)
				else:
					serializer.save()
					return Response(status = status.HTTP_201_CREATED)
			print(serializer.errors)
			return Response(status = status.HTTP_400_BAD_REQUEST)



#Comments of community's post
class CommunityPostCommentsListCreateViewSet(viewsets.ViewSet):
	serializer_class = CommunityPostCommentsListSerializer
	def list(self, request, id):
		try:
			current_post_of_Posts = CommunityPosts.objects.get(id = id)
			current_post_of_PostComments = CommunityPostComments.objects.all().filter(post = current_post_of_Posts)
			serializer = self.serializer_class(current_post_of_PostComments, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def create_delete(self, request, id):
		try:
			validated_data = {'post':id, 'user':request.data['user'], 'comment':request.data['comment']}
			serializer = self.serializer_class(data = validated_data)
			if serializer.is_valid():
				if 'id' in request.data:

					serializer.delete(request.data['id'])
					return Response(status = status.HTTP_200_OK)

				serializer.save()
				return Response(serializer.data, status = status.HTTP_200_OK)

			return Response(status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)