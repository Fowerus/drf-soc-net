from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.contrib.auth import get_user_model

from django_resized import ResizedImageField

from .managers import UserManager 



class Image(models.Model):
	full_image = ResizedImageField(crop=['middle', 'center'], upload_to='../static/images/Users')
	middle_image = ResizedImageField(crop=['middle', 'center'], null = True, upload_to='../static/images/Users')
	small_image = ResizedImageField(crop=['middle', 'center'], null=True, upload_to='.../static/images/Users')
	
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

	likes = models.ManyToManyField('User', blank=True, related_name='image_likes', verbose_name='Likes')

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		if self.middle_image is None:
			self.middle_image = self.full_image
		if self.small_image is None:
			self.small_image = self.full_image

		return self.save(force_insert, force_update, using, update_fields)


	def __str__(self):
		return f'{self.id}'


	class Meta:
		verbose_name_plural = 'Images'
		verbose_name = 'Image'
		ordering = ['created_at']



class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=100, unique=True, verbose_name='Username')
	email = models.EmailField(validators=[validators.EmailValidator], unique=True, verbose_name='Email')
	last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Last name')
	first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='First name')
	second_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Second name')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

	image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_image', verbose_name='Image')
	images = models.ManyToManyField(Image, blank=True, related_name='user_images', verbose_name='Images')
	friends = models.ManyToManyField('User', blank=True, related_name='user_friends', verbose_name='Friends')
	followers = models.ManyToManyField('User', blank=True, related_name='user_followers', verbose_name='Followers')

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
		ordering = ['-updated_at']