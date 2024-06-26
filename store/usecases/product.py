from motor.motor_asyncio import AsyncIOMotorClient
from store.db.mongo import db_client

class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database = None

uscase = ProductUsecase()