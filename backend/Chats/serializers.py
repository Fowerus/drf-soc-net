from .models import *
from rest_framework import serializers



class ChatsSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		chat = Chats().save()
		print(chat)
		chat.users.update(validated_data['users']).save()
		admin = Chats_admins.objects.create(chat = chat.id, user = validated_data['main_user'])
		return chat

	class Meta:
		model = Chats
		fields = ['id', 'users']



class MessagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messages
		fields = ['id', 'chat', 'user','text']