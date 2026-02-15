from database_utils import Database

db = Database()

def init_db():
    db.execute("create_table")

def create_user(chat_id, secret):
    db.execute("insert_user", {
        "chat_id": chat_id,
        "app_key_secret": secret
    })

def get_token(chat_id):
    row = db.execute("get_token", {"chat_id": chat_id}, one=True)
    return row["app_key_secret"] if row else None
