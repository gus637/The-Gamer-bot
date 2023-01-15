class DiscordUser:
    users = {}
    
    def __init__(self, username: str, user_id: int, *, level=1, xp=0, new_user=False):
        if new_user:print("making new user")
        self.name = username
        if new_user:print(f"name = {username}")
        self.id = user_id
        if new_user:print(f"id = {user_id}")
        self.level = level
        if new_user:print(f"level = {level}")
        self.xp = xp
        if new_user:print(f"xp = {xp}")
        self.__class__.users[user_id] = self
        self.message = []
        
    def add_xp(self, xp: int) -> bool:
        level_up = False
        self.xp += xp
        while self.xp >= 100:# Level up when XP reaches 100 or more
            self.level += 1
            self.xp -= 100  # Reset XP back to 0
            print(f"{self.name} has leveled up to level {self.level}!")
            if not level_up:
                level_up = True
        return level_up
    
    @property
    def messages(self) -> list[str]:
        return self.message
    
    @messages.setter
    def messages(self, new_message):
        self.message.append(new_message)
        if len(self.message) > 5:
            self.message.pop(0)
