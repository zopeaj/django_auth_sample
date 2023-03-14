from django.http import Http404
from account.models import Account
from django.contrib.auth.models import User
from account.repository.AccountRepository import AccountRepository

class AccountService:
    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def create(sef, account):
        account_data = self.accountRepository.save(account)
        return account_data

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist::
            return Http404

accountService = AccountService(AccountRepository(Account))
