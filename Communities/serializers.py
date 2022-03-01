from rest_framework import serializers

from .models import *


class CommunityListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		community = Community.objects.create(**validated_data)
		post_admin = Community_admins.objects.create(community = community, user = community.creator, description = 'Creator')
		return community

	class Meta:
		model = Community
		fields = ['id','name', 'description', 'creator', 'date_creating', 'category', 'image']



class CommunityCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Community
		fields = ['id','name','date_creating']



class Community_adminsSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		admin = Community_admins.objects.create(**validated_data)
		return admin

	class Meta:
		model = Community_admins
		fields = ['id','community','user','date_creating']



class Community_followersSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		try:
			follower = Community_followers.objects.create(community = validated_data['community'], user = validated_data['user'])
			return follower
		except:
			return {'error':'User do not exist'}


	def delete(self, validated_data):
		try:
			follower = Community_followers.objects.get(community = validated_data['community'], user = validated_data['user'])
			follower.delete()
			return follower

		except:
			return {'error':'User do not exist'}


	class Meta:
		model = Community_followers
		fields = ['id','community','user','date_creating']



class CommunityPostsSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		try:
			print(validated_data['community'])
			admin = Community_admins.objects.filter(user = validated_data['author'].id, community = validated_data['community'].id).first()
			if admin:
				post = CommunityPosts.objects.create(**validated_data)
				return post
			else:
				return {'error':'This user is not admin'}

		except:
			return {'error':'This user is not admin'}


	class Meta:
		model = CommunityPosts
		fields = ['id','community','text','author','date_creating']



class CommunityPostLikesListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		post_likes = CommunityPostLikes.objects.create(**validated_data)
		return post_likes


	def check_like(self, validated_data):
		try:
			post_like = CommunityPostLikes.objects.get(**validated_data)
			return True
		except:
			return False


	def delete(self, validated_data):
		return CommunityPostLikes.objects.get(**validated_data).delete() 


	class Meta:
		model = CommunityPostLikes
		fields = ['id','post','user']



class CommunityPostCommentsListSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		post_likes = CommunityPostComments.objects.create(**validated_data)
		return post_likes


	def delete(self, comment_id):
		return CommunityPostComments.objects.get(id = comment_id).delete() 


	class Meta:
		model = CommunityPostComments
		fields = ['id','post','user','comment']