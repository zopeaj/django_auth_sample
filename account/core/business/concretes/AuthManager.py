from account.models import Account
from account.core.config.passwordConfiguration import bcryptPasswordConfiguration
from account.core.business.abstracts.AccountService import accountService
from rest_framework.response import Response
from rest_framework import status

class AuthManager:
    def __init__(self, bcryptPasswordConfiguration, accountService):
        self.bcryptPasswordConfiguration = bcryptPasswordConfiguration
        self.accountService = accountService

    def authenticate(self, account):
        username = account.getUsername()
        account_user = self.accountService.getUserByName(username)
        if account_user.isAuthenticated():
            return Response({"detail": "User already authenticated"}, status=status.HTTP_204_AUTHENTICATED)
        account_user.setAuthentication(account.getUsername() is not None)
        return account_user

    def register(self, registerationData):
        username = registerationData.get("username")
        last_name = registerationData.get("last_name")
        password = registerationData.get("password")
        is_superuser = registerationData.get("superuser")
        bio = registerationData.get("bio")

        account = self.accountService.getUserByName(username)
        if account is not None:
            return Response({"detail": "User with username already exist"}, status=status.HTTP_400_BAD_REQUEST)

        passwordEncoded = self.bcryptPasswordConfiguration.encode(password)
        user = User.objects.create(username=username, last_name=last_name, password=passwordEncoded, is_superuser=is_superuser)
        account = Account(user=user, authenticate=False, bio=bio, avatar=None)
        account_data = self.accountService.create(account)
        return account_data

authManager = AuthManager(bcryptPasswordConfiguration, accountService)
