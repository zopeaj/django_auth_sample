from account.models import Account

class AccountRepository:
    def __init__(self, account):
        self.account

    def save(self, data):
        self.account.create(**data)
        self.account.save()
        return data

accountRepository = AccountRepository(Account)
