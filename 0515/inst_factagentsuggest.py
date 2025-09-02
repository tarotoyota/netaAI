from dataclasses import dataclass, field
from typing import List, ClassVar

@dataclass
class FactAgentSuggest:
    ALL_FACTAGENTSUGGEST: ClassVar[List['FactAgentSuggest']] = []
    INST_FactAgentSuggest:str

    love_spot :list= field(default_factory=list)
    hate_spot :list= field(default_factory=list)
    love_time :list= field(default_factory=list)
    hate_time :list= field(default_factory=list)
    love_tool :list= field(default_factory=list)
    hate_tool :list= field(default_factory=list)

    love_word :list= field(default_factory=list)
    hate_word :list= field(default_factory=list)
    love_sign :list= field(default_factory=list)
    hate_sign :list= field(default_factory=list)
    love_sound:list= field(default_factory=list)
    hate_sound:list= field(default_factory=list)

    hobby    :list= field(default_factory=list)
    grasp    :list= field(default_factory=list)
    media_on :list= field(default_factory=list)

    cliche     :list= field(default_factory=list)
    situation         :list= field(default_factory=list)
    def __post_init__(self):
        FactAgentSuggest.ALL_FACTAGENTSUGGEST.append(self)


sugg_criminal    =FactAgentSuggest("criminal"   )
sugg_rapist      =FactAgentSuggest("rapist"     )
sugg_pedophilia  =FactAgentSuggest("pedophilia" )
sugg_junkey      =FactAgentSuggest("junkey"     )
sugg_couple      =FactAgentSuggest("couple"     )
sugg_frail       =FactAgentSuggest("unhealthy"  )
sugg_old         =FactAgentSuggest("old"        )
sugg_ugly        =FactAgentSuggest("ugly"       )
sugg_fat         =FactAgentSuggest("fat"        )
sugg_illiteracy  =FactAgentSuggest("illiteracy" )
sugg_poor        =FactAgentSuggest("poor"       )
sugg_middle_aged =FactAgentSuggest("middle_aged")
sugg_play_girl   =FactAgentSuggest("play_girl"  )
sugg_womanizer   =FactAgentSuggest("womanizer"  )





########################################################################################################################################################################################################
# "school", "park", "kindergarten", "lost child center", "orphan", "hotel", "dumpyard", "station", "pickup spot", "high way", "brothel"
# - Select all designated locations for users to receive or get any living thing.
# -- Lost child center, Orphanage, Station (if it's a designated meeting point), Pickup spot

b_child  = ["school", "kindergarten", "park", "orphanage", "lost child center", "pediatric clinic", "school road"]
b_suitor = ["dating app", "pickup spot", "marriage agency", "speed dating event"]

########################################################################################################################################################################################################
sugg_criminal    .love_spot += ["Back alley", "Mexico", "State border", "CCTV blind spot", "Dark web", "Night road"]
sugg_rapist      .love_spot += [sugg_criminal.love_spot, "Toilet in shopping mall"]
sugg_pedophilia  .love_spot += [sugg_criminal.love_spot, b_child, "Public pool", "Toilet in shopping mall", "South-east asia"]
sugg_junkey      .love_spot += [sugg_criminal.love_spot, "Harm reduction facility", "Pharmacy", "Hospital"]

sugg_couple      .love_spot += ["nursing room", "delivery room", "bed room", "wedding venue"]
sugg_frail       .love_spot += ["mildly air-conditioned train car", "Escalator", "Massage clinic"]
sugg_old         .love_spot += [sugg_frail.love_spot, "Hospital waiting room", "Church", "碁会所"]
sugg_ugly        .love_spot += ["Cosmetic surgery clinic"]
sugg_fat         .love_spot += [sugg_frail.love_spot, sugg_ugly.love_spot, "Fast food restaurant", "Shadow"]
sugg_illiteracy  .love_spot += ["pub", "casino"]
sugg_poor        .love_spot += ["Shelter", "Food bank", "Community center", "Public park", "Pawn shop", "Discount store"]
sugg_middle_aged .love_spot += [sugg_frail.love_spot, "smoking area"]
sugg_play_girl        .love_spot += ["Pick-up spot", "smoking area", "Bar", "Night pool", "Hot-pillow hotel", "A pawn shop to cash in gifts they've received", "hotel room", "marriage agency", "dirts bar"]
sugg_womanizer   .love_spot += [sugg_play_girl.love_spot]


# Define poor.love_spot without any explanations. Align characters and spaces with existing instances.

# Add new items in frail.love_spot without any explanations. Align characters and spaces with existing instances.



sugg_criminal    .hate_spot += ["Panic room", "Police station", "Courtroom", "Prison", "Security office", "Self-defense classes"]
sugg_rapist      .hate_spot += [sugg_criminal]
sugg_pedophilia  .hate_spot += [sugg_criminal.hate_spot]
sugg_junkey      .hate_spot += [sugg_criminal.hate_spot]
sugg_couple      .hate_spot += []
sugg_frail       .hate_spot += ["Stair", "Slope", "McDonald's"]
sugg_old         .hate_spot += [sugg_frail.hate_spot, "funeral home", "Vietnam", "retirement home"]
sugg_ugly        .hate_spot += ["front of a mirror", "Outside"]
sugg_fat         .hate_spot += [sugg_ugly.hate_spot, "Stair", "Slope", "Gym", "juice server", "Diet clinic", "Salad bar", "Running track"]
sugg_illiteracy  .hate_spot += ["Library", "School"]
sugg_poor        .hate_spot += ["Tax office"]
sugg_middle_aged .hate_spot += [sugg_frail.hate_spot]
sugg_play_girl        .hate_spot += []
sugg_womanizer   .hate_spot += []

# Add new items in poor.hate_spot without any explanations. Align characters and spaces with existing instances.

# Define poor.hate_spot without any explanations. Align characters and spaces with existing instances.








########################################################################################################################################################################################################

# あるピー一週間 hacker armwrestling 追加




sugg_criminal    .love_time += ["Night", "Police shift changes", "Low traffic time", "Suspension period"]
sugg_rapist      .love_time += [sugg_criminal.love_time]
sugg_pedophilia  .love_time += [sugg_criminal.love_time, "School dismissal time", "Summer vacation", "After school", "Weekend"]
sugg_junkey      .love_time += [sugg_criminal.love_time]
sugg_frail       .love_time += []
sugg_old         .love_time += ["Time of Death", "Early bird specials", "Senior discount days", "Family visit times"]
sugg_ugly        .love_time += []
sugg_fat         .love_time += [sugg_ugly.love_time]
sugg_illiteracy  .love_time += ["typhoon"]
sugg_poor        .love_time += ["Payday", "Discount period"]
sugg_middle_aged .love_time += [sugg_frail.love_time]
sugg_play_girl        .love_time += ["Valentine's Day",]
sugg_womanizer   .love_time += [sugg_play_girl        .love_time]

# Define poor.love_time without any explanations. Align characters and spaces with existing instances.

# Add new items in illiteracy.love_time without any explanations. Align characters and spaces with existing instances.





sugg_criminal    .hate_time += ["Daylight hours", "Patrol time", "High traffic time", "Suspension period"]
sugg_rapist      .hate_time += [sugg_criminal.hate_time]
sugg_pedophilia  .hate_time += [sugg_criminal.hate_time]
sugg_junkey      .hate_time += [sugg_criminal.hate_time]
sugg_frail       .hate_time += []
sugg_old         .hate_time += ["Time of Death", "Emergency room hours"]
sugg_ugly        .hate_time += []
sugg_fat         .hate_time += [sugg_ugly.hate_time, "Meal prep time"]
sugg_illiteracy  .hate_time += ["Testing periods", "Class hours"]
sugg_poor        .hate_time += ["Rent due dates", "Tax season", "Bill due dates", "Children's birthday", "X'mas"]
sugg_middle_aged .hate_time += [sugg_frail.hate_time]
sugg_play_girl        .hate_time += []
sugg_womanizer   .hate_time += []

# Define poor.hate_time without any explanations. Align characters and spaces with existing instances.


# Add new items in illiteracy.hate_time without any explanations. Align characters and spaces with existing instances.







########################################################################################################################################################################################################
sugg_criminal    .love_tool += ["bar", "bat", "gun", "balaclava", "knife", "van", "lawyer", "parole", "human rights"]
sugg_criminal    .love_tool += [sugg_criminal.love_tool]
sugg_pedophilia  .love_tool += [sugg_criminal.love_tool, "sweets", "toy", "icecream van"]
sugg_junkey      .love_tool += [sugg_criminal.love_tool, "syringe"]
sugg_frail       .love_tool += ["grab bar", "soft food"]
sugg_old         .love_tool += [sugg_frail.love_tool, "reading glasses", "walking cane", "walker", "hearing aid"]
sugg_ugly        .love_tool += ["face mask", "filter", "photo editor"]
sugg_fat         .love_tool += [sugg_frail.love_tool, sugg_ugly.love_tool, "walker", "Electric wheelchair"]
sugg_illiteracy  .love_tool += ["comic books", "video games"]
sugg_poor        .love_tool += ["second-hand goods", "food stamps"]
sugg_middle_aged .love_tool += [sugg_frail.love_tool, "washlet", "recliner chair", "multivitamins"]
sugg_play_girl   .love_tool += ["sex toy", "rubber", "abortion clinic"]
sugg_womanizer   .love_tool += [sugg_play_girl.love_tool]
# Add new items in middle_aged.love_tool without any explanations. Align characters and spaces with existing instances.


# Define poor.love_tool without any explanations. Align characters and spaces with existing instances.





sugg_criminal    .hate_tool += ["rape alert", "CCTV", "Security alarms", "panic buttons", "tracking devices", "key", "guard dog", "mobile safety apps", "DNA analysis", "law", "911", "police"]
sugg_criminal    .hate_tool += [sugg_criminal.hate_tool]
sugg_pedophilia  .hate_tool += [sugg_criminal.hate_tool, "child protection laws", "internet safety filters"]
sugg_junkey      .hate_tool += [sugg_criminal.hate_tool]
sugg_frail       .hate_tool += ["meat", "hard food"]
sugg_old         .hate_tool += [sugg_frail.hate_tool, "nursing home brochure", "machine"]
sugg_ugly        .hate_tool += ["mirror"]
sugg_fat         .hate_tool += [sugg_ugly.hate_tool, "scale"]
sugg_illiteracy  .hate_tool += ["books", "numbers"]
sugg_poor        .hate_tool += ["donation box", "tax", "invoices"]
sugg_middle_aged .hate_tool += [sugg_frail.hate_tool]
sugg_play_girl   .hate_tool += ["event wristband","rubber","STI test"]
sugg_womanizer   .hate_tool += [sugg_play_girl.love_tool]


# Add new items in frail.hate_tool without any explanations. Align characters and spaces with existing instances.

# Define illiteracy.hate_tool without any explanations. Align characters and whitespaces with existing instances.






########################################################################################################################################################################################################


sugg_criminal    .love_word += ["You have the right to remain silent.",  "Parole granted.", "Your lawyer is here to see you.", "Plea bargain.", "You have visitors.",]
sugg_rapist      .love_word += [sugg_criminal.love_word]
sugg_pedophilia  .love_word += [sugg_criminal.love_word]
sugg_junkey      .love_word += [sugg_criminal.love_word]
sugg_frail       .love_word += []
sugg_old         .love_word += ["It's jelly.", "Your grandson has arrived."]
sugg_ugly        .love_word += []
sugg_fat         .love_word += ["It's all you can eat.", "Would you like to have some fries with it?"]
sugg_illiteracy  .love_word += ["School is closed today."]
sugg_poor        .love_word += ["It's on discount.", "You can pay in installments.", "The tests show I'm not pregnant."]
sugg_middle_aged .love_word += []
sugg_play_girl        .love_word += []
sugg_womanizer   .love_word += []

### This is for creating comedy. usage example: A fat man is sleeping. His wife whispers in his ear to wake him up, "Would you like to have some fries with it?" The fat man loves fries because he is fat, and wakes up surprised by what his wife whispered.

# Add new items in criminal.love_word without any explanations. Align characters and spaces with existing instances.


# Define illiteracy.love_word without any explanations. Align characters and whitespaces with existing instances.


sugg_criminal    .hate_word += ["Stop the car", "Sir, Do you have ID?", "You have the right to remain silent.", "Can I see some identification, please?", "Would you mind if I conducted a quick pat-down?", "What's this in your pocket?","Hands behind your back.","Step out of the vehicle.","We have a warrant.","You're coming downtown with us.","You have visitors in the interrogation room.","Empty your pockets.","You match the description.","We have an eyewitness.""Your fingerprints are on file.""Your accomplice confessed.""We have a warrant.""You're surrounded."]
sugg_rapist      .hate_word += [sugg_criminal.hate_word]
sugg_pedophilia  .hate_word += [sugg_criminal.hate_word]
sugg_junkey      .hate_word += [sugg_criminal.hate_word]

sugg_frail       .hate_word += ["Go up the stairs and it's on the right."]
sugg_old         .hate_word += [sugg_frail.hate_word, "It's snowing tomorrow.", "Your medicine is ready.", "Grandpa, you should really consider a retirement home.", "(Vietnamese language)"]
sugg_ugly        .hate_word += []
sugg_fat         .hate_word += [sugg_frail.hate_word, "Escalator is out of order.", "The buffet is closing soon.", "Desserts are sold out."]
sugg_illiteracy  .hate_word += ["I didn't understand your instructions."]
sugg_poor        .hate_word += ["My period is late.","I got pregnant.", "That's the price excluding tax.", "Hello, this is the tax office.", "Hello, this is the landlord.", "Please wait while we check your credit history.", "Dad, I want to go to college.", "Sorry, we don’t accept food stamps.", "I can't make friends without a game console."] # Add new 10 words that poverty people hates. No explanations.
sugg_middle_aged .hate_word += [sugg_frail.hate_word]
sugg_play_girl   .hate_word += ["I tested positive for HIV.", "Let's be exclusive.", "Meet my parents.", "I want a serious relationship.", "You never call me.", "Why didn't you text back?", "I told my friends about us.", "Is that your husband?"]
sugg_womanizer   .hate_word += ["I got pregnant.", "Can I stay the night?", "Wear a rubber.", "I tested positive for HIV.", "Let's be exclusive.", "Meet my parents.", "I want a serious relationship.", "You never call me.", "Why didn't you text back?","My period is late.", "I told my friends about us.", "Is that your wife?"]




### This is for creating comedy. usage example: A fat man is sleeping. His wife whispers in his ear to wake him up, "Escalator is out of order." The fat man hates stairs because he is fat, and wakes up surprised by what his wife whispered.

# Add new items in illiteracy.hate_word without any explanations. Align characters and spaces with existing instances.


# Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.









########################################################################################################################################################################################################

sugg_criminal    .love_sign += ["20 miles to the US-Mexican border.", "20 miles to the state line"]
sugg_pedophilia  .love_sign += [sugg_criminal.love_word]
sugg_junkey      .love_sign += [sugg_criminal.love_word]
sugg_frail       .love_sign += []
sugg_old         .love_sign += []
sugg_ugly        .love_sign += []
sugg_fat         .love_sign += []
sugg_illiteracy  .love_sign += []
sugg_poor        .love_sign += ["30% OFF", "FREE", "installment plan"]
sugg_middle_aged .love_sign += []
sugg_play_girl   .love_sign += []

### This is for creating comedy. usage example: A fat man is sleeping. His wife whispers in his ear to wake him up, "Would you like to have some fries with it?" The fat man loves fries because he is fat, and wakes up surprised by what his wife whispered.

# Add new items in criminal.love_word without any explanations. Align characters and spaces with existing instances.


# Define illiteracy.love_word without any explanations. Align characters and whitespaces with existing instances.

sugg_criminal    .hate_sign += ["Surveillance Cameras in Operation", "DRIVER'S LICENSE CHECK POINT AHEAD", "PROTECTED BY PSA PACIFIC SECURITY ALARM [206]575-7813", "Beware of Dog"]
sugg_pedophilia  .hate_sign += [sugg_criminal.hate_word]
sugg_junkey      .hate_sign += [sugg_criminal.hate_word]
sugg_frail       .hate_sign += ["Escalator out of order"]
sugg_old         .hate_sign += [sugg_frail.hate_sign]
sugg_ugly        .hate_sign += []
sugg_fat         .hate_sign += [sugg_frail.hate_sign]
sugg_illiteracy  .hate_sign += []
sugg_poor        .hate_sign += []
sugg_middle_aged .hate_sign += [sugg_frail.hate_sign]
sugg_play_girl        .hate_sign += []

### This is for creating comedy. usage example: A police officer places a sign that says "30% OFF" in front of a pit to catch poor people, who fall into the trap because they like discounts.

# Add new items in criminal.hate_word without any explanations. Align characters and spaces with existing instances.


# Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.







########################################################################################################################################################################################################
sugg_criminal    .love_sound += []
sugg_pedophilia  .love_sound += ["School dismissal bell"]
sugg_junkey      .love_sound += []
sugg_frail       .love_sound += []
sugg_old         .love_sound += []
sugg_ugly        .love_sound += []
sugg_fat         .love_sound += ["The sound of McDonald's fries being cooked.", "The sound of frying food."]
sugg_illiteracy  .love_sound += []
sugg_poor        .love_sound += ["The sound of a coin falling to the ground"]
sugg_middle_aged .love_sound += []
sugg_play_girl        .love_sound += []

### This is for creating comedy. usage example: A fat man is sleeping. His wife whispers in his ear to wake him up, "Would you like to have some fries with it?" The fat man loves fries because he is fat, and wakes up surprised by what his wife whispered.

# Add new items in criminal.love_word without any explanations. Align characters and spaces with existing instances.


# Define illiteracy.love_word without any explanations. Align characters and whitespaces with existing instances.


sugg_criminal    .hate_sound += ["police car siren"]
sugg_pedophilia  .hate_sound += [sugg_criminal.hate_sound]
sugg_junkey      .hate_sound += [sugg_criminal.hate_sound]
sugg_frail       .hate_sound += []
sugg_old         .hate_sound += []
sugg_ugly        .hate_sound += []
sugg_fat         .hate_sound += []
sugg_illiteracy  .hate_sound += []
sugg_poor        .hate_sound += []
sugg_middle_aged .hate_sound += []
sugg_play_girl        .hate_sound += []

### This is for creating comedy. usage example: A police officer places a sign that says "30% OFF" in front of a pit to catch poor people, who fall into the trap because they like discounts.

# Add new items in criminal.hate_word without any explanations. Align characters and spaces with existing instances.
# Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.


########################################################################################################################################################################################################








########################################################################################################################################################################################################
sugg_criminal    .hobby     += ["using illegal drugs"]
sugg_pedophilia  .hobby     += ["watching anime"]
sugg_junkey      .hobby     += []
sugg_frail       .hobby     += []
sugg_old         .hobby     += ["playing chess"]
sugg_ugly        .hobby     += []
sugg_fat         .hobby     += ["eating"]
sugg_illiteracy  .hobby     += ["watching baseball"]
sugg_poor        .hobby     += []
sugg_middle_aged .hobby     += ["watching baseball", "playing golf", "fishing", "collecting vinyl records", "riding a motorcycle"]
sugg_play_girl        .hobby     += [sugg_middle_aged.hobby, "smoking", "drinking", "playing an instrument"]

# Add new items in middle_aged.hobby without any explanations. Align characters and spaces with existing instances.
#   Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.

sugg_criminal    .grasp     += ["criminal law and sentences", "CCTV positions", "Their target's daily routine"]
sugg_pedophilia  .grasp     += [sugg_criminal.grasp]
sugg_junkey      .grasp     += [sugg_criminal.grasp]
sugg_frail       .grasp     += ["one's own calorie intake", "one's blood sugar level", "health insurance premiums"]
sugg_old         .grasp     += [sugg_frail.grasp]
sugg_ugly        .grasp     += ["cosmetic surgery costs"]
sugg_fat         .grasp     += [sugg_frail.grasp]
sugg_illiteracy  .grasp     += []
sugg_poor        .grasp     += []
sugg_middle_aged .grasp     += [sugg_frail.grasp]
sugg_play_girl        .grasp     += []

# Add new items in middle_aged.grasp without any explanations. Align characters and spaces with existing instances.
#   Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.


sugg_criminal    .media_on   += ["News", "Wikipedia", "EU-SOCTA", "Neighborhood Watch"]
sugg_pedophilia  .media_on   += [sugg_criminal.media_on, "Dru Sjodin National Sex Offender Public Website", "Sex offender gps trafficker", "State and Local Sex Offender Registries"]
sugg_frail       .media_on   += []
sugg_old         .media_on   += ["Letters to the Editor section of a newspaper", "Vietnam Veterans of America Roster"]
sugg_ugly        .media_on   += []
sugg_fat         .media_on   += []
sugg_illiteracy  .media_on   += []
sugg_poor        .media_on   += []
sugg_middle_aged .media_on   += []
sugg_play_girl        .media_on   += []

# Add new items in middle_aged.grasp without any explanations. Align characters and spaces with existing instances.
#   Define illiteracy.hate_word without any explanations. Align characters and whitespaces with existing instances.













########################################################################################################################################################################################################


# ビッグスクーターはバイクに入るか　打ちっ放しはゴルフに入るか

########################################################################################################################################################################################################

sugg_criminal    .cliche += ["I'll call a lawyer.", "Do you have a warrant?", "I can't breathe!", "Can I have your badge number?", "I deny the charges", "I need medical attention.", "You have the wrong person!", "I plead the Fifth.", "It wasn't me, it was him!", "Forced into it"]# Add new 20 cliche phrase without any explanations
sugg_rapist      .cliche += [sugg_criminal.cliche, "It was consensual.", "The woman asked me to have sex with her.", "She never said no.", "She didn't resist.","She made it up for revenge.","We were both drunk.",  "She was dressed provocatively.","She wanted attention.","She’s doing this for money.","She led me on." "She was asking for it." "I didn't force her."]
sugg_pedophilia  .cliche += [sugg_criminal.cliche, "Do you want some candy?", "The ice cream van is here!","Don't tell your parents.", "It's our little secret.", "You can trust me.","Nobody will believe you.","Don't you know? This is something all the other Boy Scouts do.", "Even if a boy says it, no one will believe him", "I need your help with something in my car.", "If you do this, I’ll give you a present.", "Wow! I’m 14 too! Can I send you a friend request?", "I have a puppy at home, want to see it?", "Where is the toilet in this park? Please show me."]
sugg_junkey      .cliche += [sugg_criminal.cliche, "I'm just holding this for a friend.", "These are just mosquito bite marks", "The grass there grew on its own.", "I swear, I thought it was oregano.", "I'm an undercover journalist doing research.", "This white stuff is just flour."]

cp_before_having_sex  = ["How about we take this to the next level?", "We missed the last train.", "I'm tired, so let's rest at the hotel.", "Do you have the 0.1mm ones in this store?", "Calm down, Let's just go with the flow.", "Calm down, Let's set the mood.",]
cp_when_having_sex    = ["Can we turn off the lights?","Is it just me, or is it getting hot in here?", "I think we need some mood music.", "Slower."]
cp_after_having_sex   = ["Get me a tissue.", "Is it over yet?", "Do you want some water?", "I hope I didn't snore.",]
sugg_play_girl   .cliche += cp_before_having_sex + cp_when_having_sex + cp_after_having_sex
sugg_womanizer   .cliche += cp_before_having_sex + cp_when_having_sex + cp_after_having_sex
sugg_old        .cliche += []

# Add new 10 cliche phrase in "play_girl .cliche_phrase" python without any explanations.




# the_phrases = ["Can we turn off the lights?","Is it just me, or is it getting hot in here?", "I think we need some mood music."]




########################################################################################################################################################################################################






########################################################################################################################################################################################################



sugg_pedophilia.situation+=[

# pervert.situation=[
# For creating Horror situations. Ali is a pervert.

# Each item should start with "Ali".
# Mislead and Plot twist sections should start with "Location = [one noun]"
# Add new 3 situations.
# Start answer with ```python. Only output new situations.
# The existing situations are correct. You have to observe and mimic them.

 """Ali explanins that he wanted to do the job because he was influenced by child actors.
    Mislead     : Location = An interview to become an actor
    Plot twist  : Location = An interview to become a pediatrician
    Composition : Perverts want to touch children -> What kind of job involves touching children? -> Pediatrician

    """
,"""Ali asks the receptionist if he can find the child who is short, skinny and tanned.
    Mislead     : Location = A lost children center
    Plot twist  : Location = An adoption office
    Composition : Perverts have a certain appearance that they like. -> In what situations would it be natural for a person to describe a child's appearance in detail? -> Lost Child Center
    """


    
,"""Ali palpates a child patient.
    Mislead     : Location = A pediatric clinic
    Plot twist  : Location = A dental clinic"""
,"""Ali tries to pick up girls.
    Mislead     : Location = A pick-up spot
    Plot twist  : Location = A kindergarten"""
,"""Ali caused damage to a child patient's colon through medical malpractice.
    Mislead     : Location = A proctology clinic
    Plot twist  : Location = A dental clinic"""
,"""Ali gives a child CPR.
    Mislead     : Location = An emergency scene
    Plot twist  : Location = A dissection room"""




 """Ali explanins that he wanted to do the job because he was influenced by child actors.
    Mislead     : Ali = A man who wants to be an actor; Location = An interview to become an actor
    Plot twist  : Location = An interview to become a pediatrician"""
,"""Ali asks the receptionist if he can find the child who is short, skinny and tanned.
    Mislead     : Ali = A parent; Location = A lost children center
    Plot twist  : Ali = Not the parent; Location = An adoption office"""
,"""Ali tries to pick up girls.
    Mislead     : Ali = An ordinary play boy; Location = a pick-up spot
    Plot twist  : Location = A kindergarten"""
,"""Ali caused damage to a child patient's colon through medical malpractice.
    Mislead     : Ali = A proctologist; Location = A proctology clinic
    Plot twist  : Ali = A dentist; Location = A dental clinic"""






 """Ali explanins that he wanted to do the job because he was influenced by child actors.
    Mislead: Ali = A man who wants to be an actor; Location = An interview to become an actor
    Plot twist: Location = An interview to become a pediatrician
    Motivation: Ali tries to contact children's body"""
,"""Ali asks the receptionist if he can find the child who is short, skinny and tanned.
    Mislead: Ali = A parent; Location = A lost children center
    Plot twist: Ali = Not the parent; Location = An adoption office
    Motivation: Ali tries to get a child who looks just the way he wants."""
,"""Ali tries to pick up girls.
    Mislead: Ali = An ordinary play boy; Location = a pick-up spot
    Plot twist: Location = A kindergarten
    Motivation: Ali tries to pick up children."""
,"""Ali caused damage to a child patient's colon through medical malpractice.
    Mislead: Ali = A doctor; Location = A proctology clinic
    Plot twist: Ali = A dentist; Location = A dental clinic
    Motivation: Ali got involved with the child"""



,"""Ali searches for a child at a lost children center.
    Mislead: Ali = The parent.
    Plot twist: Ali = Not the parent.
    Motivation: Ali tries to get others' children"""
]


"""
pervert.situation+=[
 "In a delivery room, Ali, a man, supports Bob as she gives birth. This misleads Ali as Bob's husband. Bob, a pregnant, says: Who are you? You're not my husband."
,"In Bob's house, Ali a man, insists on planning a surprise anniversary party for Bob. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In Bob's house, Ali a man, offers to cook dinner for Bob and set the mood with candles. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In a private room at a spa, Ali, a man, offers to give Bob a massage to help her relax. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"At the wedding venue, Ali, a man, complains about the ceremony order. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In the car on a road trip, Ali, a man, plays music he thinks would make the drive enjoyable for both of them. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In a secluded cabin, Ali, a man, suggests they play board games for fun. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In a hotel room, Ali, a man, suggests they watch a movie together to unwind. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
,"In Bob's bedroom, Ali, a man, offers to help organize Bob's closet. This misleads Ali as Bob's husband. Bob, a woman, says: Who are you? You're not my husband."
# Add new 10 situations what end with "Bob, a woman, says: Who are you? You're not my husband.". Start answer with ```python. Only output new situations. Just mimic the existing situations.
]
"""


sugg_play_girl.situation+=[

# Sitcom situations. Ali's father suspects Ali is a slut in the following situations:
 "In Ali's funeral                       , there are many men in the attendance"
,"In Ali's wedding                       , there are many men trying to call off the wedding"
,"In search for the missing Ali          , there are many men who can offer detail information about Ali"
,"In investigation into the murder of Ali, there are many men whose DNA was found on Ali's body"
,"In court case against Ali              , there are many men who is ready to filiates Ali's child"
,"At a press conference about a scandal  , there are many men defending Ali's reputation"
,"At the site of a plane crash           , there are many men waiting for news of Ali"
,"After a devastating house fire         , there are many men helping to search for Ali"
,"At the hospital where Ali is treated   , there are many men waiting for news about Ali's condition"
,"In the aftermath of a natural disaster , there are many men helping to recover the missing"
# Add new 10 situations. Start answer with ```python. Only output new instances. Each situation should involve something tragic: a death, a legal battle, a disaster, an incident, etc.


# Sitcom situations. Bob suspects Ali because there is plenty of evidence that she is a slut.
,"Bob is a Muslim.          Ali is planning to marry with him"
,"Bob is a Shinto priest.   Ali is planning to become a Shinto maiden"
,"Bob is a father.          Ali is planning to marry with Bob's son"
# Add new 10 situations. Start answer with ```python. Only output new instances. Ali must be a virgin in each situation.
]

sugg_old.situation+=[
# Sitcom situations. Bob suspects Ali is old.

 "Bob is the potter.            Ali applies to become an apprentice to Bob, the potter, who has no successor. Ali's face is hidden by frosted glass, but Bob suspects that Ali might be an old man."
,"Bob is the father.            Ali is Bob's daughter's boyfriend. Although Ali's face is not visible on the phone, Bob suspects that Ali is an old man."
,"Bob is the coach.             Ali tries to fill in for a sudden vacancy on the sports team. Ali's face is obscured by his football gear, but Bob suspects he may be an old man."
,"Bob is the firefighter.       Ali rushes into the burning building to save Bob who is trapped inside. Ali's face is hidden by rubbles, but Bob suspects that Ali might be an old man."
,"Bob is the patient.           Ali is the surgeon performing Bob's surgery. Although Bob cannot see Ali's face because his eyes are covered with a medical sheet, Bob suspects that Ali is an old man."
,"Bob is the pilot.             Ali is a passenger on a turbulent flight. Bob cannot see Ali because of the cabin pressure mask, but he suspects that Ali might be an old man who is at risk of a heart attack."

# Add new 10 situations. Start answer with ```python. Only output new situations. In each situation, Bob must be in a position to be harmed by Ali being old.



,"Bob is the amnesiac.          Ali is Bob's wife. Ali's face is hidden by the bandage covering Bob's eyes, but Bob suspects that Ali might be an old man."

]



