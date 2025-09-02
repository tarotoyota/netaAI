from dataclasses import dataclass, field
from typing import List, ClassVar

@dataclass
class InferiorityTwister:
    ALL: ClassVar[List['InferiorityTwister']] = []

    name: str
    expl_not        : str = "" ; exam_not       : List[List[str]] = field(default_factory=list)
    expl_fast       : str = "" ; exam_fast      : List[List[str]] = field(default_factory=list)
    expl_fast_not   : str = "" ; exam_fast_not  : List[List[str]] = field(default_factory=list)
    expl_bit        : str = "" ; exam_bit       : List[List[str]] = field(default_factory=list)
    expl_different  : str = "" ; exam_different : List[List[str]] = field(default_factory=list)

    def __post_init__(self): self.ALL.append(self)
    @staticmethod
    def tablize():
        sections = [
            ("not", "expl_not", "exam_not"),
            ("fast", "expl_fast", "exam_fast"),
            ("fast_not", "expl_fast_not", "exam_fast_not"),
            ("bit", "expl_bit", "exam_bit"),
            ("different", "expl_different", "exam_different")
        ]
        base, index = [], []
        for i in InferiorityTwister.ALL:
            sec_html = [
                f"<tr><th id='{i.name}.{k}'>{k}</th><td>{expl}</td></tr>" +
                "".join(
                    f"<tr><td>{e[0]}</td><td>{e[1]}</td><td>{e[2]}</td></tr>"
                    for e in exam
                )
                for k, ea, xa in sections
                if (expl := getattr(i, ea)) and (exam := getattr(i, xa))
            ]
            base.append(
                f"<tr><th id='{i.name}' colspan='3' class='th_cyan'>{i.name}</th></tr>{''.join(sec_html)}"
            )

            # Check presence for index table
            marks = []
            for _, ea, xa in sections:
                exists = (getattr(i, ea) != "") and (len(getattr(i, xa)) > 0)
                marks.append("✅" if exists else "❌")

            index.append(f"""<tr><th id='th_lime'>{i.name}  </th>
                                 <td             >{marks[0]}</td>
                                 <td             >{marks[1]}</td>
                                 <td             >{marks[2]}</td>
                                 <td             >{marks[3]}</td>
                                 <td             >{marks[4]}</td>
                                 
                            </tr>""")

        return "\n".join(index), "\n".join(base)

    
    @staticmethod
    def htmlize():
        index, base = InferiorityTwister.tablize()

        td = '<td class="no-wrap">'

        head = """
            <head>
            <title>Inferiority Twisters</title>
                <link rel='stylesheet' href='static/styles.css'>
                <style>
                    td.no-wrap {
                        white-space: nowrap;
                        }
                    .left-justified-table {
                        margin-left: 0px;
                        margin-right: auto;
                        width: 50%;
                        }

                  .table-container {
    display: flex;
    gap: 20px; /* space between tables */
    align-items: flex-start;
  }
                                  </style>
            </head>
        """

        same_as_above = """<td class="same-symbol">''</td>
        """


        with open("tablize_result.html", "w", encoding="utf-8") as f:
            f.write(

        f"""
        <html>
            <head>
            <title>Inferiority Twisters</title>
                <link rel='stylesheet' href='static/styles.css'>
                {head}
            </head>
            <body>
<div class="table-container">
    <table class="left-justified-table" id="the-five-twisters">
    <tr><th>Inferiority.Twister<br><span style="font-size: smaller;">(Click to view precedent)</span></th><th>Before Reveal		 		            </th><th>After Reveal				  	                            </th></tr>
    <tr>{td} <a href="#poor_personal_life_status.bit"     >poor_personal_life_status.bit     </a></td><td>Ali mentions his poor circumstances. 	     </td><td>Bob wonders why Ali's circumstances are a little better.   </td></tr>
    <tr>{td} <a href="#stereotype.not"                    >stereotype.not                    </a></td><td>Ali acts like the stereotype.		         </td><td>Ali is the opposite of the stereotype actually.            </td></tr>
    <tr>{td} <a href="#stereotype.fast_not"               >stereotype.fast_not               </a></td>{same_as_above}                                     <td>Ali becomes the opposite of the stereotype suddenly.       </td></tr>
    <tr>{td} <a href="#stereotype.bit"                    >stereotype.bit                    </a></td>{same_as_above}                                     <td>Ali is a bit of the stereotype.		                    </td></tr>
    <tr>{td} <a href="#stereotype.fast"                   >stereotype.fast                   </a></td><td>Ali doesn't act like the stereotype.	     </td><td>Ali becomes the stereotype suddenly.		                </td></tr>
    <tr>{td} <a href="#poor_ability.fast_not"             >poor_ability.fast_not             </a></td><td>Ali is not good at the activity.	         </td><td>Ali becomes good at the activity.		                    </td></tr>
    <tr>{td} <a href="#poor_ability.bit"                  >poor_ability.bit                  </a></td><td>Ali has had only a little success.         </td><td>Bob wonders why Ali was able to have a little success.	    </td></tr>
    <tr>{td} <a href="#poor_ability.not"                  >poor_ability.not                  </a></td><td>Ali seems bad at the activity.   	         </td><td>Ali is good at the activity.			                    </td></tr>
    <tr>{td} <a href="#poor_ability.bit"                  >poor_ability.bit                  </a></td>{same_as_above}                                     <td>Ali is a little good at the activity.		                </td></tr>
    <tr>{td} <a href="#poor_ability.bit"                  >poor_ability.bit                  </a></td><td>Ali seems good at the activity.  	         </td><td>Ali is a little good at the activity.		                </td></tr>
    <tr>{td} <a href="#poor_ability.different"            >poor_ability.different            </a></td><td>Ali is bad at the activity.                </td><td>Ali is good at the different activity.                     </td></tr>
    <tr>{td} <a href="#poor_professionalism.not"          >poor_professionalism.not          </a></td><td>Ali seems disrespectful of the activity.   </td><td>Ali is respectful of the activity.			                </td></tr>
    <tr>{td} <a href="#poor_professionalism.different"    >poor_professionalism.different    </a></td>{same_as_above}                                     <td>Ali is respectful of the activity in odd respects.	        </td></tr>
    <tr>{td} <a href="#poor_ethics.not"                   >poor_ethics.not                   </a></td><td>Ali seems unethical.			             </td><td>Ali is ethical.				                            </td></tr>
    <tr>{td} <a href="#poor_ethics.different"             >poor_ethics.different             </a></td>{same_as_above}                                     <td>Ali is ethical in odd respects.			                </td></tr>
    <tr>{td} <a href="#poor_self_awareness.fast_not"      >poor_self_awareness.fast_not      </a></td><td>Ali is unaware of his insanity.            </td><td>Ali becomes aware of his insanity suddenly.                </td></tr>
    <tr>{td} <a href="#poor_self_awareness.different"     >poor_self_awareness.different     </a></td>{same_as_above}                                     <td>Ali mentions a mistaken weakness about himself.            </td></tr>
    <tr>{td} <a href="#poor_self_awareness.not"           >poor_self_awareness.not           </a></td><td>Ali seems unaware of his insanity.         </td><td>Ali is aware of his insanity.                              </td></tr>
    <tr>{td} <a href="#bad_motivation.different"          >bad_motivation.different          </a></td><td>Ali seems to have the bad motivation.      </td><td>Ali has the different motivation.                          </td></tr>
    </table>


                <table  style="width: auto; margin: 0;">
                    <tr><th rowspan="2" style="vertical-align: middle; text-align: center;">Inferiorities</th>
                                <th colspan="5" style="text-align: center; vertical-align: middle;">Twisters</th></tr>
                    <tr>                                  <th>not</th><th>fast</th><th>fast<br>_not</th><th>bit</th><th>diff<br>erent</th></tr>
                    {index}
                </table>
                </div>
                <table>
                    {base}
                </table>
            </body>
        </html>
        """
        )
        print("htmlized")



# うるとらブギーズの「卑怯」は、Aliが卑怯である旨の自覚を持つ点がミソであるから、poor_self_awareness.notでは?


poor_self_awareness = InferiorityTwister("poor_self_awareness"
,expl_fast_not = "Ali suddenly becomes self-aware about his insanity or misunderstanding."
,exam_fast_not = [
 ["かもめんたる", "山菜", "わかってくれました?"] # 説明されて気付く
,["ファイヤーサンダー", "ものまねパブ", "気付いた"] # 単に気付く
,["Key & Peele", "Country Music", "Peele plays country music many times without realizing that the lyrics are discriminatory, but suddenly he realizes."] # 単に気付く
,["フランスピアノ", "ナンパ", "俺は何をしてるんだ"] # 単に気付く
]
,expl_not = "Ali is self-aware about his insanity."
,exam_not = [
 ["Key & Peele", "Wise Bully", "The bully bullies others while explaining from a bird's eye view why he bullies others."] # 質問されて答える
,["メイプル超合金", "M1 2015", "恥ずかしいなんて感情があったら こんな格好で人前には絶対出てない"] # 質問されて答える # 自己弁護, 不可能である旨述べる論駁, 
,["ビスケットブラザーズ", "野犬", "こんな格好までしてるのに"] # 独白
,["フランスピアノ", "ナンパ", "俺の良い所と悪い所が同時に出てる"] # 独白
]
,expl_different= "Ali's awareness of his madness is different from his actual madness."
,exam_different= [
 ["トータルテンボス", "", "そんなに猿顔かな"] # 疑問
,["ジェラードン", "", "鼻息荒くてごめん"] # 謝罪
]
)


"Is it because I'm just a billiards player? + Are you aware of that yourself?"

["Am I so {x}?", "Sorry for being {x}."]
["You're different from {x}.", "That's not where your problem lies."]



path_not = [
 "I just did {x}." # 自己弁護, 説明, 釈明, 非難
,"Because I did {x}?" # 質問, 非難
,"I won't do {x} again!" # 自己弁護, 釈明
,"When I was doing {x}, ..." # 説明
,"Even though I did {x}?" # 質問, 非難
#,"Who did x? + It's me."
]

["Are you aware of that yourself?"]



path_fast_not = [
 "What I'm doing?"
,"Oh damn. Now I see it."
]

["You just realized that now?"]



poor_ability = InferiorityTwister("poor_ability"
,expl_bit = "Ali has a little bit of the ability."
,exam_bit = [
 ["千鳥", "妊娠", "'できちゃったみたい'の部分だけ上手い"]
,["ファイヤーサンダー", "養成所", "おもんなくない"]
,["ななまがり", "_", "まあまあ強かった"]
]
,expl_fast_not = "Ali suddenly gains the ability."
,exam_fast_not = [
 ["キングオブコメディ", "タレントオーディション", "発話障害を持つ出っ歯の男が急に少しだけ喋れるようになる."]
,["ななまがり", "バッティングセンター", "野球をしている男が急にスランプに陥り、急にスランプを脱する."]
,["くらげ", "?", "男が急に婉曲表現の意味を理解できるようになる."]
,["ななまがり", "心が折れる音演奏会", "上達"]
,["ファイヤーサンダー", "養成所", "一回のネタ見せで急速に成長する"]
]
,expl_not = "Ali has the ability enough."
,exam_not = [
 ["うるとらブギーズ", "卑怯", "A man who uses underhanded tactics in a fight turns out to be strong even without using underhanded tactics."]
,["フランスピアノ", "お笑いコンビ", "まあまあいいのかよ"]
]
,expl_fast="_"
,exam_fast = [
 ["さらば青春の光", "パワースポット", "二年前から"]
]
,expl_different="_"
,exam_different=[
 ["霜降り明星", "採血", "採血は下手だが血圧測定だけ上手い."]
]
)

["(Ali is only good at a few parts of activity x.)", "(Ali is a bit good at activity x.)"]
["Why are you only good at that?", "Why are you a bit good at that?"]

[""]
[]







stereotype = InferiorityTwister("stereotype"
# 相性はいいよね 魔女 ななまがり やりたい
,expl_not = "_"
,exam_not = [
 ["ファイヤーサンダー", "撮り鉄", ""]
,["さらば青春の光", "パリヴィ", "_"]
,["相性はいいよね", "スタミナバクダングリル", "_"]
]
,expl_bit = "Ali becomes a bit of the stereotype."
,exam_bit = [
 ["ファイヤーサンダー", "天才", "A man modeled after L from Death Note eats something salty instead of sweet."]
,["ファイヤーサンダー", "型破り", "_"]
 # 千鳥 屁こき田 それは何?
]
,expl_fast = "Ali Becomes the stereotype quickly."
,exam_fast = [
 ["Family Guy", "s9e13", "Shortly after entering high school, Peter develops a personal life similar to that of the Columbine shooter and actually completes his preparations for a mass shooting."]
,["Family Guy", "s9e13", "Shortly after getting a dirt bike, Peter finds a girlfriend who suits it. She's a student at an alternative high school, and after reading a poem she discarded, Peter thinks she has a talent for poetry."]
,["Family Guy", "s12e13", "In the NFL Experience, Chris experiences one stereotypical NFL player after another. He ultimately shoots himself in the chest to donate his brain to science." "Family Guy", "S5E12", "After seeing the Redneck Comedy Festival, Peter quickly becomes a redneck, buying a pickup truck and engaging in incest."]
,["Family Guy", "s12e2", "Shortly after meeting the characters like Mad Max raiders in SEARS, Peter becomes one of them and acts like them."]
,["さらば青春の光", "画家", "Even though the man hasn't painted a single picture yet, he behaves in a stereotypical manner like an artist in a slump."]
,["The Simpsons", "s5e18", "Shortly after being adopted by Mr. Burns, Bart becomes arrogant toward the driver of their hire car."]
,["American Dad", "s5e11", "It's not crack. I bought it on a park bench outside a soup kitchen. Oh my god, it's crack."]
]
,expl_fast_not="Ali suddenly stops to attack others and starts to praise."
,exam_fast_not=[
 ["ファイヤーサンダー", "教育パパ", "The father canges his attitude for his son depends on his son's exam score is 100 or less than or equal to 99."]
,["ファイヤーサンダー", "頑固店主", "After losing a fight with a customer, the chef suddenly goes from aggressive to overly polite."]
]
)

insane_act = InferiorityTwister("insane_act"
,expl_not = "Ali's behavior x isn't an insane action."
,exam_not = [
 ["_", "_", "Is he your friend? + No, I don't know him. + Another madman?"]
]
,expl_fast = "Ali's behavior x isn't something from the past."
,exam_fast = [
 ["かもめんたる", "蛇", "それ今日初めて見るけど"]
,["ビスケットブラザーズ", "野犬", "さっき拾ったお気に入りの棒が"]
,["さらば青春の光", "パワースポット", "二年前から"]
]
)

poor_personal_life_status = InferiorityTwister("poor_personal_life_status"
,expl_not = "Ali has a normal personal life status."
,exam_not = [
 ["ななまがり", "", "It is indirectly suggested that the insane guys have partially normal personal lives, such as wearing a wedding ring and owning a cledit card."]
,["ネコニスズ", "M1 2024", "The tsukkomi says the boke who pretend to be a baby is the manager at his part-time job."]
,["Rick and Morty", "S6E8", "Pissmaster has a daughter."]
,["Rick and Morty", "S1E1", "Scary Terry has a son and a wife."]
,["空気階段", "火事", ""]
,["鬼ヶ島", "操り人形", "バスケ部で主将だった"]
])

poor_professionalism = InferiorityTwister("poor_professionalism"
,expl_not = "_"
,exam_not = [
 ["フランスピアノ", "スイカ農家", "ちゃんとスイカ好きなんかい"]
,["さらば青春の光", "猿回し", "作家を入れない"]
])

poor_ethics = InferiorityTwister("poor_ethics"
,expl_not = "_"
,exam_not = [
 ["うるとらブギーズ", "卑怯", "_"]
]

,expl_different = "_"
,exam_different = [ 
 ["ファイヤーサンダー", "ぼったくりバー", "卑怯やん"] # different_not?
])

bad_motivation = InferiorityTwister("bad_motivation"
,expl_different = "_"
,exam_different = [
 ["ファイヤーサンダー", "迷惑系", ""]
,["シティホテル3号室", "駄菓子", ""]
])

InferiorityTwister.htmlize()
##################################################################################

# ファイヤーサンダーの爆弾まあとkee y and peeleのmirrorは同じ

#emotionless = InferiorityTwister("emotionless"
#,expl_not = "_"
#,exam_not = [
# ["フランスピアノ", "スイカ農家", "ちゃんとスイカ好きなんかい"] # ???
#]
#)

# 呵責 は maliceと同じか


deliberate = InferiorityTwister("deliberate"
,expl_not = "Ali does M unintentionally."
,exam_not = [
 ["うるとらブギーズ", "卑怯", "A man who uses underhanded tactics in fights is surprised to discover that he is using underhanded tactics and makes an effort to improve."]
,["うしろシティ", "職員室", "悪気がある方がいいよ"]
,["見取り図", "マネージャー", "悪気はないんで +s+ そっちの方が怖いよ"]
]
)

unsucessful = InferiorityTwister("unsucessful"
,expl_bit="_"
,exam_bit=[
 ["_", "_", "_"] # なんで登録者１０人いるの?
]
)

#confusion = InferiorityTwister("confusion"
#,expl_not = "Ali is not confused."
#,exam_not =[
# ["", "", ""] # I'm sober. I'm an abled. I don't use illegal drugs.
#]
#)

epithet = InferiorityTwister("epithet"
,expl_different = "???"
,exam_different = [
 ["かもめんたる", "未来人", "未来人ってだけじゃねーだろ"]
,["キングオブコメディ", "お見合い", "思春期ってだけじゃないだろ"]
,["かもめんたる", "砂浜店長", "もう怒るのが遅いとかじゃない"]
,["ジャルジャル", "おばはん", "ヤンキーでもなんでもない"]
]
)




# why there is no "good_ability"?

# There are two type of madman that one clearly has a poor personal life status and the not one.


# Why is my reward構文はpoor_personal_life_status.notか?



# QuickReveal ヨハン
# かもめんたる 秋山 だからか Quick Suddenly
# インパルス 携帯屋 # suddenly become stereotype

good_personal_life_status = InferiorityTwister("good_personal_life_status"
,expl_not = "Ali has a poor personal life status."
,exam_not = [
 ["インパルス", "ヨハン", "_"]
,["ジェラードン", "マロン", "_"]
])







being_attacked = InferiorityTwister("being_attacked"
,expl_different="Ali is not attacked but the other person is attacked."
,exam_different=[
 ["キングオブコメディ", "不登校", "なんで君がいじめらんなかったの"]
]
)

attack = InferiorityTwister("attack"
,expl_fast = "Ali suddenly starts to attack others."
,exam_fast=[
 ["The Simpsons", "The Simpsons Movie", "Ned's sons say I want Homer as "]
,["ななまがり", "?", "死体だ"] # ???
]
# fast 子供に軽口を叩かれた教師がすぐに血縁関係について暴露する
)









trauma = InferiorityTwister("trauma"
,expl_bit = "Ali's trauma is minor."
,exam_bit = [
 ["ニューヨーク", "ダークサイドに堕ちた大物司会者", ""]
,["?", "復讐", "街でぶつかった"]
])





# 

# hypo_si シティホテル３号室 文学青年 エッセイ

# differentは事実と異なる

seriousness = InferiorityTwister("seriousness"
,expl_not = "_"
,exam_not = [
 ["ニューヨーク", "路上アーテイスト", "知り合いに見られたら恥ずかしいんで"]
])

# 相性はいいよね コント 魔女



def gen():

    action = "Ali, an athlete, is bitterly complaining to the event organizer, about the low turnout at her events."

    action = "Ali subjects his junior members on the sports team to harsh training and physical punishment."

    action = "Ali, a school gangster, uses dirty tactics in fights."

    action = "Ali, a nuisance youtuber smears a restaurant."

    action = "Ali becomes stuck in his painting and turns to self-destructive."

    action = "Ali, a school gangster, uses dirty tactics in fights."

    action = "Ali, an employee of a mega-farm, negotiates with poor farmers to buy their land, but the atmosphere between them becomes hostile."

    action = "Ali causes trouble for event organizers by committing acts of vandalism and performing unethically during his own concerts."

    # Answer the following question. If yes, assign "y". If no, leave it brank.
    # Note the reason why you answered so as comments. Start answer with ```python.

    q1 = "" # Ali is not self-aware about his abnormality.                                                                                          poor_self_awareness.not		          
    q2 = "" # Ali is incompetent or lacks ability.                                                                                                  poor_ability.not, .bit
    q3 = "" # Ali does the action intentionally.                                                                                                    deliberate.not
    q4 = "" # Ali's purpose in the action is only to harm others.                                                                                   deliberate.not    
    q5 = "" # The same occupation or activity that Ali does is generally considered as a high social status.                                        good_personal_life_status.bit, .not ; if not : poor_personal_status.bit, .not
    q6 = "" # Ali has likely been involved in the activity for a long time.                                                                         strereotype.fast
    q7 = "" # In fiction, characters who does behaviors like Ali are often talented.                                                                poor_ability.bit
    q8 = "" # In fiction, characters like Ali portrayed as psychopath or emotionless.                                                               watermelon
    q9 = "" # In fiction, characters like Ali portrayed as villain.                                                                                 





    q8 = "" # Does Ali's occupation or activity requires some kind of technique? iow, Is this not something that anyone can do?     poor_ability.bit









