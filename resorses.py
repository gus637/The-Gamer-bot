from discord_user import DiscordUser

games: list[str] = ["Minecraft", "Roblox", "Pokemon", "Bloons TD", "Raft"]


class File:
    __file_path: str = ""
    
    def __init__(self, user: DiscordUser):
        self.file_name = str(user.id)
        self.USER = user
    
    def check(self, *, print_out: bool = False, Return=True, ALL=False):
        file = self.__file_path + self.file_name
        with open(file, 'r') as f:
            print(f.readline())
            level_check = self.USER.level == int(f.readline().split(" ")[2])
            xp_check = self.USER.xp == int(f.readline().split(" ")[2])
            name_check = self.USER.name == f.readline().split(" ")[2]
            id_check = self.file_name == f.readline().split(" ")[2]
        if print_out:
            print(
                f'pass = True\n'
                f'level check = {level_check}\n'
                f'xp check = {xp_check}\n'
                f'name check = {name_check}\n'
                f'id check = {id_check}'
            )
        if Return:
            if ALL:
                return level_check and xp_check and name_check and id_check
            return level_check, xp_check, name_check, id_check
        
    @staticmethod
    def get_stats(user_id: int) -> list[str, int, int, list[str]]:
        """
        :param user_id: the id of the user from wo you want to get the stats
        :return: level, xp, name, messages
        """
        file = File.__file_path + str(user_id)
        with open(file, "r") as file:
            file.readline()
            level = int(file.readline().split(" ")[2])
            xp = int(file.readline().split(" ")[2])
            name = file.readline().split(" ")[2]
            file.readline()
            messages = file.read().split("\n")
        return [name, level, xp, messages]
    
    def new_file(self, *, new_user=True):
        file = self.__file_path + self.file_name
        with open(file, "w") as file:
            if new_user:
                file.write(f"#this is the file for {self.USER.name}\n"
                           f"level = {self.USER.level} \n"
                           f"exp = {self.USER.xp} \n"
                           f"name = {self.USER.name} \n"
                           f"id = {self.USER.id} \n"
                           f"# last 5 massages\n"
                           )
        if new_user:
            with open(self.__file_path + "UserIds", "a") as f:
                f.write(self.file_name)
                f.write('\n')
                
    def save(self, *, BUG=False):
        if BUG:
            print(f"saving file \"{self.USER.name}\"")
        file = self.__file_path + self.file_name
        try:
            with open(self.__file_path + self.file_name, "r") as f:
                txt = f.read()
                with open(file + "_backup", "w") as backup:
                    backup.write(txt)
        except FileNotFoundError:
            self.new_file()
        else:
            user = self.USER
            with open(file, "w") as file:
                file.write(
                        f"#this is the file for {user.name}\n"
                        f"level = {user.level} \n"
                        f"exp = {user.xp} \n"
                        f"name = {user.name} \n"
                        f"id = {user.id} \n"
                        f"# last 5 messages\n"
                )
                for message in user.messages:
                    file.write(f"{message} \n")
        if BUG:
            print(txt)
        
    @property
    def path(self):
        return
    
    @path.setter
    def path(self, new_path):
        assert type(new_path) == str
        self.__file_path = new_path
        
    @classmethod
    def reload(cls):
        try:
            with open(cls.__file_path + "UserIds")as f:
                f.readline()
                id_txt = f.read().split('\n')
            for ID in id_txt:
                print(ID)
                if len(ID) == 0:
                    break
                stats: list[str, int, int] = cls.get_stats(int(ID))
                DiscordUser(stats[0], int(ID), level=stats[1], xp=stats[2])
        except FileNotFoundError:
            with open(cls.__file_path + "UserIds", "w") as f:
                f.write("#this file hold all of the ID's")
            
    
    
    
    
