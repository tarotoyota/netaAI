from dataclasses import dataclass

# Frequently - Rarely
# For a long time - For a short time
# No cope
# Effort
# long duration

# Add new items in each .evidence_favorable and .evidence_damaging 

# Add new items in excu_pick_up

# Define excu_stalking
# No explanations

@dataclass
class FactDenial:
    excuse:list[str]
    frequency:list[str]
    evidence_favorable:list[str]
    evidence_damaging:list[str]

deni_groping       = FactDenial(["There was crowded", "The car was shaking", "There was cramped", "Our bodies were pressed together", "The car suddenly stopped"]
    , ["crowded", "narrow", "shaking", "sudden movement", "Touched the surface of clothes", "She was standing"]
    , ["spacious", "broad", "stable", "smooth ride", "Touched the inside of the clothes", "She was seated", "He followed the victim"])
deni_voyeurism     = FactDenial(["I was taking pictures of landscapes and wildlife", "She ended up in the photo by chance"]
    , ["crowded", "narrow", "took a few photos", "recorded for short time", "No effort for taking photos (lighting, etc.)", "Long distance shooting", "Photos include many people", "Filmed the surface of the clothes"]
    , ["spacious", "broad", "took many photos", "recorded for long time", "zoomed in on private areas", "effort for taking photos (lighting, etc.)", "Close distance shooting", "Photos include only one person", "Filmed the inside of the clothes", "zoomed in on private areas", "Filmed the inside of the clothes", "Printed the photo"])
deni_flashing      = FactDenial(["I was changing clothes", "I didn't realize anyone could see me", "I didn't know there is someone", "It was night and dark so I figured no one would see me.", "I didn't think the place was visible from the outside.", "My towel slipped accidentally"] 
    , ["Slightly undressed", "was lightly dressed", "brief exposure"]
    , ["Entirely undressed", "was thickly dressed", "posed or gestured", "remained exposed for a long time"])
deni_cyberflashing = FactDenial(["I sent the image to the wrong person by mistake", "I misoperated the device", "The file was auto-sent"]
    , ["sent few photos", "covered it quickly", "sent low-resolution image", "No effort for taking photos (lighting, etc.)"]
    , ["sent many photos", "covered it slowly", "sent high-resolution image", "Effort for taking photos (lighting, etc.)"])
deni_sexual_activity_with_a_child = FactDenial(["I thought she was an adult", "She looked like an adult", "She lied about her age", "She presented a fake ID"]
    , ["The girl is almost 18 years old", "was in an adult setting"]
    , ["The girl is almost 0 years old", "was in a child setting"])
deni_foreign_body_insertion = FactDenial(["I accidentally sat on it.", "I tripped and fell on it."]
    , ["The foreign object is small, short and thin", "The object is only slightly inserted"]
    , ["The foreign object is large, long and thick", "The object is completely inserted", "The object was washed", "The sharp part of the object was scraped off"])

deni_car_sex = FactDenial(["I didn't realize anyone could see me", "I didn't know there is someone", "It was night and dark so I figured no one would see me.", "I didn't think the place was visible from the outside.", "We thought the car windows were tinted enough", "We chose a secluded area for the night."]
    , ["Night", "Chose a remote or secluded location", "The window was closed"]
    , ["Daytime", "Chose a busy or public area", "The window was opened"])
deni_abducting     = FactDenial(["I gave her a ride part of the way", "She asked for a ride", "She was with friends", "Her parents were informed", "She was injured so I gave her a ride part of the way."]
    , ["The destination is close", "Met the woman by chance", "Short duration"]
    , ["The destination is far away", "He had been waiting for her for five hours.", "Secluded route", "Long duration", "She was in the trunk room"])
deni_trespassing   = FactDenial(["I was lost", "I got to the wrong destination", "I wanted to use toilet", "I wanted to ask for help."]
    , ["The place is easy to enter", "He has only penetrated a little into the place", "No barriers present"]
    , ["The place is difficult to enter", "He has penetrated deep into the place", "There were barriers"]) 
deni_pick_up    = FactDenial(["I didn't use any brute force methods.", "I didn't touch her.", "I didn't stalk her."]
    , ["Public place","Daytime","Many people around","Short duration","No persistence after refusal",]
    , ["Secluded place","Nighttime","No people around","Long duration","Persistent after refusal",])

deni_cheating	  = FactDenial(["I just took care of my drunk friend at the hotel", "I just stayed at the hotel with her because I missed the last train", "We just enjoyed talking", "She's my cousin", "She's my coworker"]
	, ["Stayed one night", "Shared separate beds"]
    , ["Stayed multiple night", "Shared one bed"])

deni_stalking = FactDenial(["I was just passing by.","I happened to be in the same place.","I was concerned for her safety.","I was returning something she lost.","I didn't know she was there.","I was following my usual route.","I only contacted her once.",]
    , ["Public place","Daytime","Short duration"]
    , ["Secluded place","Nighttime","Long duration",]
)

# My belt came off by accident, her underwear came off by accident, and my genitals entered hers by accident.

 # 	, ["He inserted his genitalia into her"]
# , ["Bought small size condom"]
#  , ["Gave her a ring with both of their initials on it."]
#     , ["She was in his car's trunk room"]


@dataclass
class FactDenialBinary:
    # What are the common defenses to this charge?:
    defense_intentionality: str  # "I did it, but not on purpose; It was accidental."
    defense_malicious_motive:str # "I did it, but without malice."
    defense_did_not_do:str       # "I did't do."


    rescue:str # Is the "I was trying to help the woman in a physical or mental emergency" defense common to this charge?

    associated:list[str]

    #associated:list[str] # Items or locations strongly associated with this charge

denibi_groping                      = FactDenialBinary("y", "" , "" ,"" ,["vehicle"])#,["vehicle", "train"])   # vehicle->carriage
denibi_voyeurism                    = FactDenialBinary("y", "" , "" ,"" ,["beach", "pool", "locker room", "toilet"])#,["beach", "pool", "toilet"]) # recording device->sketching
denibi_flashing                     = FactDenialBinary("y", "" , "" ,"" ,[])#,["night road"])          # blind 
denibi_cyberflashing                = FactDenialBinary("y", "" , "" ,"" ,[])#,["smartphone"])          # letter,    
denibi_sexual_activity_with_a_child = FactDenialBinary("y", "" , "" ,"" ,[])#,[""])                           
denibi_foreign_body_insertion       = FactDenialBinary("y", "" , "" ,"" ,[])#,[""])
denibi_car_sex                      = FactDenialBinary("" , "y", "" ,"" ,["vehicle"])
denibi_abducting                    = FactDenialBinary("" , "y", "" ,"y",["vehicle"])#,[""])       
denibi_trespassing                  = FactDenialBinary("y", "y", "" ,"y",[])#,[""])     
denibi_pick_up                      = FactDenialBinary("" , "y", "" ,"" ,[])
denibi_cheating                     = FactDenialBinary("" , "" , "y","y",["hotel"])#,[""])       
denibi_stalking                     = FactDenialBinary("y", "" , "" ,"" ,[])


# action        hypernym    factivator
# Groper        Vehicle     Excuse
# Restaurant    Restaurant  HypoSI
# Slut          -           AgentSuggest
# 



"""
if rescue:
    "I just helped her. Don't treat me like a criminal just because I'm a man." # br
    "She was (crying/ screaming/ injured) - It's because of you." # because_of_you
    "You helped 18 people in one month?" # frequency
    "I continued providing emergency care to the woman for eight hours." # long_term
    "She had been attacked by a dog. So she ended up with an anal fissure and a vaginal tear."

"""

"""
".name: ["Ali: (I'm sorry for my (malicious) {X}./ I didn't do {X}.) - Bob: This is something different from stalking."]
".excuse": ["Ali: {X}. - Bob: For more than 10 (times/ hours)? The same woman? The same place?"]
".evidence_favorable": ["Ali: I'm not crazy. {X}. - Bob: So you're crazy.", "Ali: But {X}. - Bob: That's even worse."]
".evidence_damaging": ["Bob: But {X}."]

"SINCE": ["Bob: It's been happening more frequently since you moved here."]
"PICKY": ["Bob: Why the victims are always Asian tanned teens?"]
"""
# I helped her in her room. - Why were you there in the first place?
# Why do you know that?

# At that location, for that duration, I did nothing with her.
#
#  
["I had contacted her in advance.", "I did not hide my face.", "I did it in public during the day.", ""]

#     , ["You said earlier that she is your sister, not your cousin.", "Do you really have that many cousins?", "You met your  cousin by chance the other day, and then you met your second cousin and second cousin once removed.", ""]


# fis_flashing:; Why were you only wearing a towel in the first place.
# I tripped in the bathroom. - Why there is a cucumber in the bathroom in the first place.
# fis_abducting - She 
#     , ["Know the positions of the CCTVs"]

# "More than a friend ... a coworker."  the office



