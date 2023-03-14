from django.http import Http404
from account.models import Account
from django.contrib.auth.models import User
from account.repository.AccountRepository import AccountRepository
from account.serializers import AccountSerailizer
from rest_framework.response import Response


class AccountService:
    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def create(sef, account):
        account_db = self.get_object(account.getUsername())
        if account_db is not None:
            return Response({"error": f"user with {account_db.getUsername()} already exists"})
        serializer = AccountSerailizer(data=account)
        data = self.accountRepository.save(serializer)
        return data

    def get_object(self, username):
         user = self.accountRepository.getUserByUsername(username)
         return user

accountService = AccountService(AccountRepository(Account))
