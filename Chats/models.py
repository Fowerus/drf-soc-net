from django.conf import settings
from django.db import models
from rest_framework import status
from rest_framework.response import Response


class Chats(models.Model):
	users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'my_chats', verbose_name = 'chat_users')
	date_creating = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'id: {self.id}'


	class Meta:
		verbose_name_plural = 'Chats'
		verbose_name = 'Chat'
		ordering = ['-date_creating']



class Messages(models.Model):
	chat = models.ForeignKey(Chats, on_delete = models.CASCADE, related_name = 'chat_messages', verbose_name = 'chat')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, related_name = 'my_messages' ,verbose_name = 'user')
	message = models.TextField(verbose_name = 'message')
	date_creating = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'id: {self.id} | chat: {self.chat.id} | user: {self.user.id}'


	class Meta:
		verbose_name_plural = 'Messages'
		verbose_name = 'Message'
		ordering = ['date_creating']



class Chats_admins(models.Model):
	chat = models.ForeignKey(Chats, on_delete = models.CASCADE, related_name = 'chats_admins', verbose_name = 'chat_admins')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, related_name = 'you_chats_admin', verbose_name = 'you_admin')
	date_creating = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f'id: {self.id} | chat: {self.chat.id} | user: {self.user.id}'


	class Meta:
		unique_together = ('chat','user')
		verbose_name_plural = 'Admins'
		verbose_name = 'Admin'
		ordering = ['-date_creating']