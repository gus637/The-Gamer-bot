import sqlite3


class DiscordUser:
    def __init__(self, username: str, user_id: int):
        self.username = username
        self.user_id = user_id
        self.level = 1
        self.xp = 0

        # Connect to the database and create the table if it doesn't exist
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, level INTEGER, xp INTEGER)"
        )
        self.conn.commit()

    def add_xp(self, xp: int):
        self.xp += xp
        if self.xp >= 100:  # Level up when XP reaches 100 or more
            self.level += 1
            self.xp -= 100  # Reset XP back to 0
            print(f"{self.username} has leveled up to level {self.level}!")

        # Update the database with the new XP and level
        self.cursor.execute(
            "UPDATE users SET xp = ?, level = ? WHERE id = ?", (self.xp, self.level, self.user_id)
        )
        self.conn.commit()

    def __del__(self):
        # Close the database connection when the object is deleted
        self.conn.close()


users = {}
