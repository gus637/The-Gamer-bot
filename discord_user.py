class DiscordUser:
    def __init__(self, username: str, user_id: int):
        self.username = username
        self.user_id = user_id
        self.level = 1
        self.xp = 0

    def add_xp(self, xp: int):
        self.xp += xp
        if self.xp >= 100:  # Level up when XP reaches 100 or more
            self.level += 1
            self.xp -= 100  # Reset XP back to 0
            print(f"{self.username} has leveled up to level {self.level}!")

users = {}