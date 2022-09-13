from enum import Enum

class E_Stage(Enum):
    E_Stage_None = 0
    E_Stage_Question = 1 # 答题模式
    E_Stage_Piction = 2 # 拼图模式

class E_Game(Enum):
    E_Game_None = 0
    E_Game_Tang = 1 # 唐
    E_Game_Song = 2  # 宋