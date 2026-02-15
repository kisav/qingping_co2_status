import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Database:
    def __init__(self, path=BASE_DIR / "database.db",
                 sql_file=BASE_DIR / "queries.sql"):
        self.path = path
        self.queries = self._load(sql_file)

    def _load(self, file):
        text = Path(file).read_text(encoding="utf-8")
        queries = {}
        parts = text.split("-- name:")
        for part in parts[1:]:
            name, sql = part.split("\n", 1)
            queries[name.strip()] = sql.strip()
        print("LOADED QUERIES:", list(queries.keys()))
        return queries



    def execute(self, name, params=None, one=False, all=False):
        params = params or {}

        with sqlite3.connect(self.path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(self.queries[name], params)

            conn.commit()   # ← КРИТИЧНО

            if one:
                row = cur.fetchone()
                return dict(row) if row else None

            if all:
                return [dict(r) for r in cur.fetchall()]
