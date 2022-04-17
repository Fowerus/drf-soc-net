from django.contrib.auth.base_user import BaseUserManager



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