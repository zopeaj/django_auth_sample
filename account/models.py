from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authenticate = models.BooleanField(default=False)
    bio = models.TextField(default='no bio...')
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def getUsername(self):
        return self.user.username

    def setUsername(self, username):
        self.user.usernmae = username

    def isAuthenticated(self):
        return self.authenticate

    def setAuthentication(self, isAuthenticated):
        self.authenticate = authenticate

    def __str__(self):
        return f"Account of {self.user.username}"

