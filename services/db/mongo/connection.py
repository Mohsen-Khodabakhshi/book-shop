import motor.motor_asyncio


class Connection:
    def __init__(self, host: str, port: int, auth: bool, user: str, pwd: str, name: str):
        self.host = host
        self.port = port
        self.auth = auth
        self.user = user
        self.pwd = pwd
        self.client = self.client_connect()
        self.db = self.db_connect(name)

    def client_connect(self):
        if not self.auth:
            return motor.motor_asyncio.AsyncIOMotorClient(self.host, self.port)

        return motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://{self.user}:{self.pwd}@{self.host}:{self.port}')

    def db_connect(self, name: str):
        return self.client[name]
