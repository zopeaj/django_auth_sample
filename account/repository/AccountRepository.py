from account.models import Account

class AccountRepository:
    def __init__(self, account):
        self.account

    def save(self, serializer):
        if serializer.is_valid():
            data = serializer.save()
        return data

accountRepository = AccountRepository(Account())
