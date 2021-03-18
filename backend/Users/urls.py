from django.urls import path,include
from . import views


urlpatterns = [

	#User's auth
	path('auth/registration/',views.UserRegistrationAPIView.as_view()),
	path('auth/login/',views.UserLoginAPIView.as_view()),
	path('auth/retrieve-update-destroy/<int:id_user>/', views.UserRetrieveUpdateDestroyAPIView.as_view()),
	path('auth/user-info/<int:id_user>/',views.UserInfoAPIView.as_view()),
	path('auth/VerifyJWTUser/',views.VerifyJWTUserAPIView.as_view()),


	#User's interactions
	path('user-followers/all-user/<int:id_user>/', views.User_followersViewSet.as_view({'get':'list_user'})),
	path('user-followers/all-user-follower/<int:id_follower>/', views.User_followersViewSet.as_view({'get':'list_user_follower'})),
	path('user-followers/create-delete/', views.User_followersViewSet.as_view({'post':'create_delete'})),


	#User's posts
	path('posts/',views.UserPostsListCreateAPIView.as_view(), name = 'posts_all'),
	path('posts/posts-of-user/<int:id_user>', views.UserPostsListUserAPIView.as_view()),
	path('posts/retrieve-update-destroy/<int:id>/', views.UserPostsRetrieveUpdateDestroyAPIView.as_view()),

	path('posts/like/all/<int:post_id>/', views.UserPostLikesListCreateViewSet.as_view({'get':'list'})),
	path('posts/like/create_delete/<int:post_id>/', views.UserPostLikesListCreateViewSet.as_view({'post':'create_delete'})),

	path('posts/comment/all/<int:post_id>/', views.UserPostCommentsListCreateViewSet.as_view({'get':'list'})),
	path('posts/comment/create-delete/<int:post_id>/', views.UserPostCommentsListCreateViewSet.as_view({'post':'create_delete'}))

]