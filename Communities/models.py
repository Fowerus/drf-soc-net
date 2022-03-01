from django.conf import settings
from django.db import models



class CommunityCategory(models.Model):
	name 			= models.CharField(max_length = 150, unique = True, verbose_name = 'name')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	is_active 		= models.BooleanField(default = True, blank = True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Categories'
		verbose_name = 'Category'
		ordering = ['-date_creating']



class Community(models.Model):
	name 			= models.CharField(max_length = 100, verbose_name = 'name')
	description 	= models.CharField(max_length = 2000, verbose_name = 'description')
	image 			= models.ImageField(upload_to = '../static/Communities/images', default = '../static/Communities/images/default-community-image.jpeg', verbose_name = 'image')
	creator 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'creator')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	category 		= models.ForeignKey(CommunityCategory, on_delete = models.SET_DEFAULT, default = 1)

	is_active 		= models.BooleanField(default = True)

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | creator: {self.creator.id}'


	class Meta:
		verbose_name_plural = 'Communities'
		verbose_name = 'Community'
		ordering = ['-date_creating']



class Community_admins(models.Model):
	community 		= models.ForeignKey(Community, on_delete = models.CASCADE, verbose_name = 'community', related_name = 'com_admins')
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user', related_name = 'you_admin')
	description 	= models.CharField(max_length = 100, verbose_name = 'description', default = '')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id} | community: {self.community.id} | user: {self.user.id}'


	class Meta:
		verbose_name_plural = 'Admins'
		verbose_name = 'Admin'
		ordering = ['-date_creating']



class Community_followers(models.Model):
	community 		= models.ForeignKey(Community, on_delete = models.CASCADE, verbose_name = 'community', related_name = 'com_followers')
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user', related_name = 'you_follower')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id} | community: {self.community.id} | user: {self.user.id}'


	class Meta:
		unique_together = ('community','user')
		verbose_name_plural = 'Followers'
		verbose_name = 'Follower'
		ordering = ['-date_creating']



class CommunityPosts(models.Model):
	text 			= models.CharField(max_length = 10000, verbose_name = 'text')
	author 			= models.ForeignKey(Community_admins, on_delete = models.PROTECT, verbose_name = 'author', related_name = 'com_posts_author')
	community 		= models.ForeignKey(Community, on_delete = models.CASCADE, verbose_name = 'community', related_name = 'com_posts')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id} | author: {self.author.id} | community: {self.community.id}'


	class Meta:
		verbose_name_plural = 'Posts'
		verbose_name = 'post'
		ordering = ['-date_creating']



class CommunityPostLikes(models.Model):
	post     		= models.ForeignKey(CommunityPosts, on_delete = models.CASCADE, verbose_name = 'post')
	user    		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user')
	date_creating	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id}'


	class Meta:
		verbose_name_plural = 'Likes'
		verbose_name = 'Like'
		ordering = ['-date_creating']



class CommunityPostComments(models.Model):
	post 	    	= models.ForeignKey(CommunityPosts, on_delete = models.CASCADE, verbose_name = 'post')
	user    		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user')
	comment 		= models.CharField(max_length = 5000, verbose_name = 'comment')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id}'


	class Meta:
		verbose_name_plural = 'Comments'
		verbose_name = 'Comment'
		ordering = ['date_creating']