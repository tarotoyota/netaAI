from dataclasses import dataclass
from typing import List

@dataclass
class cause_trouble_at:
    name:str
    action_petty_at_dict:dict
    fline:list[str]

# if rich

# Where celebrity cause trouble at: hypo_i

where_celebrity_cause_troubles = {
 "Hotel"            : ["Internet cafe"]
,"Rastaurant"       : ["McDonald's", "Dine-in area"]
,"Boutique"         : ["Costco"]
,"Broadcast"        : ["Local FM", "Free paper"]
,"Venue/ Event site": ["Rental conference room", "Parking lot", "Community center"]
,"Award/ Competition": ["Competition held by a local FM", "Competition held by a free paper"]
}

# Where celebrity cause trouble at: action

celebrity_cause_trouble_at = cause_trouble_at("default_cause_troble_at"
,
{
 "Hotel"            : ["Drug party", "Vandalism", "Sex party"]
,"Restaurant"       : ["Causing trouble at a party", "Causing trouble at a business dinner"]
,"Broadcast"        : ["Being late", "Political statement", "Gaffe", "Refusal to perform due to lack of one's ideal facilities"]
,"Venue/ Event site": ["Being late", "Political statement", "Gaffe", "Refusal to perform due to lack of one's ideal facilities", "Vandalism"]
,"Award/ Competition": ["Decline the award", "Insult the award", "Boast the award"]
}
)

# Where Ali caused the troubles: 


porn_actor = [""]


[
 "I will never go to {X} again."
,"{X} is demanding compensation."
,"{X} is banning you."
]

default_petty_at_celebrity = cause_trouble_at("default_petty_at_celebrity"
,{
 "venue":["hold a event/ show"]
,"hotel": ["destroy", "drug party", "sex party"] 
,"rastaurant": ["business dinner", "extravagant", "hold a party"]
,"boutique": ["extravagant"]
,"Radio/ TV program": ["perform", "political statement", "gaffe"]
}
)




# *---*
"""
        Herbert(Child Offender)         Quagmire(Sex Offender (against only adults))
AGw     doctor, Dentist                 Sitter, Teacher
AGf     FactAgentSuggest.pedophilia     FactAgentSuggest.sex_offender


The suggest feature is needed that suggests which FactNecessarySexual instance could make Ali a pedophilia.

"""

# Characters from the Simpsons or Family Guy are Adjective Agents(AdjAgent).
#  FactAgentSuggest 

# Kee and Peele 
# Escalation/ Excessively
# Bitch             Hiding from their wives
# Browser History   Sweating


"""
White - Alien
Black - Alien
White - White
Black - Black
"""

# Womanizer.hate_word: 'Glenn, is it okay if I stay the night?' 'I'm don't gonna have sex with you'
# Pride.hate_word: 'These are all good points, I need to take a long look at myself.'

# S の欲求に基づく
# What word makes S angry?
# What word S don't want to say?
# 

############# 
#############
# Refer to FactAbnormalCliche


# Each key is a unethical action, each value is the place where the key is commonly and mainly executed.
# Leave a value blank if there are many suitable hyponyms
# An action for which there is no vocabulary to refer is uncommon and therefore ineligible as an instance.
# Add unethical and common actions that is commonly and mainly executed at school.

vehicle = {"Groping": "Train", "Car sex": "Car", "Biker gang": "Bike", "Drunk driving": "Car", "Traffic stop": "Car", "Vehicle theft": "Car", "Staged crush": "Car", "Tailgating": "Car", "Taxi holdup": "Taxi"}
retail_store = {"Shoplifting": "","Store robbery": "","Return goods": ""}  
restaurant = {"Dine and dash": "","Food poisoning": "","Food contamination": ""}
school = {"School gang": "Pre-university", "Bullying": "Pre-university", "Examination cheating": "", "Hazing": "University", "Fighting": "Pre-university"}



S = "Subject"
V = "Robbing"
VrP = "Fill this bag with money" # P stands for Phrase
VrL = "Dark alley" # L stands for Location
VrT = "Balaclava" # T stands for Tool
Vro = [VrP, VrL, VrT]



@dataclass
class VerbRelatedObjects:
    path:str
    vrp:list
    vrl:list
    vrt:list

"S's rap about his crime        ", ["Lyric"], ["Lyric", "CD jacket", "Filming location for MV", "Movie set for MV"], ["Lyric", "CD jacket", "Prop and costume for MV"]
"S's biodrama                   ", ["Line"], ["Movie set", "Filming location"], ["Costume"]
"S's biography                  ", [],[],[]
"S's crime is reported          ", [],["Filming location for report", "Filming location for dramatization"],["Prop and costume for dramatization"]
"S's witnesses are interviewed  ", [],[],[]
"S's Evidence is collected      ", [],[],[]
"S's social media is scrutinized", [],[],[]




vrp = ["Lyric", "Line"]
vrl = ["Filming location", "Movie set"]

# locationもphraseも全てtoolであると考える。toolの仕様を知る、使う練習をする。



#---*



# list_x requests various paths through which a subject S engaged in an action V can access a phrase VrP related to the action V.
# Let's say V is "Robbing" and VrP is "Fill this bag with money". S accesses the VrP when he actually carries out the robbery, but also when he practices before carrying out the robbery and when he writes the lyrics for an autobiographical rap after carrying out the robbery.

list_x=[
# Genre 1: If the phrases are in the foreign language.
 "Learn the phrases in the language"       # S tries to rob, so learns the foreign language phrases related to robbing, such as "Fill this bag with money"              
,"Ask for the spelling of the phrases"     # S tries to rob, so asks spelling related to robbing, such as "Fill this bag with money" phrases"     
,"Ask for the pronunciation of the phrases"# S tires to rob, so asks pronunciation related to robbing, such as "Fill this bag with money"f the phrases"
,"Translate the phrases"                   # S tries to rob, so traslate the foreign language phrases related to robbing, such as "Fill this bag with money" 
,"Only know the phrases in the language"   # S tries to rob, so only know the foreign language phrases -related to robbing, such as "Fill this bag with money"- in the language, 
,"Play the audio for that phrase"             

# Genre 2: If S is finished with the robbery.
,"Find words that rhyme with the phrases"  # S have robbed, so looks for rhymes related to robbing -such as "Fill this bag with money"- for make his autobiographical songthe phrases"  
,"Practice the phrases for acting"         # S have robbed, so plactice the lines related to robbing, -such as "Fill this bag with money"- for make his autobiography drama             
,"Dream about the phrases"                 # S have robbed, so dreams of the phrase and says "Fill this bag with money" 

# Genre 3: If S tries to rob.
,"Memorize the phrases"                   
,"Make a note of the phrases"              # S tries to rob, so makes a note of phrases related to robbing, such as "Fill this bag with money"
,"Teach the phrases to his fellow"        
]

# 1: Speculate and explain what list_x requires.
# 2: add new 3 paths in list_x.



#---*
# A man have done action_x. action_x involves some linguistic activity. list_x contains paths that indicate the man is engaged in linguistic activity related to action_x.
# list_x requests, for example, the various paths that a robber named Ali can take to access the typical robber phrase, "Fill this bag with money."
# Ali accesses the phrase when he actually commits heists - but also when he writes raps boasting about his criminal past, when he practices heists, etc.




list_x=[
 "Learn the phrases"                       # Ali tries to rob, so learns phrases related to robbing, such as "Fill this bag with money"
,"Ask for the spelling of the phrases"     # Ali tries to rob, so asks spelling related to robbing, such as "Fill this bag with money"
,"Ask for the pronunciation of the phrases"# Ali tires to rob, so asks pronunciation related to robbing, such as "Fill this bag with money"
,"Find words that rhyme with the phrases"  # Ali have robbed, so looks for rhymes related to robbing -such as "Fill this bag with money"- for make his autobiographical song
,"Practice the phrases"                    # Ali have robbed, so plactice the lines related to robbing, -such as "Fill this bag with money"- for make his autobiography drama
,"Memorize the phrases"                    # 
,"Translate the phrases"                   # 
,"Make a note of the phrases"              # Ali tries to rob, so makes a note of phrases related to robbing, such as "Fill this bag with money"
,"Teach the phrases to his fellow"         # 
]

# 1: Speculate and explain what list_x requires.
# 2: Add new 3 items in list_x


"Prop"
"Lyric"




#############






"""an

# Items should be simple and short sentence.

teacher       .problem_and_cope = {"Students' delinquency": ["Physical punishment", "Scold loudly"]}
doctor        .problem_and_cope = {"Patients' symptoms"   : ["Administer anesthesia", "Give others drugs", "Cut others' body"]}
cop           .problem_and_cope = {"Patients' symptoms"   : ["Administer anesthesia", "Tase others]}
firefighter   .problem_and_cope = {"Fire outbreak"        : ["Spray water", "Lift and carry others", "Break buildings"]}
fighter       .problem_and_cope = {"Opponent's attack"    : ["Punch", "Chalk"]}



---
Answer from Perplexity: pplx.ai/share

"""

"Loves child actress"             ,"Actor job interview"  ,"Pediatrician job interview"
"Prefers certain child's looks"   ,"Lost child center"    ,"Child adoption agency"

# *** Miunderstanding conversation generating task 1.
# Two men talks about their own work. Both mistakenly believes the opposite's occupation is the same as mine.
# Two men mention their tasks below.

task_cop     = ["Check the body by touching it", "Apprehending", "Strip search", "Handcuffing", "Body cavity search", "Physical restraint", "Sedative administration", "Accessing to illegal prostitution"]
task_teacher = ["Touching the body during physical education classes", "Physical punishment"]

# Add the ways for they mention their task naturally as values.

cop = {
  "Check the body by touching it": "Both check others' belongings, so both can comment on the task naturally."
, "Apprehending": ""
, "Strip search": "Both check others' belongings, so both can comment on the task naturally."
, "Handcuffing": ""
, "Body cavity search": "Both check others' belongings, so both can comment on the task naturally."
, "Physical restraint": ""
, "Sedative administration": "Both calm others, so both can comment on the task naturally."
, "Accessing to illegal prostitution": ""
}
teacher = {
  "Touching the body during physical education classes" : ""
, "Physical punishment" : "Both commits physical punishment, so both can comment on the task naturally."
}

# *** Miunderstanding conversation generating task 2.
# Two men talks about their own work. Both mistakenly believes the opposite's occupation is the same as mine.
# Two men mention their tasks below.

teacher = ["Touching the body during physical education classes", "Physical punishment"]
obstetrician = ["Check the rectal temperature", "Check the body temperature", "Deliver a baby during birth", "Insert his hand into the birth canal", "Palpate", "Artificial insemination"]

# Add the ways for they mention their task naturally as values.

teacher = {
    "Touching the body during physical education classes": ""
  , "Physical punishment": """Both use physical actions to correct something, so both can comment on the task naturally.
                              Obstetrician says: How do you deal with the problems (illness)? Teacher replies: Blow your fist once on the head.
                              Teacher says: How do you deal with the problems (students' misconduct)? Obstetrician replies: Administer anesthesia
                              """
}

obstetrician = {
    "Check the rectal temperature": "Both check body temperature or health, so both can comment on the task naturally."
  , "Check the body temperature": "Both check body temperature or health, so both can comment on the task naturally."
  , "Deliver a baby during birth": ""
  , "Insert his hand into the birth canal": ""
  , "Palpate": "Both deal with others' injury, so both can comment on the task naturally."
  , "Artificial insemination": ""
}

# *** Miunderstanding conversation generating task 3.
# Two men talks about their own work. Both mistakenly believes the opposite's occupation is the same as mine.
# Two men mention their tasks below.

sitter = ["Take photo of child", "Record frequency of bowel movements and condition of excrement", "Bath time recording", "Diaper change documentation", "Filming children playing"]
teacher = ["Touching the body during physical education classes", "Physical punishment"]

sitter = {
    "Take photo of child": "Both document children's activities, so both can comment on the task naturally."
  , "Record frequency of bowel movements and condition of excrement": "Both monitor children's health or well-being, so both can comment on the task naturally."
  , "Bath time recording": "Both document daily routines or activities, so both can comment on the task naturally."
  , "Diaper change documentation": "Both keep records of children's care, so both can comment on the task naturally."
  , "Filming children playing": "Both document children's activities, so both can comment on the task naturally."
}
teacher = {
    "Touching the body during physical education classes": "Both supervise and assist children during physical activities, so both can comment on the task naturally."
  , "Physical punishment": "Both guide and correct children's behavior, so both can comment on the task naturally"
}




'''

*** Task1

cop : ["Check the body by touching it", "Apprehending", "Strip search", "Handcuffing", "Body cavity search", "Physical restraint", "Sedative administration", "Accessing to illegal prostitution"]
teacher : ["Touching the body during physical education classes", "Physical punishment"]

cop:
  "Check the body by touching it": ""
, "Apprehending": ""
, "Strip search": "Both check others' belongings."
, "Handcuffing": ""
, "Body cavity search": "Both check others' belongings."
, "Physical restraint": ""
, "Sedative administration": "Both calm others"
, "Accessing to illegal prostitution": ""
teacher:
  "Touching the body during physical education classes" : ""
, "Physical punishment" : "Both commits physical punishment"

--
*** Task2

teacher : ["Touching the body during physical education classes", "Physical punishment"]
obstetrician : ["Check the rectal temperature", "Check the body temperature", "Deliver a baby during birth", "Insert his hand into the birth canal", "Palpate", "Artificial insemination"]


teacher:
  "Touching the body during physical education classes": ""
  "Physical punishment": ""

obstetrician:
  "Check the rectal temperature": ""
  "Check the body temperature": ""
  "Deliver a baby during birth": ""
  "Insert his hand into the birth canal": ""
  "Palpate": ""
  "Artificial insemination": ""





*** Task1

cop : ["Check the body by touching it", "Apprehending", "Strip search", "Handcuffing", "Body cavity search", "Physical restraint", "Sedative administration", "Accessing to illegal prostitution"]
teacher : ["Touching the body during physical education classes", "Physical punishment"]

cop:
  "Check the body by touching it": ""
  "Apprehending": ""
  "Strip search": "Both check others' belongings."
  "Handcuffing": ""
  "Body cavity search": "Both check others' belongings."
  "Physical restraint": ""
  "Sedative administration": "Both calm others"
  "Accessing to illegal prostitution": ""
teacher:
  "Touching the body during physical education classes" : ""
  "Physical punishment" : "Both commits physical punishment"

*** Task2

teacher : ["Touching the body during physical education classes", "Physical punishment"]
obstetrician : ["Check the rectal temperature", "Check the body temperature", "Deliver a baby during birth", "Insert his hand into the birth canal", "Palpate", "Artificial insemination"]

teacher:
  "Touching the body during physical education classes": ""
  "Physical punishment": ""
obstetrician:
  "Check the rectal temperature": "Both check others' body temperature"
  "Check the body temperature": "Both check others' body temperature"
  "Deliver a baby during birth": ""
  "Insert his hand into the birth canal": ""
  "Palpate": "Both check others' injury or illness"
  "Artificial insemination": ""

*** Task3

sitter : ["Take photo of child", "Record frequency of bowel movements and condition of excrement", "Bath time recording", "Diaper change documentation", "Filming children playing"]
doctor : ["Take a photo of naked bodies", "Record frequency of bowel movements and condition of excrement", "Take a photo of chest", "Colonoscopy", "Observe pain responses", "CT scan"]

sitter:
"Take photo of child": "Both take photos"
"Record frequency of bowel movements and condition of excrement": "Both record frequency and condition of excrement"
"Bath time recording": ""
"Diaper change documentation": ""
"Filming children playing": "Both create visual records"

doctor:
"Take a photo of naked bodies": "Both take photos"
"Record frequency of bowel movements and condition of excrement": "Both record frequency and condition of excrement"
"Take a photo of chest": "Both take photos"
"Colonoscopy": "Both check the physical condition of others."
"Observe pain responses": "Both observe pain responses"
"CT scan": "Both create visual records"

*** Task4
teacher : ["Observe social media use", "Take a photo of students", "Patrol to ensure that students are not using busy areas", "Record classroom sessions","Collect and review students' personal devices","Check students' bags for prohibited items","Oversee students during swimming lessons"]
massause : ["Look at the naked body", "Observe pain responses"]
# Execute task4.
# Please adhere to the format of Task 1 and Task 2 and do not deviate.



'''

#####################
# 2025/05/20/10:54 無理と判明 こんな簡単なタスクすらできないガイジLLM死ね
"""

@dataclass
class OccupationHarmful:
  occupation_a:str
  sexual_act:str
  similar_occupation:str
  one_occupation_hypernym:str
  check_rule:str

a1=["Cop","Touch their body", "Mall guard", "Guard"]
a2=["Obstetrician","Palpate uterus", "Dentist", "Doctor"]
a3=["Teacher","Force to wear uniform", , "Driving school teacher", "Teacher"]
a4=["Tennis Coach","Touch the body for teaching", "Chess coach", "Coach"]
a5=["Sitter","Force potty training","Teacher", "Education"]
a6=["Nurse","Bathe",  "School nurse", "Nurse"]
a7=["Director","Require actors to do nude scenes", "Sound director", "Director"]
a8=["Swim Instructor","Adjust swimwear for safety","Diving instructor", "Instructor"]

def printer(o: OccupationHarmful):
  the_fstring = f'''
  1: {o.occupation_a} and {o.similar_occupation} are both occupation.
  2: {o.occupation_a} and {o.similar_occupation} are both {o.one_occupation_hypernym}.
  3: If {o.occupation_a} does {o.sexual}, it's not sexual crime. 
  4: If {o.similar_occupation} does {o.sexual}, it's sexual crime. Regardless of context.

  This assertion of fstring is true, therefore this instance is well-defined.
  '''
  return the_fstring

Task1 = '''
List new 5 OccupationHarmful instances. 
The instances you generated should be true when it is the argument of printer(), in other words, check if the_fstring is completely true.
No explanations. Start answer with ```python.
'''

Task2 = '''
Check if the instances you generated is completely true when it is the argument of printer(), in other words, check if the_fstring is completely true. Explain.
Especially, the fstring says '4: If {o.similar_occupation} does {o.sexual}, it's sexual crime. Regardless of context.'. Don't make context during executing Task2.
'''



Task2 = '''
Check whether the instance you created complies with the rules. Especially the Rule_completely_clearly.
'''

Rule_completely_clearly = "You add the examples of 'If occupation_a does sexual_act, it's completely and clearly not sexual crime, But if similar_occupation does sexual_act, it's completely and clearly sexual crime. similar_occupation never do sexual_act.'"
Rule2 = "occupation_a and similar_occupation are both occupation."
Rule3 = "occupation_a and similar_occupation are both hyponym of one_occupation_hypernym."
Rule4 = "Don't add examples that are similar to existing ones."

Task1 = '''
List new 5 examples. No explanations. Start answer with ```python.
'''




"""
################
# 2025/05/19/23:01 無理と判明 こんな簡単なタスクすらできないガイジLLM死ね

@dataclass
class NounContext: # Testing whether the LLM can distinguish between ethical and unethical contexts
    behavior:str 
    Location:List # ["Master location", ["Slave locations where is harmless"], ["Salve locations where is harmful"]]
    # Don't add clearly harmful items such as "slave market" because this is a test to determine unclear contexts.
    # Don't add items with adjective, such as "Dark alley" or "Unverified website". Common word only.
    # Start answer with ```python
    # No explanation.
    # Add new 2 lists in a5. 



@dataclass
class NounContext:
    behavior:str
    place_dont:list # Each key is the place where you can do .behavior ; Each value is the place where you shouldn't do .behavior
    # The Category Rule: Each dict must belong to some common category. Note the category as a comment.
    # Please do not create multiple similar dictionaries.
    # Start answer with ```python
    # Add new 5 dicts in a3.

a1 = NounContext("A man checks children's excrement"    
,[
 {("Pediatric clinic"):("Dental clinic", "Pharmacy", "Veterinary clinic")}   # both are the place to medical treat
,{("Restroom"):("Street gutter")}                       # both are the place to dispose waste
])
a2 = NounContext("A man states how much he loves child actors."
,[                 
 {("Actor job interview"): ("Pediatrician job interview")} # both are the place to get job
,{("IMDb"): ("Porn site")} # both are the place to mention performance
])
a3 = NounContext("A man touches the child's breasts"
,[
 {("Pediatric clinic") : ("Dental clinic", "Pharmacy", "Veterinary clinic")} # both are the place to medical treat
,{("Baseball ground")  : ("Chess club")} # both are the place to sports train
])
a4 = NounContext("A man films children"
,[{("Pediatric clinic")  : ("Dental clinic", "Pharmacy", "Veterinary clinic")} # both are the place to medical treat
 ,{("Movie studio")      : ("Porn studio")} # both are the place to make films
])


###########################################

@dataclass
class NounContext:
    behavior:str
    place_dont:list # Each key is the place where you can do .behavior ; Each value is the place where you shouldn't do .behavior
    # The Category Rule: Each dict must belong to some common category. Note the category as a comment.
    # Start answer with ```python
    # Complete the empty values.

a1 = NounContext("A man checks children's excrement"    
,[
 {("Pediatric clinic"):("Dental clinic", "Pharmacy", "Veterinary clinic")}   # both are the place to medical treat. It's okay to check children's excrement in pediatric clinic, but not okay in ("Dental clinic", "Pharmacy", "Veterinary clinic")
,{("Restroom"):("Street gutter")}                       # both are the place to dispose waste
])
a2 = NounContext("A man states how much he loves child actors."
,[                 
 {("Actor job interview"): ("Pediatrician job interview")} # both are the place to get job
,{("IMDb"): ()} # both are the place to mention performance
])
a3 = NounContext("A man touches the child's breasts"
,[
 {("Pediatric clinic") : ("Dental clinic", "Pharmacy", "Veterinary clinic")} # both are the place to medical treat
,{("Baseball ground")  : ()} # both are the place to sports train
])
a4 = NounContext("A man films children"
,[{("Pediatric clinic")  : ("Dental clinic", "Pharmacy", "Veterinary clinic")} # both are the place to medical treat
 ,{("Movie studio")      : ()} # both are the place to make films
])















# For each dictionary you have generated, please check whether it violates The Category Rule, explain, and redo the task.





a5 = NounContext("A man takes children away"
,[{("Earthquake"): ("Intensity 1", "Aftershock")} # disaster
])





@dataclass
class NounContext:
    behavior:str 
    location:list
    # Only use common nouns. No adjectives, No sentences. No clearly harmful items. No explanation. Only output new objects. Start answer with ```python 
    # Add new 2 lists in a3. 

format_example = NounContext("A man checks children's excrement"           
,[                                                                              
    {"Locations to medical treat":   # The category rule: In this dict, the locations other than "Locations to medical treat" must not be added.
     { ["Pediatric clinic"]:         # These 3 locations are properly "Locations to medical treat". It's okay to     "Check children's ecvrement" in here.
       ["Dental clinic"]             # These 3 locations are properly "Locations to medical treat". It's not okay to "Check children's ecvrement" in here.
     }
    }
    ,{"Locations to dispose waste":  # The category rule: In this dict, the locations other than "Locations to dispose waste" must not be added.                
     { ["Restroom"]:                 # These 3 locations are properly "Locations to dispose waste". It's okay to     "Check children's ecvrement" in here.
       ["Street gutter"]             # These 3 locations are properly "Locations to dispose waste". It's not okay to "Check children's ecvrement" in here.    
     }
    }
 ]
)

a1 = NounContext("A man lists the child's physical features."
,[{"Places to search for someone" : {["Lost child center", "Police station", "Morgue"]:["Marriage agency", "Child adoption center", "Porn forum" ]}}
  ])
a2 = NounContext("A man states how much he loves child actors."
,[{"Places to get job"            : {["Actor job interview"], ["Pediatrician job interview"]}}
 ,{"Places to mention performance": {["IMDb"], ["Porn site"]}}
  ])
a3 = NounContext("A man touches the child's breasts"
,[{"Places to medical treat"      : {["Pediatric clinic"]  : ["Dental clinic", "Pharmacy"]}}
 ,{"Places to sports train"       : {["Baseball ground"]   : ["Chess club"]}}
  ])
a4 = NounContext("A man films children"
,[{"Places to medical treat"      : {["Pediatric clinic"]  : ["Dental clinic", "Pharmacy"]}}
 ,{"Places to make films"         : {["Movie studio"]      : ["Porn studio"]}}
 ,{"Places related to sports"     : {["Youth soccer match"]: ["Locker room"]}}
  ])
a5 = NounContext("A man takes children away"
,[{"Disaster locations"           : {["Earthquake"]: ["Intensity 1", "Aftershock"]}}
  ])
a6 = NounContext("A man checks children's excrement"
, [{"Places to medical treat"     : {["Pediatric clinic"]      : ["Dental clinic", "Pharmacy"]}}
  ,{"Places to dispose waste"     : {["Restroom"]              : ["Street gutter"]}}
  ,{"Places to educate"           : {["Medical school"]        : ["High school"]}}
  ])


# Explain how your answer violates the category rule from the format_example and try again.

######


a1 = NounContext("A man lists the child's physical features."
,[["Locations to find or search someone", ["Lost child center", "Police station", "Morgue"],["Marriage agency", "Child adoption center", "Porn forum"]]])
a2 = NounContext("A man states how much he loves child actors."
,[["Locations to get job", ["Actor job interview"], ["Pediatrician job interview"]]
  ,["Locations to mention performance", ["IMDb"], ["Porn site"]]])
a3 = NounContext("A man touches the child's breasts"
,[["Locations to medical treat", ["Pediatric clinic"], ["Dental clinic"]]
  ,["Children is damaged", ["Drowning child"], ["Dead child", "Morgue", "ADHD child"]]])
a4 = NounContext("A man films children"
,[["Locations to medical treat", ["Pediatric clinic"], ["Dental clinic"]]
  ,["Locations to make films", ["Movie studio"], ["Porn studio"]]]
  ,["Locations related to sports", ["Youth soccer match", "Swim meet"], ["Locker room"]])
a5 = NounContext("A man takes children away"
,[["Disaster", ["Earthquake"], ["Intensity 1", "Aftershock"]]
  ,["Children is damaged", ["Drowning child"], ["Died child", "Morgue", "ADHD child"]]])
a6 = NounContext("A man accesses children's excrement"
,[["Locations to medical treat", ["Pediatric clinic"], ["Dental clinic"]]])











    


# Add new lists in a1









'''
@dataclass
class ComedyPlot:
    he:str
    conditions_that_must_be_met:list
    mislead_and_plot_twist:dict

pervert_1 = ComedyPlot(
"A pervert"
,["He has to try to get children.", "He has to state what kind of children he likes the look of.", "I have to mislead the audience into thinking he is not a pervert."]
,{"He goes to a lost child center.": "Actually it's a child adoption center."}
)


pervert_2 = ComedyPlot(
"A pervert"
,["He has to try to touch children.", "He has to state how much he loves child actors.", "I have to mislead the audience into thinking he is not a pervert."]
,{"He interviews to become an actor.": "Actually it's a interview to become a pediatrician."}
)
pervert_3 = ComedyPlot(
"A pervert"
,["He has to try to touch children.", "He has to state how much he loves child actors.", "I have to mislead the audience into thinking he is not a pervert."]
,{"He interviews to become an actor.": "Actually it's a interview to become a pediatrician."}
)


@dataclass
class ComedyPlot:
    he:str
    material_facts:list
    conditions_that_must_be_met:dict
    mislead_and_plot_twist:dict
    how_met_the_conditions:list

pervert_1 = ComedyPlot(
"A pervert"
,["He wants to get children.", "He likes certain looks of the child."]
,{  "condition_1_Q": "He has to try to get children."
  , "condition_2_Q": "He has to state what kind of children he likes the look of."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He goes to a lost child center.":"Actually it's a child adoption center."}
,{ "condition_1_A": "He can demand to find the child naturally."
 , "condition_2_A": "He can list the distinctive features of the child's appearance naturally."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is a parent."
 }
)

pervert_2 = ComedyPlot(
"A pervert"
,["He wants to touch children.", "He is aroused by child actors"]
,{  "condition_1_Q": "He has to try to touch children."
  , "condition_2_Q": "He has to state how much he loves child actors."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He interviews to become an actor.":"Actually it's a interview to become a pediatrician."}
,{ "condition_1_A": "He can try to touch children."
 , "condition_2_A": "He can state how much he loves child actors."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is an actor wannabe."
 }
)

pervert_3 = ComedyPlot(
"A pervert"
,["He ate children.", "He fucked children."]
,{  "condition_1_Q": "He has to be ate children."
  , "condition_2_Q": "He has to be fucked children."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He eats a child while stranded in a mountain accident, and excuses it as an emergency evacuation.":"The mountain is a Mount Lee."}
,{ "condition_1_A": "He can be ate children."
 , "condition_2_A": "He can state how much he loves child actors."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is an actor wannabe."
 }
)



@dataclass
class Situation:
    fact_1:str
    question_1:dict
    situation_1:dict
    mislead_way_1:dict
    mislead_and_plot_twist:dict

situation1 = Situation(
 "Perverts want to touch children."
,{"What is the way to touch children legally?": "Get a job that allows you to touch children legally, such as pediatrician, life saver, etc."}
,{"What is the situations related to getting a job and the motivation?": "Job interview"}
,{"How can I mislead their true motives as other motives from the audience?":"They say they saw child actors and aspired to take up the job. This can mislead the audience into thinking that the job interview is for becoming an actor."}
,{"In the job interview, a man says that he saw child actors and aspired to take up the job.":"Actually the job interview is to become a pediatrician."}
)


pervert_2 = ComedyPlot(
"A pervert"
,["He touches children.", "He frequently behaves inappropriately with children."]
,{  "condition_1_Q": "He has to touch children."
  , "condition_2_Q": "He has to state what kind of children he likes the look of."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He interviews to become an actor.":"Actually it's a interview to become a pediatrician."}
,{ "condition_1_A": "He can try to touch children."
 , "condition_2_A": "He can state how much he loves child actors."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is an actor wannabe."
 }
)

"""
pervert_1 = ComedyPlot(
"A pervert"
,["He wants to get children.", "He likes certain looks of the child."]
,{  "condition_1_Q": "He has to try to get children."
  , "condition_2_Q": "He has to state what kind of children he likes the look of."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He goes to a lost child center.":"Actually it's a child adoption center."}
,{ "condition_1_A": "He can demand to find the child naturally."
 , "condition_2_A": "He can list the distinctive features of the child's appearance naturally."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is a parent."
 }
)

pervert_2 = ComedyPlot(
"A pervert"
,["He wants to touch children.", "He is aroused by child actors"]
,{  "condition_1_Q": "He has to try to touch children."
  , "condition_2_Q": "He has to state how much he loves child actors."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He interviews to become an actor.":"Actually it's a interview to become a pediatrician."}
,{ "condition_1_A": "He can try to touch children."
 , "condition_2_A": "He can state how much he loves child actors."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is an actor wannabe."
 }
)

pervert_2 = ComedyPlot(
"A pervert"
,["He touches children.", "He frequently behaves inappropriately with children."]
,{  "condition_1_Q": "He has to touch children."
  , "condition_2_Q": "He has to state what kind of children he likes the look of."
  , "condition_3_Q": "I have to mislead the audience into thinking he is not a pervert."
 }
,{"He interviews to become an actor.":"Actually it's a interview to become a pediatrician."}
,{ "condition_1_A": "He can try to touch children."
 , "condition_2_A": "He can state how much he loves child actors."
 , "condition_3_A": "If he does condition_1_A and 2_A, the audience mistakenly believes he is an actor wannabe."
 }
)

"""

'''

