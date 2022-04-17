from django.db import models



class GroupCategory(models.Model):
	name = models.CharField(max_length=150, unique=True, verbose_name='Name')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Categories'
		verbose_name = 'Category'
		ordering = ['-created_at']



class Group(models.Model):
	name = models.CharField(max_length=150, verbose_name='Name')
	description = models.CharField(max_length=2000, verbose_name='Description')
	image = models.ImageField(upload_to='../static/Communities/images', verbose_name='Image')
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True, verbose_name='Creator')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

	category = models.ForeignKey(CommunityCategory, on_delete = models.SET_NULL, null = True, verbose_name = 'Category')

	def __str__(self):
		return f'id: {self.id} | name: {self.name}'


	class Meta:
		verbose_name_plural = 'Groups'
		verbose_name = 'Group'
		ordering = ['-created_at']