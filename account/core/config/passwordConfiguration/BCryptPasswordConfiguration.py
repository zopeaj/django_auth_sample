from passlib.context import CryptContext

passwordContext = CryptContext(scheme=['bcrypt'])

class BCryptPasswordConfiguration:
    def encode(self, plain_password) -> str:
        return passwordContext.hash(plain_password)

    def verify(self, plain_password, hashed_password) -> bool:
        return passwordContext.verify(plain_password, hashed_password)

bcryptPasswordConfiguration = BCryptPasswordConfiguration()

