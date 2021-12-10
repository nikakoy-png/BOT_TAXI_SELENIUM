import pymongo


class DB:

    def __init__(self, host):
        self.db_client = pymongo.MongoClient(host)
        self.current_db = self.db_client["DB_user_TAXI"]
        self.collection = self.current_db["user"]

    def register_new_user(self, fio, id_dr, id_tg):
        request = {
            'id_tg': str(id_tg),
            'id_dr': str(id_dr),
            'fio': str(fio),
        }
        self.collection.insert_one(request)
        print(f"successful recorded {fio}")

    def get_user(self, id_tg):
        return self.collection.find_one({'id_tg': str(id_tg)})
