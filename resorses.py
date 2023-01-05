from dataclasses import dataclass

games:list[str] = ["Minecraft", "Roblox", "Pokemon", "Bloons TD", "Raft"]


@dataclass
class User:
    name: str
    level: int = 0
    exp: int = 0
        
