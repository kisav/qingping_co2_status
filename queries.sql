-- name:create_table
CREATE TABLE IF NOT EXISTS users (
    chat_id INTEGER PRIMARY KEY,
    app_key_secret TEXT
);

-- name:insert_user
INSERT OR REPLACE INTO users (chat_id, app_key_secret)
VALUES (:chat_id, :app_key_secret);

-- name:get_token
SELECT app_key_secret
FROM users
WHERE chat_id = :chat_id;
