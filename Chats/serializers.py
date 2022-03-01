from rest_framework import serializers
from .models import *

from Users.models import User



class ChatsSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		chat = Chats.objects.create()

		for i in validated_data['users']:
			chat.users.add(i)
		chat.save()

		admin = Chats_admins.objects.create(chat = chat, user = User.objects.get(id = validated_data['users'][0].id))
		return chat

	class Meta:
		model = Chats
		fields = ['id', 'users']



class MessagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Messages
		fields = ['id', 'chat', 'user','message']