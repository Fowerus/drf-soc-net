from django.shortcuts import render

import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


from Users.models import User
from Communities.models import Community
from Chats.models import Chats



def main(request):
	return render(request, 'index.html')


class VerifyJWTUserAPIView(APIView):
	def post(self,request):
		current_user = User.objects.get(username = request.data.get('username'))
		try:
			if current_user and current_user.is_active:
				token_decode = jwt.decode(request.data.get('token'),settings.SECRET_KEY, algorithms = ['HS256'])
				
				if token_decode['id'] == current_user.id:

					return Response({
						'id':current_user.id,
						'email':current_user.email,
						'username':current_user.username,
						'last_name':current_user.last_name,
						'first_name':current_user.first_name
						}, status = status.HTTP_200_OK)

			return Response(status = status.HTTP_400_BAD_REQUEST)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class VerifyPostAdminAPIView(APIView):
	def post(self, request):
		try:
			current_user = User.objects.get(id = request.data.get('user_id'))
			current_com = Community.objects.get(id = request.data.get('com_id'))
			if current_user.id == current_com.com_admins.filter(id = current_user.id).first().id:
				return Response(status = status.HTTP_200_OK)

			return Response(status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class VerifyChatMembershipAPIView(APIView):
	def post(self, request, chat_id):
		try:
			current_chat = Chats.objects.get(id = chat_id)
			current_user = User.objects.get(id = request.data['id'])
			if current_user in current_chat.users.all():
				return Response(status = status.HTTP_200_OK)

			return Response(status = status.HTTP_400_BAD_REQUEST)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)