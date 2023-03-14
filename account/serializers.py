from rest_framework import serializers
from account.models import Account
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.OneToOneField(User, required=True)
    authenticate = serializers.BooleanField(required=True, default=False)
    bio = serializers.TextField(required=True, default='no bio...')
    avatar = serializers.ImageField(upload_to='avatars', default=None)
    created = serializers.DateTimeField(input_formats=None, default_timezone=None)
    updated = serializers.DateTimeField(input_formats=None)

    class Meta:
        model = Account
        fields = ['authenticate', 'bio', 'avatar', 'created', 'updated']

