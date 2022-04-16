from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.contrib.auth import get_user_model



class UserManager(BaseUserManager):
	def _create_user(self, email, username, last_name=None, first_name=None, password=None, **extra_fields):
		username = self.model.normalize_username(username)
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, last_name=last_name, first_name=first_name, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)

		return user


	def create_user(self, email, username, last_name=None, first_name=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)

		return self._create_user(email=email, username=username, last_name=last_name, first_name=first_name, password=password, **extra_fields)


	def create_superuser(self, username, email, last_name=None, first_name=None, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self._create_user(email=email, username=username, last_name=last_name, first_name=first_name, password=password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=100, unique=True, verbose_name='Username')
	email = models.EmailField(validators=[validators.EmailValidator], unique=True, verbose_name='Email')
	image = models.ImageField(upload_to='../media/Users/images', verbose_name = 'Image')
	last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Last name')
	first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='First name')
	second_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Second name')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

	friends = models.ManyToManyField('User', blank = True, related_name = 'user_friends', verbose_name = 'Friends')
	followers = models.ManyToManyField('User', blank = True, related_name = 'user_followers', verbose_name = 'Followers')

	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ('username', 'last_name', 'first_name')

	objects = UserManager()


	def __str__(self):
		return f'id:{self.id} | username:{self.username} | email:{self.email}'


	class Meta:
		verbose_name_plural = 'Users'
		verbose_name = 'User'
		ordering = ['-created_at']