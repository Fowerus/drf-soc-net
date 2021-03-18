from django.urls import path

from . import views


urlpatterns = [
	path('',views.MyChatsListAPIView.as_view()),
	path('create-delete/', views.ChatCreateUpdateDeleteAPIView.as_view()),
	path('retrieve-chat/<int:id>',views.ThisChatAPIView.as_view()),
	path('chats-messages/<int:chat_id>', views.ChatsMessagesAPIView.as_view())
]