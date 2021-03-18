from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from Users.models import *
from .models import *
from .serializers import *


#List of current user chats
class MyChatsListAPIView(APIView):
	serializer_class = ChatsSerializer
	def post(self, request):
		try:
			current_user = User.objects.get(id = request.data['user_id']).my_chats.all()
			serializer = self.serializer_class(current_user, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



#Create or delete chat
class ChatCreateUpdateDeleteAPIView(APIView):
	serializer_class = ChatsSerializer
	def post(self, request):
		print(request.data['users'])
		serializer = self.serializer_class(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(status = status.HTTP_400_BAD_REQUEST)




	def patch(self, request, chat_id):
		try:
			current_chat = Chats.objects.get(id = chat_id)

			if request.data['delete'] == False:
				for i in request.data['users']:
					current_chat.users.add(i)
				current_chat.save()
				serializer = self.serializer_class(current_chat)

				return Response(serializer.data, status = status.HTTP_200_OK)


			elif request.data['delete'] == True:
				if request.data['user_id'] == current_chat.chat_admins.user.id:
					for i in request.data['users']:
						current_chat.users.remove(i)
					current_chat.save()

					return Response(status = status.HTTP_200_OK)


			return Response(status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


	def delete(self, request, chat_id):
		try:
			current_chat = Chats.objects.get(id = chat_id)
			current_chat.users.remove(request.data['user_id'])
			current_chat.save()

			return Response(status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)


#Retrieve chat
class ThisChatAPIView(generics.RetrieveAPIView):
	serializer_class = ChatsSerializer
	lookup_field = 'id'



#Chat's messages
class ChatsMessagesAPIView(APIView):
	serializer_class = MessagesSerializer
	def get(self, request, chat_id):
		try:
			current_chats_content = Messages.objects.filter(chat = chat_id)
			serializer = self.serializer_class(current_chats_content, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)