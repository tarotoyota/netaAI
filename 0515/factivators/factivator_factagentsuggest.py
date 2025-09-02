from factivators.class_factivatortable import FactivatorTable

factivator_factagentsuggest=FactivatorTable("factivators_factagentsuggest"
,[["", "", ""]]
,{
 "spot_love"    :[
 "Ali knows where {X} is"
,"Ali knows when {X} is (busy/ empty)"
,"Ali knows when {X} is (closed/ opened)"
,"Ali knows the users and employees of {X}"
,"Ali knows the discount system of {X}"
,"Ali knows how to use {X}"
,"Ali knows the layout of {X}"
,"Ali knows the rules and regulations of {X}"
,"Ali knows the nearest public transport to {X}"
,"Ali knows the contact information for {X}"
,"There are eyewitness accounts of Ali being seen at {X}."
,"Ali's lost property was found at {X}."
,"Ali knows the restroom locations in {X}."
]
,"spot_hate"    :[
 "They threat Ali that they will take him to {X}"
] #
,"spot_expr"    :[
 "Ali was banned from {X}"
]
,"love_time"    :[
 "Ali sets his timer to that time"
,"Ali can feel when the time has come"
,"Ali marks it on my calendar"
,"Ali knows when the time will come"
,"Ali counts down the days to that time"
,"Ali checks the clock frequently as it approaches"
,"Ali prepares special meals for that time"
,"Ali celebrates milestones occurring at that time"
]
,"hate_time"    :[
 "We can do that during {X}"
,""
]
,"love_tool"    :[# [print(f"Sitcom Scene. X = "stun gun" Ali lives an unsafe city, so {i}." for i in freq_tool]
 "Ali carries around {X}"
,"Ali knows the average price of {X}"
,"Ali knows the useful life of {X}"
,"Ali has the favorite {X}"
,"Ali has many {X}"
,"Ali can compare {X}"
,"Ali purchases {X} regularly"
,"Ali lost {X}"
,"Ali understands how to maintain {X}"
,"Ali can identify different brands of {X}"
,"Ali can recommend the best type of {X}"
,"Ali knows the safety precautions for {X}"
,"Ali can troubleshoot issues with {X}"
,"Ali knows the specifications of {X}"
,"Ali can demonstrate how to use {X}"
,"Ali categorizes {X} as a consumable item"
,"Ali keeps a spare {X}"
,"Ali can repair {X}"
,"Ali can identify counterfeit versions of {X}."
]
,"hate_tool"    :[] # rape victims buy rape alerts. I hate {X}. I was troubled because of {X}.
,"love_word"    :["REFER TO 'factivator_factagentsuggest_cliche_love_word_hate_word'"]
,"hate_word"    :["REFER TO 'factivator_factagentsuggest_cliche_love_word_hate_word'"]

,"love_sign"    :[]
,"hate_sign"    :[]
,"love_sound"   :[
 "Ali's ringtone is {X}"
,"Ali likes listening to recordings of {X}"
,"Ali uses {X} as ASMR"
,"Ali can play {X} on an instrument"
,"Ali wakes up when he hears {X}"
,"Ali plays {X} in his car"
,"Ali falls asleep to the sound of {X}"
,"Ali recognizes {X} from a distance"

,"Ali's ringtone for close friends is {X}."
,"Ali, who is unable to wake up from her sleep, jumps up when someone makes her hear the sound of {X}."
]
,"hate_sound"   :[
 "Ali is tortured into hearing the sound of {X}."
,"Ali wakes up when he hears {X}"
,"Like the mosquito sound, {X} is used to scare Ali away."
]
,"hobby"        :[]
,"acv_grasp"        :[]
,"acv_cliche":["REFER TO 'factivator_factagentsuggest_cliche_love_word_hate_word'"]

,"rephrase"     :["Ali uses (A) as (B)", "Ali cals (A) (B)", "Ali compares (A) to (B)", "Ali doesn't need (A) because he can access to (B)"]
}
,note=".cliche, .love_word, .hate_wordはfactivator_factagentsuggestでなくfactivator_factagentsuggest_cliche_love_word_hate_wordで取り扱う"
)