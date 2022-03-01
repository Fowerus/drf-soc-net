from django.urls import path

from . import views


urlpatterns = [
	#chats
	path('',views.MyChatsListAPIView.as_view()),
	path('create/', views.ChatCreateAPIView.as_view()),
	path('update-delete/<int:chat_id>/', views.ChatUpdateDeleteAPIView.as_view()),
	path('retrieve-chat/<int:id>/',views.ThisChatAPIView.as_view()),

	#messages
	path('chats-messages/<int:chat_id>/', views.ChatsMessagesAPIView.as_view())
]