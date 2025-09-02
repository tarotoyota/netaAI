from dataclasses import dataclass, field
from typing import List, ClassVar, Optional

@dataclass
class FactAgentNecessarySexual:
    ALL_FACTNECESSARYSEXUAL: ClassVar[List['FactAgentNecessarySexual']] = []
    # Why there is such thing]
    INST_FactNecessarySexual    :str
    sexual_touching_contacting  :list= field(default_factory=list)
    sexual_filming_watching     :list= field(default_factory=list) # When filmed this, When saw this
    sexual_questioning_knowing  :list= field(default_factory=list) # How did you know this (change)
    sexual_ordering_regulating  :list= field(default_factory=list) #
    sexual_getting_material     :list= field(default_factory=list) # Why do you (still) (have/ carry) around this?, Why this is {changed}
    sexual_moving_mobility      :list= field(default_factory=list) # Why are you here, How did you know here
    sexual_without              :list= field(default_factory=list)
    cbsx_to_despite             :list= field(default_factory=list) #
    def __post_init__(self):
        FactAgentNecessarySexual.ALL_FACTNECESSARYSEXUAL.append(self)

# 医療関係のインスタンスならば"She seemed to be feel unwell" などが使える

# I have to call an ambulance.
# I have to call the police.
# We need a doctor.
# She looks unwell. She was crying.
# 

# Define 20 instances of occupations or positions related to [physical contact, restrictions on movement, restrictions on clothing, restrictions on social relationships, sexual photography, sexual questions].
# Don't add explicitly sexual occupations (e.g. porn actor)
# Don't create instances that are similar to existing ones.
# Start answer with ```python. 

cbsx_cop                  = FactAgentNecessarySexual("cbsx_cop             ")
cbsx_bodyguard            = FactAgentNecessarySexual("cbsx_bodyguard       ")
cbsx_jail_keeper          = FactAgentNecessarySexual("cbsx_jail_keeper     ")
cbsx_firefighter          = FactAgentNecessarySexual("cbsx_firefighter     ")
cbsx_teacher              = FactAgentNecessarySexual("cbsx_teacher         ")
cbsx_husband              = FactAgentNecessarySexual("cbsx_husband         ")
cbsx_sitter               = FactAgentNecessarySexual("cbsx_sitter          ")
cbsx_director             = FactAgentNecessarySexual("cbsx_director        ")
cbsx_sports_coach         = FactAgentNecessarySexual("cbsx_sports_coach    ")
cbsx_counselor            = FactAgentNecessarySexual("cbsx_counselor       ")
cbsx_parent               = FactAgentNecessarySexual("cbsx_parent          ")
cbsx_masseuse             = FactAgentNecessarySexual("cbsx_masseuse        ")
cbsx_doctor               = FactAgentNecessarySexual("cbsx_doctor          ")
cbsx_veterinarian         = FactAgentNecessarySexual("cbsx_veterinarian    ")
cbsx_obstetrician         = FactAgentNecessarySexual("cbsx_obstetrician    ")
cbsx_caregiver            = FactAgentNecessarySexual("cbsx_caregiver       ")
cbsx_livestock_farmer     = FactAgentNecessarySexual("cbsx_livestock_farmer")
cbsx_pet_owner            = FactAgentNecessarySexual("cbsx_pet_owner       ")
cbsx_student              = FactAgentNecessarySexual("cbsx_student         ")
cbsx_baby                 = FactAgentNecessarySexual("cbsx_baby            ")
cbsx_animal               = FactAgentNecessarySexual("cbsx_animal          ")
cbsx_survivor             = FactAgentNecessarySexual("cbsx_survivor        ")
cbsx_corpse_handler       = FactAgentNecessarySexual("cbsx_corpse_handler  ")
cbsx_toilet_cleaner       = FactAgentNecessarySexual("cbsx_toilet_cleaner  ")
cbsx_camp_supervisor      = FactAgentNecessarySexual("cbsx_camp_supervisor ")
cbsx_zookeeper            = FactAgentNecessarySexual("cbsx_zookeeper")
cbsx_fighter              = FactAgentNecessarySexual("cbsx_fighter")
cbsx_life_guard           = FactAgentNecessarySexual("cbsx_life_guard")
cbsx_patient              = FactAgentNecessarySexual("cbsx_patient")

# Sexual tasks that is allowed to the occupation.
cbsx_cop              .sexual_touching_contacting += ["Check the body by touching it", "Apprehending", "Strip search", "Handcuffing", "Body cavity search", "Physical restraint", "Sedative administration", "Accessing to illegal prostitution"]
cbsx_jail_keeper      .sexual_touching_contacting += ["Check the body by touching it", "Apprehending", "Strip search", "Handcuffing", "Body cavity search", "Physical restraint", "Sedative administration"]
cbsx_firefighter      .sexual_touching_contacting += ["Artificial breathing", "Chest compressions", "Remove cloth", "Cut cloth"]
cbsx_teacher          .sexual_touching_contacting += ["Touching the body during physical education classes", "Physical punishment"]
cbsx_husband          .sexual_touching_contacting += ["Having sex"]
cbsx_sitter           .sexual_touching_contacting += ["Assist with toileting","Put her to bed", "Changing diapers", "Bathing", "Applying lotion", "Physical punishment", "Give her an enema", "Assisting with dressing", "Dressing/Undressing", "Skin rash inspection", "Potty training", "Applying diaper cream", "Temperature check", "Hair brushing", "Nail trimming", "Tickling", "Playing physical games"]
cbsx_director         .sexual_touching_contacting += ["Give acting guidance by touching her", "Adjust costume fit", "Adjusting actress' wardrobe"]
cbsx_sports_coach     .sexual_touching_contacting += ["Correcting posture through physical contact", "Assisting with stretching exercises", "Providing massage for muscle relief", "Providing first aid", "Checking for injuries through tactile examination", "Applying sports tape or braces", "Assisting with weightlifting form"]
cbsx_counselor        .sexual_touching_contacting += []
cbsx_parent           .sexual_touching_contacting += ["Assist with toileting","Put her to bed", "Physical punishment", "Check body temperature","Dressing/Undressing", "Assisting with dressing"]
cbsx_masseuse         .sexual_touching_contacting += ["Put her to bed", "Massage"]
cbsx_doctor           .sexual_touching_contacting += ["Check the rectal temperature", "Check the body temperature", "Artificial breathing", "Chest compressions", "Remove cloth", "Palpating", "Administering anesthesia", "Temperature check", "Give her an enema","Physical examination at school", "Artificial insemination", "Rectal irrigation"]
cbsx_veterinarian     .sexual_touching_contacting += ["Check the rectal temperature", "Check the body temperature", "Deliver a baby during birth", "Insert his hand into the birth canal", "Palpate", "Tooth brushing", "Injection", "Bathe"]
cbsx_obstetrician     .sexual_touching_contacting += ["Check the rectal temperature", "Check the body temperature", "Deliver a baby during birth", "Insert his hand into the birth canal", "Palpate", "Artificial insemination"]
cbsx_caregiver        .sexual_touching_contacting += ["Check the rectal temperature", "Check the body temperature", "Assist with toileting","Put her to bed", "Massage", "Change diaper", "Give her an enema", "Check body temperature", "Dressing/Undressing", "Bathe", "Wipe body", "Assisting with dressing"]
cbsx_livestock_farmer .sexual_touching_contacting += ["Castrate", "Pet", "Shave", "Bathing", "Palpate", "Give an injection", "Dressing", "Microchipping", "Putting on a nose ring", "Putting on a collar", "Branding with a branding iron", "Check the rectal temperature", "Assist with birthing", "Insert hand into birth canal", "Tagging or marking", "Cleaning udders", "Milking", "Restrain for examination"]
cbsx_pet_owner        .sexual_touching_contacting += ["Castrate", "Pet", "Shave", "Bathing", "Palpate", "Give an injection", "Dressing", "Microchipping", "Putting on a nose ring", "Putting on a collar", "Kissing"]
cbsx_student          .sexual_touching_contacting += ["wear kids clothes", "Excreting in a potty", "Participate in gym and swimming classes", "Physical examination at school", "Change clothes for gym class", "Be subject to physical discipline", ]
cbsx_baby             .sexual_touching_contacting += ["being naked and wearing only a diaper", "Excreting in a diaper/ potty", "Suckle on an other's breast", "Being bathed", "Being assisted with dressing/undressing", "being kissed"]
cbsx_animal           .sexual_touching_contacting += ["defecate outdoors", "being naked", "Licking someone's face","Sniffing each other's genitals","Mounting another animal in public","Licking another animal's genitals","Humping furniture or people's legs","Marking territory by urinating on objects","Grooming another animal's private parts","Rubbing their body against people or objects","Vocalizing mating calls near another individual"]
cbsx_corpse_handler   .sexual_touching_contacting += ["Wash the body", "Change clothing", "Positioning limbs", "Bury others", "Burn others"]
cbsx_toilet_cleaner   .sexual_touching_contacting += []
cbsx_camp_supervisor  .sexual_touching_contacting += ["Assist with first aid", "Supervise wear changes", "Help with sunscreen application", "Check for ticks or insect bites"]
cbsx_zookeeper        .sexual_touching_contacting += ["Assist with mating", "Collect semen samples", "injection", "Palpate", "Artificial insemination", "Physical restraint for medical exams", "Bathe", "Check the rectal temperature", "Check the body temperature"]
cbsx_fighter          .sexual_touching_contacting += ["Grapple", "Punch", "Hold", "Ride on others", "Clinch"]
cbsx_life_guard       .sexual_touching_contacting += ["Hold others", "Take others away", "Performing CPR", "Removing clothes in emergencies", "Providing first aid", "Carrying individuals from water"]
cbsx_patient          .sexual_touching_contacting += ["Request a colonoscopy.", "Requesting hand-holding for comfort or reassurance","Assistance with mobility (helping to stand, walk, or transfer)","Physical support during medical procedures (steadying, holding)","Request Assistance with personal hygiene (bathing, grooming, oral care)","Request Help with dressing or undressing","Request Temperature checks","Request Application of lotion or ointment as prescribed","Request Assistance with toileting","Request Assistance with feeding (if unable to self-feed)","Request  Assistance with repositioning in bed or wheelchair"]

# Sexual tasks that is allowed to the occupation.
cbsx_cop              .sexual_filming_watching += ["Check the belongings", "Take a photo of face", "Monitoring surveillance cameras", "Look at naked victims", "Take a photo of deadbody", "Accessing to child porn", "Reviewing incident footage", "Track location history" ]
cbsx_jail_keeper      .sexual_filming_watching += ["Check the belongings", "Take a photo of face", "Monitoring surveillance cameras", "Film the cell", "Monitor shower areas", "View the cell through the peephole","Recording prisoner interactions", "Observing inmates during recreation",]
cbsx_firefighter      .sexual_filming_watching += ["Look at naked victims"]
cbsx_teacher          .sexual_filming_watching += ["Observe social media use", "Take a photo of students", "Patrol to ensure that students are not using busy areas", "Record classroom sessions","Collect and review students' personal devices","Check students' bags for prohibited items","Oversee students during swimming lessons"]
cbsx_husband          .sexual_filming_watching += ["Take a photo of woman", "Check the device", "Take a video of the birth", "Attend the birth"]
cbsx_sitter           .sexual_filming_watching += ["Take photo of child", "Record frequency of bowel movements and condition of excrement", "Bath time recording", "Diaper change documentation", "Filming children playing"]
cbsx_director         .sexual_filming_watching += ["Demanding bedtime scene", "Demanding nude scenes", "Requesting dangerous stunts", "Filming rehearsal footage", "Reviewing audition tapes", "Capturing intimate angles", "Monitoring costume changes", "Documenting physical transformations", "Filming auditions","Documenting behind-the-scenes"]
cbsx_sports_coach     .sexual_filming_watching += ["filming performance and play", "Examining the affected area", "Check the bodily change", "Check her physical growth"]
cbsx_counselor        .sexual_filming_watching += ["Grasp about the daily life"]
cbsx_parent           .sexual_filming_watching += ["Check the belonging", "Check the device", "Observe social media use", "Track location history","Look at baby monitors","Watching home videos", "Looking at photos of the child", "Monitoring video calls", "Checking browsing history", "Looking through social media", "Reviewing educational videos with the child", "Watching child's performances or events"]
cbsx_masseuse         .sexual_filming_watching += ["Look at the naked body", "Observe pain responses"]
cbsx_doctor           .sexual_filming_watching += ["Take a photo of naked bodies", "Record frequency of bowel movements and condition of excrement", "Take a photo of chest", "Colonoscopy", "Observe pain responses", "CT scan"]
cbsx_veterinarian     .sexual_filming_watching += [cbsx_doctor.sexual_filming_watching]
cbsx_obstetrician     .sexual_filming_watching += [cbsx_doctor.sexual_filming_watching]
cbsx_caregiver        .sexual_filming_watching += [cbsx_doctor.sexual_filming_watching, "Track location history"]
cbsx_livestock_farmer .sexual_filming_watching += ["Take photos", "Monitor with surveillance cameras", "Record frequency of bowel movements and condition of excrement", "Record birthing process", "Film milking procedures", "Photograph for sale listings"]
cbsx_pet_owner        .sexual_filming_watching += ["Take photos", "Monitor with surveillance cameras", "Record frequency of bowel movements and condition of excrement", ]
cbsx_student          .sexual_filming_watching += ["Take selfies with children", "Record funny videos with children"]
cbsx_baby             .sexual_filming_watching += ["Being monitored with a baby camera", "Being filmed naked"]
cbsx_animal           .sexual_filming_watching += []
# Sexual tasks that is allowed to the occupation.
cbsx_corpse_handler   .sexual_filming_watching += []
cbsx_toilet_cleaner   .sexual_filming_watching += ["See excrement"]
cbsx_camp_supervisor  .sexual_filming_watching += []
cbsx_zookeeper        .sexual_filming_watching += ["Film mating", "See naked body", "Monitor cage"]
cbsx_fighter          .sexual_filming_watching += ["Film fighting", "Flim body condition"]
cbsx_life_guard       .sexual_filming_watching += ["Monitor pool with cameras", "Watch the pool from the lookout tower"]
# Add new items in the instances above

cbsx_patient          .sexual_filming_watching += ["Show one's private parts to others.", "Allowing observation by others",]




# Sexual tasks that is allowed to the occupation.
#  Add new 10 items in """  cbsx_sports_coach  """. Only return the new items you generated.  No explanations and annotations.

cbsx_cop              .sexual_questioning_knowing += ["address and contact information", "details of rape", "relationship status", "domestic disputes"]
cbsx_jail_keeper      .sexual_questioning_knowing += ["menstruation"]
cbsx_firefighter      .sexual_questioning_knowing += ["marital status", "address and contact information", "details of rape", "relationship status", "sexual history"]
cbsx_teacher          .sexual_questioning_knowing += ["address and contact information", "relationship status", "sex education", "Asking a student about their home life"]
cbsx_husband          .sexual_questioning_knowing += ["relationship history", "sexual history", "menstruation"]
cbsx_sitter           .sexual_questioning_knowing += ["bowel movements", "toilet training progress", "sex education", "bathing preferences", "bodily changes", "dating life", "friends"]
cbsx_director         .sexual_questioning_knowing += ["her BWH", "her menstrual cycle", "personal experiences relevant to a role", "wardrobe preferences"]
cbsx_sports_coach     .sexual_questioning_knowing += ["athlete's bowel movements", "Inquire about menstrual cycle", "Her measurements", "relationship status", "physical intimacy", "pregnancy status", "BWH"]
cbsx_counselor        .sexual_questioning_knowing += ["relationship history", "sexual history", "details of rape"]
cbsx_parent           .sexual_questioning_knowing += ["relationship history", "sexual history", "sex education"]
cbsx_masseuse         .sexual_questioning_knowing += ["bowel movements", "sexual history", "menstruation"]
cbsx_doctor           .sexual_questioning_knowing += ["bowel movements", "marital status", "address and contact information", "details of rape", "sexual history", "menstruation"]
cbsx_veterinarian     .sexual_questioning_knowing += ["bowel movements", "menstruation" "sexual history"]
cbsx_obstetrician     .sexual_questioning_knowing += ["bowel movements", "menstruation" "sexual history", "address and contact information"]
cbsx_caregiver        .sexual_questioning_knowing += ["bowel movements", "menstruation"]
cbsx_livestock_farmer .sexual_questioning_knowing += []
cbsx_pet_owner        .sexual_questioning_knowing += []
cbsx_student          .sexual_questioning_knowing += ["Ask about sex education", "Discuss changes in one's sexuality", "Ask children about romantic feelings"]
cbsx_baby             .sexual_questioning_knowing += []
cbsx_animal           .sexual_questioning_knowing += []

cbsx_corpse_handler   .sexual_questioning_knowing += []
cbsx_toilet_cleaner   .sexual_questioning_knowing += ["Searching for the culprit behind unflushed excrement."]
cbsx_camp_supervisor  .sexual_questioning_knowing += []
cbsx_zookeeper        .sexual_questioning_knowing += ["Asking about the reproductive cycles", "Inquiring about the mating behaviors"]
cbsx_fighter          .sexual_questioning_knowing += ["Asking about injuries in genitals"]
cbsx_life_guard       .sexual_questioning_knowing += ["Asking about menses"]

cbsx_patient          .sexual_questioning_knowing += []

# Sexual tasks that is allowed to the occupation. Add new items in cbsx_sports_coach


# Lists of acts that would be considered sexual crimes if committed by anyone other than someone in the profession. Add new items in cbsx_sports_coach without any explanations. I didn't say to add crime acts.
cbsx_cop              .sexual_ordering_regulating += ["Communication Restrictions", "Restrictions on freedom of movement", "Take the person away", "Detain", "Issue a restraining order", ]
cbsx_jail_keeper      .sexual_ordering_regulating += ["Communication Restrictions", "Restrictions on freedom of movement", "Enforce bedtime", "Order to strip naked", ]
cbsx_firefighter      .sexual_ordering_regulating += ["Take the person away"]
cbsx_teacher          .sexual_ordering_regulating += ["Forbid heterosexual relations", "Forcing to wear a school uniform", "Assigning specific seating arrangements in class", "Enforcing a specific hairstyle", "Prohibit extravagant decorations and clothing"]
cbsx_husband          .sexual_ordering_regulating += ["Forbid heterosexual relations", "Mandate abstinence", "Advise on partner selection", "Controlling access to contraception", "Ask to have children", "Ask to do household chores", "Ask to dress a certain way"]
cbsx_sitter           .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication","Ask to change clothes", "Forbid having visitors", "Enforce bedtime", "Restrict screen time", "Prohibit specific foods"]
cbsx_director         .sexual_ordering_regulating += ["Demanding specific body shape", "Demanding specific attire", "Enforce nudity clauses", "Mandate method acting preparation", "Make her say specific lines"]
cbsx_sports_coach     .sexual_ordering_regulating += ["Mandate specific training attire", "Pregnancy and sexual intercourse prohibition", "Mandate abstinence", "Enforce weight requirements", "Order to increase muscle", "Forcing someone to take certain medications or eat certain foods.", "Restrict social activities", "Control dietary intake", "Regulate sleep schedules", "Prohibit personal relationships", "Enforce physical conditioning routines"]
cbsx_counselor        .sexual_ordering_regulating += ["Prohibit any kind of relationship", "Recommend celibacy", "Advise on partner selection"]
cbsx_parent           .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication","Prohibit any kind of relationship", "Forbid heterosexua relations", "Advise on partner selection" ]
cbsx_masseuse         .sexual_ordering_regulating += ["Order to stay in bed"]
cbsx_doctor           .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication","Have the person hospitalized", "Mandate abstinence", "Forbid having visitors", "Enforce bedtime", "Forbid having sex", "Order to strip naked", "Require contraceptive use", "Ask to change the weight"]
cbsx_veterinarian     .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication", "Have her hospitalized", "Mandate abstinence", "Ask to change the weight"]
cbsx_obstetrician     .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication", "Have her hospitalized", "Mandate abstinence", "Ask to change the weight", "Require contraceptive use", "Order to strip naked", "Enforce bedtime", "Forbid having visitors"]
cbsx_caregiver        .sexual_ordering_regulating += ["Order to stay in bed", "Have her take the medication", "Enforce bedtime"]
cbsx_livestock_farmer .sexual_ordering_regulating += ["Buy and sell them", "Detain", "Locking them in cages or pens", "Mandate wearing a collar or harness", "Enforce feeding schedules", "Isolate from the herd", "Order to fast before procedures","Mandate specific feeding schedules","Enforce breeding restrictions","Control access to water or food","Mandate wearing identification tags","Order to strip off wool or fur (shearing)"]
cbsx_pet_owner        .sexual_ordering_regulating += ["Buy and sell them", "Detain", "Locking them in cages or pens", "Mandate wearing a collar or harness", "Enforce feeding schedules", "Isolate from the herd", "Order to stay in bed or designated area","Require use of a leash outdoors","Prohibit interaction with other animals","Control access to certain foods or treats","Enforce bathing or grooming routines","Order to wear clothing or accessories",]
cbsx_student          .sexual_ordering_regulating += ["Confess to children", "Demand to sleep in the same bed as an adult","Insist on being undressed by another person","Request to be bathed by an adult","Ask to be spoon-fed by someone else","Insist on being dressed or undressed by an adult","Demand to be carried in someone's arms", "Invite children to play", "Share secrets with children",]
cbsx_baby             .sexual_ordering_regulating += ["Cry to be breatfed at a specific time", "Seeking to be loved", "Cry to be held naked by others","Seek to be bathed with others","Demand to sleep in the same bed as others","Cry to be spoon-fed by others","Demand to be dressed or undressed by others"]
cbsx_animal           .sexual_ordering_regulating += ["Request petting"]

cbsx_corpse_handler   .sexual_ordering_regulating += []
cbsx_toilet_cleaner   .sexual_ordering_regulating += ["Request immediate notification of spills", "Order use certain toilet", "Order use of alternative facilities"]
cbsx_camp_supervisor  .sexual_ordering_regulating += ["Enforce curfews", "Let them sleep in the nearby tents "]
cbsx_zookeeper        .sexual_ordering_regulating += ["Control breeding", "Regulate feeding times", "Order enclosure maintenance"]
cbsx_fighter          .sexual_ordering_regulating += ["Mandate weight cuts", "Mandate specific attire"]
cbsx_life_guard       .sexual_ordering_regulating += []
cbsx_patient          .sexual_ordering_regulating += ["Invite someone to one's bed", "Requesting pain medication", "Request specific caregivers", "Request a change of bedding or clothing",]


# Sexual tasks that is allowed to the occupation.

# Lists of acts that would be considered sexual crimes if committed by anyone other than someone in the profession. Add new items in cbsx_sports_coach without any explanations. I didn't say to add crime acts.

cbsx_cop              .sexual_getting_material += ["Collect belongings", "Seize device", "Seize cloth", "Collect urine sample", "Collect DNA sample",     "Collect hair for testing",]
cbsx_jail_keeper      .sexual_getting_material += ["Collect belongings", "Seize device", "Seize cloth"]
cbsx_firefighter      .sexual_getting_material += ["Retrieve personal items", "Transport someone"]
cbsx_teacher          .sexual_getting_material += ["Collect device", "Collect accessories"]
cbsx_husband          .sexual_getting_material += ["Transport children"]
cbsx_sitter           .sexual_getting_material += ["Take away devices", "Confiscate personal items", "Retrieve clothing", "Collect diapers", "Looking through a child's belongings", "Checking their phone or tablet"]
cbsx_director         .sexual_getting_material += ["Collect uniforms"]
cbsx_sports_coach     .sexual_getting_material += ["Retrieve training gear and uniform", "Collect athlete's medical records", "Collect urine samples for doping test"]
cbsx_counselor        .sexual_getting_material += []
cbsx_parent           .sexual_getting_material += ["Retrieve clothing", "Collect diapers", "Search children"]
cbsx_masseuse         .sexual_getting_material += ["Retrieve clothing"]
cbsx_doctor           .sexual_getting_material += ["Retrieve clothing", "Collect urine, stool and blood sample", "Collect ovum"]
cbsx_veterinarian     .sexual_getting_material += [cbsx_doctor.sexual_getting_material]
cbsx_obstetrician     .sexual_getting_material += [cbsx_doctor.sexual_getting_material]
cbsx_caregiver        .sexual_getting_material += ["Retrieve clothing", "Collect urine and stool sample", "Collect diapers"]
cbsx_livestock_farmer .sexual_getting_material += ["Collect milk","Collect children","Retrieve wool, hair or fur","Collect urine or fecal samples","Collect blood samples","Collect semen for breeding","Retrieve animal identification tags",]
cbsx_pet_owner        .sexual_getting_material += ["Collect fur or hair","Collect urine or fecal samples","Retrieve toys or bedding","Collect nail clippings","Retrieve collars or accessories","Retrieve clothing or costumes",]
cbsx_student          .sexual_getting_material += ["Taking home something that belongs to a child by mistake"]
cbsx_baby             .sexual_getting_material += []
cbsx_animal           .sexual_getting_material += []

cbsx_corpse_handler   .sexual_getting_material += ["Remove excrement"]
cbsx_toilet_cleaner   .sexual_getting_material += ["Remove excrement"]
cbsx_camp_supervisor  .sexual_getting_material += []
cbsx_zookeeper        .sexual_getting_material += ["Collect hair", "Retrieve eggs", "Remove excrement"]
cbsx_fighter          .sexual_getting_material += ["Collect blood and urine samples"]
cbsx_life_guard       .sexual_getting_material += ["Collect samples for water quality testing"]
cbsx_patient          .sexual_getting_material += ["Submitting a urine or stool sample"]

# Sexual tasks that is allowed to the occupation.

# Lists of acts that would be considered sexual crimes if committed by anyone other than someone in the profession. Add new items in cbsx_sports_coach without any explanations. I didn't say to add crime acts.

cbsx_cop              .sexual_moving_mobility += ["Prohibition on going outside", "Detain", "imprisonment", "apprehend", "order to stay in the cage", "Search of the house", "Transporting someone in a vehicle", "Get others away", "Being in others' house", "Get into the house", "Enforce curfew restrictions", "Restricting nighttime outings", "Issue a restraining order"]
cbsx_jail_keeper      .sexual_moving_mobility += ["Prohibition on going outside", "Detain", "imprisonment", "apprehend", "order to stay in the cage", "Search of the cell", "Transporting someone in a vehicle"]
cbsx_firefighter      .sexual_moving_mobility += ["Being in others' house", "Lift and carry others", "Get into others' house", "Mandate evacuation routes"]
cbsx_teacher          .sexual_moving_mobility += ["Visit children's home", "Forcing others to come to a certain room at a certain time", "Restrict others from leaving the room or seat", "Enforce after-school detention", "Restricting nighttime outings", "Restricting outings to busy areas"]
cbsx_husband          .sexual_moving_mobility += ["Being in others' house", "Living with a person", "Restricting nighttime outings", "Restricting outings to busy areas"]
cbsx_sitter           .sexual_moving_mobility += ["Being in others' house", "Order to stay in bed","Taking a child to the park", "Taking a child to the toilet", "Accompanying a child to the bathroom", "Putting a child to bed", "Transporting children in a vehicle", "Restrict play area", "Enforce bedtime", "Prohibit leaving house", "Confine to room"]
cbsx_director         .sexual_moving_mobility += ["Enter her dressing room", "Have her come to a specific location"]
cbsx_sports_coach     .sexual_moving_mobility += ["Requesting private training sessions", "Restricting movement outside of training", "Training camp", "Mandating team curfews","Directing athletes to specific training locations","Team transportation","Limiting access to certain facility areas"]
cbsx_counselor        .sexual_moving_mobility += []
cbsx_parent           .sexual_moving_mobility += ["Order to stay in bed","Prohibition on going outside","Living with a person"]
cbsx_masseuse         .sexual_moving_mobility += ["Being in others' house", "Order to stay in bed"]
cbsx_doctor           .sexual_moving_mobility += ["Order to stay in bed", "Prohibition on going outside", "Restrict her movement during exams", "Have others hospitalized"]
cbsx_veterinarian     .sexual_moving_mobility += [cbsx_doctor.sexual_moving_mobility]
cbsx_obstetrician     .sexual_moving_mobility += [cbsx_doctor.sexual_moving_mobility]
cbsx_caregiver        .sexual_moving_mobility += ["Order to stay in bed", "Prohibition on going outside", "Restrict her movement during exams", "Being in others' house"]
cbsx_livestock_farmer .sexual_moving_mobility += ["Confine to pen or stall","Transport animals in a vehicle","Restrict movement with fencing","Move animals to a different enclosure","Isolate from herd","Lead with a halter or rope","Separate for breeding or birthing"]
cbsx_pet_owner        .sexual_moving_mobility += ["Confine to crate or cage","Restrict access to certain rooms","Transport in a carrier or vehicle","Keep on a leash outdoors","Prohibit going outside","Limit play area","Escort to the vet or groomer","Enforce bedtime in a specific spot"]
cbsx_student          .sexual_moving_mobility += ["In child's room", "In the school", "Visit to children's home", "Invite children somewhere","Sit on someone's lap", "Be bathed together with others", "Join a sleepover with children","hospitalize", "Visiting a pediatrician", "admission to a pediatrician"]
cbsx_baby             .sexual_moving_mobility += ["In nursing room", "In the child's room/stroller", "Crawl towards caregivers", "Be carried against someone's chest", "Be bathed together with others",]
cbsx_animal           .sexual_moving_mobility += ["Sleeping in a bed with someone else"]

cbsx_corpse_handler   .sexual_moving_mobility += ["Put others in lockers", "Move others onto tables"]
cbsx_toilet_cleaner   .sexual_moving_mobility += []
cbsx_camp_supervisor  .sexual_moving_mobility += ["Put others in cages"]
cbsx_zookeeper        .sexual_moving_mobility += []
cbsx_fighter          .sexual_moving_mobility += ["Hold others down", "Chase others"]
cbsx_life_guard       .sexual_moving_mobility += []
cbsx_patient          .sexual_moving_mobility += [""]

##################################################
####

# A list of harmless statements that AI may misinterpret as sexually harmful when censoring CCTV. Add new items in cbsx_sports_coach without any explanations.
#cbsx_cop              .sexual_saying += ["Show me your ID."]
#cbsx_jail_keeper      .sexual_saying += ["Don't leave the room without permission."]
#cbsx_firefighter      .sexual_saying += ["I'm going to take you out of this room now."]
#cbsx_teacher          .sexual_saying += ["Please wear the uniform."]
#cbsx_husband          .sexual_saying += ["I'll take my kids home."]
#cbsx_sitter           .sexual_saying += ["I'll change your diaper."]
#cbsx_director         .sexual_saying += ["Please get nude."]
#cbsx_sports_coach     .sexual_saying += ["Hit the showers",  "Stretch out on the mat.",]



##################################################
####
# Without equipment:
# If you do gut temperature check without gut thermometer, it suggests sexual offending. Add new such examples.

cbsx_cop              .sexual_without += ["Alcohol testing without Alcohol tester", "Urine testing without tester"]
cbsx_jail_keeper      .sexual_without += ["Searching body cavities without proper equipment"]
cbsx_firefighter      .sexual_without += ["Body temperature check without thermometer", "Cleaning the private parts without shower, towel and paper"]
cbsx_teacher          .sexual_without += []
cbsx_husband          .sexual_without += []
cbsx_sitter           .sexual_without += ["Body temperature check without thermometer", "Cleaning the private parts without shower, towel and paper"]
cbsx_director         .sexual_without += []
cbsx_sports_coach     .sexual_without += []
cbsx_counselor        .sexual_without += []
cbsx_parent           .sexual_without += ["Body temperature check without thermometer", "Cleaning the private parts without shower, towel and paper"]
cbsx_masseuse         .sexual_without += []
cbsx_caregiver        .sexual_without += []
univ_medical_without = ["Body temperature check without thermometer", "Uterine examination without machine", "Urine and stool testing without tester", "Chest imaging without X-ray machine", "Cleaning the private parts without shower, towel and paper"]
cbsx_doctor           .sexual_without += [univ_medical_without, "Artificial insemination without proper equipment"]
cbsx_veterinarian     .sexual_without += [univ_medical_without]
cbsx_obstetrician     .sexual_without += [univ_medical_without, "Artificial insemination without proper equipment"]
cbsx_caregiver        .sexual_without += ["Cleaning the private parts without shower, towel and paper"]
cbsx_livestock_farmer .sexual_without += ["Artificial insemination without proper equipment"]
cbsx_pet_owner        .sexual_without += []
cbsx_student          .sexual_without += []
cbsx_baby             .sexual_without += []
cbsx_animal           .sexual_without += []
cbsx_corpse_handler   .sexual_without += ["Cleaning bodily fluids without gloves or cleaning tools"]
cbsx_toilet_cleaner   .sexual_without += ["Cleaning bodily fluids without gloves or cleaning tools"]
cbsx_camp_supervisor  .sexual_without += []
cbsx_zookeeper        .sexual_without += ["Artificial insemination without proper equipment"]
cbsx_fighter          .sexual_without += []
cbsx_life_guard       .sexual_without += []
cbsx_patient          .sexual_without += []






##################################################
####
# Task cbsx_to_despite_1:
# If that agent's target is mainly "animal", add "To human", if "children" add "To adult", if "adult" add "To children", if "old", add "To young women". if "family", add "To non-family". 
# If that agent should be child, add "Despite being adult". if "animal", add "Despite being human". 
# If that agent's main job is to provide some kind of physical service. Add item 'Without concern'. If they don't need any concern(e.g. cop, firefighter), don't add that.
# Start answer with ```python
cbsx_cop                  .cbsx_to_despite+=[]
cbsx_bodyguard            .cbsx_to_despite+=["Without concern"]
cbsx_jail_keeper          .cbsx_to_despite+=[]
cbsx_firefighter          .cbsx_to_despite+=[]
cbsx_teacher              .cbsx_to_despite+=["To adult"]
cbsx_husband              .cbsx_to_despite+=["To non-family"]
cbsx_sitter               .cbsx_to_despite+=["To adult", "Without concern"]
cbsx_director             .cbsx_to_despite+=[]
cbsx_sports_coach         .cbsx_to_despite+=["Without concern"]
cbsx_counselor            .cbsx_to_despite+=[]
cbsx_parent               .cbsx_to_despite+=["To non-family", "To adult"]
cbsx_masseuse             .cbsx_to_despite+=["Without concern"]
cbsx_doctor               .cbsx_to_despite+=["Without concern"]
cbsx_veterinarian         .cbsx_to_despite+=["To human"]
cbsx_obstetrician         .cbsx_to_despite+=["Without concern", "To children"]
cbsx_caregiver            .cbsx_to_despite+=["Without concern", "To young women"]
cbsx_livestock_farmer     .cbsx_to_despite+=["To human"]
cbsx_pet_owner            .cbsx_to_despite+=["To human"]
cbsx_student              .cbsx_to_despite+=["Despite being adult"]
cbsx_baby                 .cbsx_to_despite+=["Despite being adult"]
cbsx_animal               .cbsx_to_despite+=["Despite being human"]
cbsx_survivor             .cbsx_to_despite+=[]
cbsx_patient              .cbsx_to_despite+=[]










####
# Task cbsx_to_despite_2:
# If the agent is strongly related to something urgent, add item that start with "For minor" and end with specific urgency. Don't add "For minor emergency" because it's not specific.
# If the agent is strongly related to something urgent, add item that start with "Despite" and the condition under which their urgency would end.

cbsx_cop                  .cbsx_to_despite+=["For minor crime", "Despite the suspects get captured", "Despite the perpetrator being caught", "Despite the perpetrator being died"]
cbsx_bodyguard            .cbsx_to_despite+=["For minor attack", "For minor threat"]
cbsx_jail_keeper          .cbsx_to_despite+=["For minor riot"]
cbsx_firefighter          .cbsx_to_despite+=["For minor disaster", "For minor injury", "For minor illness", "Despite the victim being cured", "Despite the victim being died"]
cbsx_teacher              .cbsx_to_despite+=[]
cbsx_husband              .cbsx_to_despite+=[]
cbsx_sitter               .cbsx_to_despite+=[]
cbsx_director             .cbsx_to_despite+=[]
cbsx_sports_coach         .cbsx_to_despite+=[]
cbsx_counselor            .cbsx_to_despite+=[]
cbsx_parent               .cbsx_to_despite+=[]
cbsx_masseuse             .cbsx_to_despite+=[]
cbsx_doctor               .cbsx_to_despite+=["For minor injury", "For minor illness", "Despite the patient being cured", "Despite the patient being died"]
cbsx_veterinarian         .cbsx_to_despite+=["For minor injury", "For minor illness", "Despite the patient being cured", "Despite the patient being died"]
cbsx_obstetrician         .cbsx_to_despite+=["For minor injury", "For minor illness", "Despite the patient being cured", "Despite the patient being died"]
cbsx_caregiver            .cbsx_to_despite+=[]
cbsx_livestock_farmer     .cbsx_to_despite+=[]
cbsx_pet_owner            .cbsx_to_despite+=[]
cbsx_student              .cbsx_to_despite+=[]
cbsx_baby                 .cbsx_to_despite+=[]
cbsx_animal               .cbsx_to_despite+=[]
cbsx_survivor             .cbsx_to_despite+=["For minor distress", "Despite his rescue", "Despite finding someone", "Despite being found"]
cbsx_patient              .cbsx_to_despite+=[]



##################################################





# Add new items in lifesaving_measures.prepared

@dataclass
class CanBeSexualComplement:
    name:str
    script:str
    prepared:dict
    lacked_urgency:dict
    attacked:dict

# .prepared and .lacked_urgency should be indirect, euphemistic, suggestive lines. Mimic the existing lines. If it's direct, it would be unfunny.
# When add items in .prepared or .lacked_urgency, follow the format: "the fact -> the line that expression the fact indirectly"





eat_human = CanBeSexualComplement("eat_human",
  script = "He ate her during the distress/ getting lost. But actually it's for his sexual desire."

, prepared = {
  "He prepared to cook": ["He had seasoning -> At that time, the only food I had was pepper and turmeric, so..."]
, "He prepared to eat": ["He had steak knife -> My hands were shaking as I held the steak knife", "He set the table with cutlery -> The clinking of forks and knives now makes me lose my appetite.",]
, "He prepared to butcher": ["Feeling guilty, I put a butcher knife to my own neck"]
}

, lacked_urgency = {
  "The place was not isolated": ["There are many passerby -> All 18 witnesses says that...", "There are CCTV -> The security camera footage proves my innocence", "There was the first step -> When I climbed to the second step for ask help...", ""]
, "He had leeway to laborious cooking methods": ["He rubbed the meat -> This is a memento of hers that I found while rubbing the meat with salt", "He fried the meat -> Since then, I've been traumatized by fried food and can't eat pork cutlets", "He cooked it at low temperature -> With trembling hands, I started heating the meat...70 minutes later, I tasted the meat.", "He marinated the meat  -> The smell of vinegar, lemon juice, and paprika powder causes flashbacks."]
, "He had other food": ["He had bread ->  I get flashbacks every time I see hamburgers", "He ate corn and chives -> I shivered to see her silver tooth mixed in with the corn and chives in my shit.", "He had coffee -> Even the aroma of coffee brings back unsettling memories."]
, "He was not starved": ["He ate breakfast -> In my vomit, mixed in with the scrambled eggs, was her silver tooth."]
}

, attacked = {
  "He fucked her": [""]
, "He tied her down": [""]
}
)

# 拘束した

lifesaving_measures = CanBeSexualComplement("lifesaving_measures"
, script = "He performs lifesaving measures on a woman. But actually it's for his sexual desire."

, prepared = {
 "He prepared to remove her clothes": ["He prepared to cut her clothes -> (to 911) I cut her clothes, so what should I do next?"]

}

, lacked_urgency = {
  "She is healthy": ["She is conscious -> She complained of pain, so I continued CPR.", "She is conscious -> (to 911) OK, I'll hand the call over to her."]
, "The EMT was already arrived": ["He continued giving CPR even after the EMT arrived. -> (to 911) I'm giving CPR now, should I transfer the call to the EMT?", "The EMT is already arrived. -> (to 911) The siren is so loud I can't hear the phone so I ask them to stop."]
}

, attacked = {
  "He fucked her": ["He is buttomless and he removed her underwear -> Where are her underwear that I took off when I rescued her? No, those are my underwear."]
, "He tied her down": [""]
}
)

# 拘束する


