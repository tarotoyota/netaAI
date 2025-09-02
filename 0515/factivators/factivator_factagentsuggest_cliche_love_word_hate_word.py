from factivators.class_factivatortable import FactivatorTable

factivator_factagentsuggest_cliche_love_word_hate_word=FactivatorTable("factivator_factagentsuggest_cliche_love_word_hate_word"
,[
 ["Family guy", "S17E14", "When Peter says 'I'm don't gonna have sex with you.' in Quagmire's house, a pitfall opens. When Joe says 'Glenn, is it okay if I stay the night?', a robot kicks him out."]
,["Rick and Morty", "S2E7", "When Rick says 'These are all good points, I need to take a long look at myself.' in the counseling sentre, a flamethrower spews fire at the location of the counselor's couch."]
,["Family guy", "S8E1", "To melt ice, Stewie says 'You wanna go for walk?', 'You wanna treat, boy?', 'Let's you go for a ride in the car', 'You wanna sleep in the bed with us?' to Brian's tale wag. When Stewie says 'I'll give you a bath', the tail stops."]
,["ラーメンズ", "にっぽん語", "Two foreigner guys read aloud a Japanese language textbook. 'I'm Suzuki', 'I don't know, that grass grew on its own', 'That's flour or something', 'These are mosquito bites'"]
,["SNL", "Rosetta Stone", "Guys are learning Thai language phrases. 'How much?', 'Is that for the whole night?', 'Oh my God! What have I done?', 'Ping pong ball', 'I need to speak with the American embassy'"]#,"'So I gonna Thailand for... a thing', 'I'm also learning Thai... for business'"
,["Kee and Peele", "Alien", "Two black guys identify the survivors are aliens or not by their answer to the following question: 'Would you let me date your daughter?', 'What do you think about the police?'"]
,["F is for family", "", "When the wife says 'I got pregnant', his husband wakes up."]
,["ロビンフット", "お見合い", ""]
,["さらば青春の光", "後継者", ""]
# 荷物多い
]

,{ # X = .love_word, .hate_word, .cliche_phrase from FactAgentSuggest
 "Genre 1: If the phrases are in the foreign language(.cliche, .hate_word, .love_word))":[
     "(Ask for/ Only know) the spelling of X"
    ,"(Ask for/ Only know) the pronunciation of X"
    ,"Ask for translate X"           
    ,"Only know X in the language"   
    ,"Can pronounce only X fluently" 
    ,"Play the audio for X"          
    ,"Make a note of X"              
    ,"Mark X in a textbook"
    ,"Ask a native speaker to correct their pronunciation of X"
    ,"Only know how to say hello in sign language"
    ,"Only know how to write hello in Braille"
    ,"Carry a card with the letter X on it"
]
,"Genre 2: If S has completed V.(.cliche, .hate_word, .love_word))":[
     "Dream about X"                 #
]
,"Genre 3: If S tries to V.(.cliche, .hate_word, .love_word)":[
     "Memorize X"                    # 
    ,"Create a mnemonic for X"       # 
    ,"Teach X to his fellow"         # 
    ,"Speak X in front of a mirror"  #
    ,"Whisper X to himself repeatedly" #
]
,"Genre 4: Creative(.cliche, .hate_word, .love_word)": [# カンペ
     "Find words that rhyme with X"  # 
    ,"Say X for act him"              # 
    ,"Say X to impersonate him"
]
,"Genre 5: Cope(.hate_word, .love_word)":[
     "Trap activates when someone says X"
    ,"Wake up when someone says X"
]
,"Genre 6: Mistake(.cliche, .hate_word, .love_word)":[ # 以下のように、そのfactivator_lineがどの状況においてavailableかをタグ付けする事で、ストーリーラインの要請に応じたflineをサジェストできる。
     "Say X to the wrong person" # Meeting, phone call, through the door, darkness, voicemail
    ,"Say X when he was said 'Remember what he said then.'" # trouble, difficulty
    ,"Say X when he was said 'Remember what you said then.'" # trouble, difficulty
]
,"love_word": [
 "He displays a piece of calligraphy that reads {X}."
,"His password is {X}"
,"He wakes up when he hears {X}"
,"He has {X} tattooed on his arm"
,"He named his pet after {X}"
,"His email address contains {X}"
,"He uses {X} as his gaming username"
,"His car's license plate spells out {X}"
,"He named his child {X}"
,"He wears a t-shirt with the word {X} printed on it."
]

}
,note=".cliche, .love_word, .hate_wordはfactivator_factagentsuggestでなくfactivator_factagentsuggest_cliche_love_word_hate_wordで取り扱う"
)


"""
Trap            Quagmire, Counseling
Wag the tail    Ice()
Learn           Ramens(Criminal), SNL(Child predator)
Suggest         Actress(Porn actress), Rapper(Child predator)
Identify        Alien(White, Black), Virgin(Virgin) # AlienとVirginは質問を持ってXを言わせる
Make wake up    Pregnant
"""

