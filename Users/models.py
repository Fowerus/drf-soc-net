import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin



#User's auth
class UserManager(BaseUserManager):
	def _create_user(self, username, email, last_name = None, first_name = None, password = None, **extra_fields):
		username 	= self.model.normalize_username(username)
		email 		= self.normalize_email(email)
		user 		= self.model(username = username, email = email, last_name = last_name, first_name = first_name, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)

		return user


	def create_user(self, username, email, last_name = None, first_name = None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)

		return self._create_user(username = username, email = email, last_name = last_name, first_name = first_name, password = password, **extra_fields)


	def create_superuser(self, username, email, last_name = None, first_name = None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self._create_user(username = username, email = email, last_name = last_name, first_name = first_name, password = password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	username 		= models.CharField(max_length = 100, unique = True, verbose_name = 'username')
	email 			= models.EmailField(validators = [validators.EmailValidator], unique = True, blank = False, verbose_name = 'email')
	image 			= models.ImageField(upload_to = '../static/Users/images', default = '../static/Users/images/default-user-image.jpeg', verbose_name = 'image')
	last_name 		= models.CharField(max_length = 150, null = True, blank = True, verbose_name = 'last_name')
	first_name 		= models.CharField(max_length = 150, null = True, blank = True, verbose_name = 'first_name')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ('email','last_name','first_name')

	objects = UserManager()


	@property
	def token(self):
		return self._generate_jwt_token()


	def get_full_name(self):
		return self.username


	def get_short_name(self):
		return self.username


	def _generate_jwt_token(self):
		dt = datetime.now() + timedelta(days = 60)

		token_encode = jwt.encode({
			'id': self.pk,
			'username':self.username,
			'email':self.email,
		}, settings.SECRET_KEY, algorithm='HS256')

		token_decode = jwt.decode(token_encode, settings.SECRET_KEY, algorithms=["HS256"])

		return token_decode

	def __str__(self):
		return f'id:{self.id} | username:{self.username} | email:{self.email}'


	class Meta:
		verbose_name_plural = 'Users'
		verbose_name = 'User'
		ordering = ['-date_creating']



class User_followers(models.Model):
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user', related_name = 'user')
	user_follower   	= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,verbose_name = 'user_follower', related_name = 'user_follower')
	date_creating 		= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id:{self.id}'


	class Meta:
		unique_together = ("user", "user_follower")
		verbose_name_plural = 'Followers'
		verbose_name = 'Follower'
		ordering = ['date_creating']



#User's posts
class UserPosts(models.Model):
	text 			= models.CharField(max_length = 10000, verbose_name = 'text')
	author 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'author', related_name = 'user_posts')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')
	
	def __str__(self):
		return f'id: {self.id} | author: {self.author}'


	class Meta:
		verbose_name_plural = 'Posts'
		verbose_name = 'Post'
		ordering = ['-date_creating']



class UserPostLikes(models.Model):
	post     		= models.ForeignKey(UserPosts, on_delete = models.CASCADE, verbose_name = 'post')
	user    		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user')
	date_creating	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id}'


	class Meta:
		verbose_name_plural = 'Likes'
		verbose_name = 'Like'
		ordering = ['-date_creating']



class UserPostComments(models.Model):
	post 	    	= models.ForeignKey(UserPosts, on_delete = models.CASCADE, verbose_name = 'post')
	user    		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'user')
	comment 		= models.CharField(max_length = 5000, verbose_name = 'comment')
	date_creating 	= models.DateTimeField(auto_now_add = True, verbose_name = 'date_creating')

	def __str__(self):
		return f'id: {self.id}'


	class Meta:
		verbose_name_plural = 'Comments'
		verbose_name = 'Comment'
		ordering = ['date_creating']