import services


class BaseCRUD:
    def __init__(self, create_model, update_model, read_model):
        self.create_model: str = self.get_col_name(create_model)
        self.update_model: str = self.get_col_name(update_model)
        self.read_model: str = self.get_col_name(read_model)

    @staticmethod
    def get_col_name(model) -> str:
        try:
            return str(model.__config__.table)
        except:
            return ""

    @staticmethod
    def db(model: str):
        return services.global_services.DB[model]

    async def get(self):
        return await self.db(self.read_model).find_one({"name": "ali"})
