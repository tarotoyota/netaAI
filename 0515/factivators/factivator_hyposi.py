from factivators.class_factivatortable import FactivatorTable

factivator_hyposi=FactivatorTable("factivator_hyposi"
,[
     ["さらば青春の光", "男優", "A porn cast executes stereotypical behavior of actors. He conflicts with the director."]
    ,["SNL", "The Actress", "A porn cast executes stereotypical behavior of actresses. She conflicts with the director."]
    ,["Aマッソ", "手タレ", "A parts model is treated as a model by her manager. The manager conflicts with the parts model."]
    ,["ライス, ファイヤーサンダー", "ぼったくりバー", "A rip-off bartender makes an effort and get skilled. Thanks to his efforts, the rip-off prices become fair prices for the customers. The owner is confused by the bartender."]
]
,{
# hypo_iに.abn_hypoと.nor_agentを加える
 "BEFORE; .effort, .action, .suffer, .appear, .slump, .nor_obj, .nor_agent": ["Ali executes {X} and causes trouble for Bob."]# ただeasa+nをアサインするより、pressureのアサインも同時にした方がbr効率が高い。
# 'BR;'が接頭するキー以下のflineは全てARにアサインせよ
,"REVEAL; .abn_hypo, .hypo_i": ["Ali is actually charged in {X}"]
,".effort, .action, .suffer, .appear, .slump, .nor_obj": ["Bob says it's strange and too early for Ali, a {.hypo_i}, to do {X}."]
,".suffer, .slump": ["If you have the talent, you're not a {.hypo_i}.", "You don't have the talent so you're a {.hypo_i}.", "The reason why your efforts don't lead to results is because you're a {.hypo_i}.", 'There are no walls for {.hypo_i} to hit.', "There's no pressure for {.hypo_i}."]
,".imposing, .bottom": ["Bob calls Ali 'a {X1} {X2}'"] # bottomは後で実装
,".rephrase": ["Don't call {X[0]} {X[1]}.", "If {s} does it, it's {X[1]}. If {.hypo_i} does it, it's {X[0]}."]
,".hypo_i_pn, hypo_i": ["I've been complimented on being (able to do/ good at) x. +s+ Bob: That is an insult."]
,".hypo_s, .hypo_i": ['{.hypo_i} is not a {.hypo_h}.', 'How could you be jealous of {.hypo_s}?', 'How could you look down on {.hypo_i}?', "Ali: It's hard to succeed as a {.hypo_s}, so I became a {.hypo_i}. - Bob: It's even harder to succeed as a {.hypo_i}.", "Ali: I'm a failure as a {.hypo_h}. - Bob: A {.hypo_i} is not a {.hypo_h}.", "Ali: Is it so difficult to being a {.hypo_h} - Bob: You're not a {.hypo_h}.", 'Ali: Seeing {.hypo_s} made me lose confidence. - Bob: Why you can lose?', 'Ali: I want to quit being a {.hypo_h}. - Bob: A {.hypo_i} is not a {.hypo_h}.', 'Ali: I fulfilled my dream of becoming a {.hypo_h} - Bob: a {.hypo_i} is not a {.hypo_h}.', 'Ali: I was told that I was suited to be a {.hypo_i}. - Bob: People who are suited to be {.hypo_i} are not suited to be {.hypo_h}.', "Ali: I don't want to lose to other {.hypo_i}. - Bob: You're already losing just by being a {.hypo_i}.", "Ali: Maybe I don't have the talent for {.hypo_h}. - Bob: You're {.hypo_i} because you don't have the talent for {.hypo_h}.", "Ali: I'm thinking of giving up my career as a {.hypo_i}. - Bob: Why not aim for becoming a {.hypo_h} instead?", "Ali: I feel like I'm wasting my potential as a {.hypo_i}. - Bob: You could always strive to become a {.hypo_h}.", "Ali: I want to be a {.hypo_h}. Now, I'm a {.hypo_i}. - Bob: That's great, you can be a {.hypo_h} someday.", "Ali: I'm struggling as a {.hypo_i}. - Bob: Have you considered aiming higher, like becoming a {.hypo_h}?", "Ali: Being a {.hypo_i} is tough. - Bob: That's why you should aspire to be a {.hypo_h}.", "Ali: I'm thinking of quitting my job as a {.hypo_i}. - Bob: Instead of quitting, why not work towards becoming a {.hypo_h}?", "Ali: I've been a {.hypo_i} for so long, I'm not sure I can be anything else. - Bob: Don't limit yourself, you could become a {.hypo_h}.", "Ali: I enjoy being a {.hypo_i}, but I feel there's more I could do. - Bob: Have you considered the possibilities as a {.hypo_h}?", 'Ali: I keep failing as a {.hypo_i}. - Bob: Every failure is a step towards becoming a {.hypo_h}.', "Ali: My parents wanted me to be a {.hypo_h}. Now, I'm a {.hypo_i}. - Bob: It's not too late to fulfill their wishes.", 'Ali criticizes {.hypo_s} +s+ Ali: This cut off my path to mainstream success. +s+ Bob: In the first place, there is not that.', "Ali: I'll repay you by being a successful {.hypo_i}. +s+ Bob: To be a successful {.hypo_i} is to fail.", "Ali: I'm embarrassed by this failure as a {.hypo_i}. +s+ Bob: Isn't it more embarrassing to be a {.hypo_i}?", "Ali: I'm embarrassed by this failure as a {.hypo_i}. +s+ Bob: Being a {.hypo_i} is a failure.", "Ali: I don't wanna lose to other {.hypo_i}. +s+ Bob: You're already losing just by being a {.hypo_i}.", 'Ali: I was told that I was suited to be a {.hypo_i}. - Bob: Perhaps it is an insult.'] 
,".modifier": ["Ali: I'm {X}. +s+ Bob: That's worse than not being that.", "Ali: I'm {X}. +s+ Bob: Are there {X} in {.hypo_i}?", "Ali: Don't mess with me, I'm {X} +s+ Bob: So I mess with you."]
,".too_slow": ["Ali suddenly starts {.too_slow} and Bob says to Ali: It won't be in time."]
,".pressure_emergency": ['Usually at times like this, {s} come.', 'Normally, in these situations, {i} are not {h}.', 'The {i} are the least needed right now.', "Don't give off the impression that you're a {s}, it's confusing.", '{i} are not {h}, but they are even less so in these circumstances.', "When we say {s}, we don't usually mean {i}.", 'When I look at {i} in this situation they look even weaker.', 'Right now, {i} is more dangerous than that.', 'Since {i} came, I have one more thing to deal with.', 'The gap between {h} and {i} becomes more apparent in these circumstances.']
# ▲pressureの各種類に対応して分割せよ

,"OTHER": [""]
# ,"OTHER_ALI_MAKE_SOMEONE": ['I want to become {.hypo_i} and make my parents happy', 'I want to become {.hypo_i} and get back at those who bullied me.', 'I want to become {.hypo_i} and inspire others to follow their dreams.', 'I want to become {.hypo_i} and prove that hard work pays off.', 'I want to become {.hypo_i} and leave a legacy that my family can be proud of.']
}
,note="Refers to FactAgentSupInf, FactAgentEasa, FactAgentEasa, FactAgentBinary"
)





