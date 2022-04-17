from djoser.serializers import UserDeleteSerializer



class CustomUserDeleteSerializer(UserDeleteSerializer):

	def validate(self, attrs):
		for item in self.instance.images.all():
			item.delete()

		return self.validate(attrs)