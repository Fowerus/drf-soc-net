from django.urls import path,include
from . import views


urlpatterns = [
	#main
	path('all/',views.CommunityListAPIView.as_view()),
	path('retrieve-update-destroy/<int:id>/', views.CommunityRetrieveUpdateDestroyAPIView.as_view()),
	path('retrieve-admins/<int:id>/', views.CommunityAdminsRetrieveViewSet.as_view({'get':'list'})),
	path('category/', views.CommunityCategoryAPIView.as_view()),
	path('verifyJWTPostAdmin/', views.VerifyPostAdminAPIView.as_view()),

	#Community's followers 
	path('community-followers/all-following/<int:id>/', views.Community_followersViewSet.as_view({'get':'list_following'})),
	path('community-followers/all-followers/<int:id>/', views.Community_followersViewSet.as_view({'get':'list_follower'})),
	path('community-followers/create-delete/', views.Community_followersViewSet.as_view({'post':'create_delete'})),

	#Communty's posts
	path('community-posts/all-posts/',views.CommunityPostsAPIView.as_view()),
	path('community-posts/posts_of-community/<int:id>/',views.CommunityPostsCommunityAPIView.as_view()),
	path('community-posts/retrieve-update-destroy/<int:id>/', views.CommunityPostsRetrieveUpdateDestroyAPIView.as_view()),

	#Community's likes
	path('community-likes/all/<int:id>/',views.CommunityPostLikesListCreateViewSet.as_view({'get':'list'})),
	path('community-likes/create-delete/<int:id>/', views.CommunityPostLikesListCreateViewSet.as_view({'post':'create_delete'})),

	#Community's comments
	path('community-comments/all/<int:id>/', views.CommunityPostCommentsListCreateViewSet.as_view({'get':'list'})),
	path('community-comments/create-delete/<int:id>/', views.CommunityPostCommentsListCreateViewSet.as_view({'post':'create_delete'}))
]