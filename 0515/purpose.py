from dataclasses import dataclass

@dataclass
class Purpose:
    true_purpose:str
    false_purpose:dict # {action : false purpose}

# If there is a man who go to a massage parlor to get a massage, he's insane.
# Add new items in sexual_desire.false_purpose. Start answer with ```python.`

sexual_desire = Purpose("sexual_desire",
{"go to a massage parlor": "massage"
,"go to a soap land": "bath"
,"go to a night pool": "swim"
,"go to FKK": "take a sauna" 
,"go to Southeast Asia": "sightseeing"
,"go to a strip club": "enjoy to watch dance"
,"watch a porn": "enjoy the story"
,"watch female sports": ""

,"buy Playboy magazine": "read the articles"
,"go to a love hotel": "rest"
,"install Tinder": "make friends"
})

desire_for_money = Purpose("desire_for_money",
{"go to a casino": "enjoy gaming"
,"act like a nuisance youtuber": "enjoy to cause a nuisance"
})

material_desire = Purpose("material_desire",
{"buy a watch": "check the time"
,"buy a car": "move fast"
})


"""

greed = InferiorityTwister("greed"
,expl_bit = "_"
,exam_bit = [
 ["ファイヤーサンダー", "迷惑系", ""]
,["シティホテル3号室", "駄菓子", ""]
])
"""

# 迷惑系 楽しむために
# ソープ 風呂に入るために
# ナイトプール 泳ぐために
# パチンコ 楽しむために
# エロゲ 遊ぶために
# ヘパリーゼ 味わうために ななまがり初瀬
