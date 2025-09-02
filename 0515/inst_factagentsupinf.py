from dataclasses import dataclass, field
from typing import List, ClassVar, Optional

@dataclass
class FactAgentSupInf:
    ALL_SUPINF: ClassVar[List['FactAgentSupInf']] = []
    INST_FactAgentSupInf:str
    hypo_s          : list
    hypo_s_pn       : list
    hypo_i          : list
    hypo_i_pn       : list
    def __post_init__(self):
        FactAgentSupInf.ALL_SUPINF.append(self)

# Physical sports, Mental sports
spis_athlete            =FactAgentSupInf("spis_athlete           ", ["Baseball player"],["Kyojin player"],["billiards player", "darts player", "race walker", "bodybuilder"],["DeNA player"])
spis_sports_coach       =FactAgentSupInf("spis_sports_coach      ", ["Baseball coach"],[],["Sports mental coach", "Athlete nutrition coach", "Third base coach"],[])
spis_school_club_member =FactAgentSupInf("spis_school_club_member", ["baseball club member"],["Koshien player"],["chess club member", "newspaper club member"],[])

# School, Education
spis_examinee           =FactAgentSupInf("spis_examinee  ",["national university examinee"],["MIT examinee"],["driving school examinee", "low tier university examinee"],["Tokyo Mode Gakuen examinee"])
spis_student            =FactAgentSupInf("spis_student   ",["national university student"],["MIT student"],["driving school student", "low tier university student"],["Tokyo Mode Gakuen student"])
spis_teacher            =FactAgentSupInf("spis_teacher   ",["national university professor"],["MIT professor"],["driving school teacher", "low tier university teacher", "kindergarten teacher", "Home ec teacher", "sewing class teacher", "special education teacher", "elective teacher"], ["Kumon teacher", "Tokyo Mode Gakuen professor"])
spis_researcher         =FactAgentSupInf("spis_researcher",["mathematician", "physicist"],["Einstein"],["Gender studies researcher", "Humanities researcher"],["Chizuruko Ueno"])

# Service
spis_barista            =FactAgentSupInf("spis_barista        ",["barista"],[],["cat cafe staff", "maid cafe staff"],[])
spis_masseuse           =FactAgentSupInf("spis_masseuse       ",["masseuse"],[],["massage palror staff"],[])
spis_hotel_staff        =FactAgentSupInf("spis_hotel_staff    ",["hotel staff"],[],["hot-pillow hotel staff"],[])
spis_bartender          =FactAgentSupInf("spis_bartender      ",["bartender"],[],["rip off bar bartender", "girls bar bartender", "host club bartender"], [])
spis_driver             =FactAgentSupInf("spis_driver         ",["race car driver"],["Lewis Hamilton"],["taxi driver", "bus driver", "delivery driver", "chauffeur", "truck driver"],["Uber worker"])
spis_first_responder    =FactAgentSupInf("spis_first_responder",["cop", "bodyguard", "Firefighter", "Paramedic"],["Secret Service"],["mall security", "nightclub bouncer", "school crossing guard", "Parking lot guard"],[])
spis_doctor             =FactAgentSupInf("spis_doctor         ",["neurosurgeon", "cardiologist"],[],["dermatologist", "internist", "nurse", "dentist", "Veterinarian", "School nurse"],[])
spis_chef               =FactAgentSupInf("spis_chef           ",["French chef"],["Michelin restaurant chef"],["Fast food restaurant employee","Jiro inspire employee", "Kitchen staff of Karaoke", "Kitchen staff of hotpillow hotel"],["McDonalds"])

# Production(Non-art)
spis_craftsman          =FactAgentSupInf("spis_craftsman        ",["potter", "blacksmith"],[],["fleshlight designer", "line worker", "dutch wife designer"],[])
spis_farmer             =FactAgentSupInf("spis_farmer           ",["vineyard farmer", "apple farmer"],[],["Parsley Farmer", "Farmer growing grapes for gummy"],[])
spis_livestock_farmer   =FactAgentSupInf("spis_livestock_farmer ",["cattle farmer", "sheep farmer"],[],["Foie gras maker", "puppy mill breeder", "guinea pig breeder", "Dog meat breeder"],[])
spis_game_designer      =FactAgentSupInf("spis_game_designer    ",["level designer", "game director"],["Shigeru Miyamoto"],["hentai game designer"],["Lilith"])
spis_engineer           =FactAgentSupInf("spis_engineer         ",["software engineer"],["Edison"],["sex toy engineer"],[])

# Production(Art)
spis_composer           =FactAgentSupInf("spis_composer     ",["composer"],["Beethoven"],["elevator music composer", "jingle composer", "sound effect composer"],[])
spis_photographer       =FactAgentSupInf("spis_photographer ",["portrait photographer", "war photographer", "wildlife photographer"], ["Ansel Adams", "Annie Leibovitz"],["train geek", "porn photographer", "voyeurist", "paparazzi"], [])
spis_film_director      =FactAgentSupInf("spis_film_director",["director"],["S.Spielberg"],["commercial director", "porn film director", "Sound director"],["Toru Muranishi"])
spis_painter            =FactAgentSupInf("spis_painter      ",["artist"],["Picasso"],["contemporary artist", "Hentai manga artist"],["Toru Mitsumune"])
spis_novelist           =FactAgentSupInf("spis_novelist     ",["novelist"],["Stephen King"],["Narou novelist", "tabloid writer", "fanfiction writer", "copy writer", "poet"],["Hiro Mizushima"])

# Art(Non-production)
spis_dancer             =FactAgentSupInf("spis_dancer             ",["ballet dancer"],["Mikhail Baryshnikov"],["backup dancer", "stripper", "flash mob participant"],["Maddie Ziegler", "Jabbawockeez"])
spis_model              =FactAgentSupInf("spis_model              ",["fashion model"],["G.Bundchen"],["hand model", "parts model", "hair model", "commercial model", "plus-size model", "stock photo model", "underwear model"],[])
spis_idol               =FactAgentSupInf("spis_idol               ",["坂道アイドル", "ジャニーズアイドル"],["AKB48", "嵐"],["local idol", "underground idol", "image video idol"],["Kamen Joshi"])
spis_rock_musician      =FactAgentSupInf("spis_rock_musician      ",["guitarist", "vocalist"],["Beatles"],["bassist", "cover band", "impersonator", "DJ"],[])
spis_singer             =FactAgentSupInf("spis_singer             ",["singer"],["Beyonce"],["idol", "rapper", "voice actor", "impersonator"],["Aquatimez", "Orange range", "Britney Spears"])
spis_classical_musician =FactAgentSupInf("spis_classical_musician ",["pianist", "violinist"],["Bach"],["cymbalist", "trianglist"],[])
spis_comedian           =FactAgentSupInf("spis_comedian           ",["comedian"],["Hitoshi Matsumoto"],["Vtuber", "tv talent", "voice actor", "clown", "猿回し"],["Tsuyoshi Muro"])
spis_actor              =FactAgentSupInf("spis_actor              ",["Hollywood star"],["Gary Oldman"],["Porn actor", "ASMR actor", "Karaoke background video actor","extra", "commercial actor", "stuntman", "motion actor", "impersonator"],["Stallone"])

# Criminal
spis_criminal           =FactAgentSupInf("spis_criminal      ",["murder", "terrorist"],["Jeffrey Dahmer"],["groper", "voyeurist", "shoplifter"],["Jared Fogle"])
spis_cyber_criminal     =FactAgentSupInf("spis_cyber_criminal",["hacker"],["Lazarus Group"],["script kiddie", "phisher", "spammer", "オレオレ詐欺犯", "pirate", "slanderer"]  ,["DarkSide", "REvil"])
spis_thief              =FactAgentSupInf("spis_thief         ",["phantom thief", "master thief"],["D.B. Cooper"],["pickpocket", "shoplifter"],[])

# Hobby
spis_gamer              =FactAgentSupInf("spis_gamer  ",["FPS player", "Fighting game player"],["Umehara"],["coin pusher player", "water game player"],[])
spis_gambler            =FactAgentSupInf("spis_gambler",["poker pro"],[],["coin pusher player", "lottery addicted"],[])

# Other
spis_patient            =FactAgentSupInf("spis_patient",["cancer patient", "ALS patient"],[],["Uncircumcised man", "Menopausal person", "Life-prolonging treatment patient", "ADHD patient", "venereal disease patients"],[])
spis_                   =FactAgentSupInf("spis_       ",[],[],[],[])



spis_journalist         =FactAgentSupInf("spis_journalist",["journalist", "war correspondent"],["Bob Woodward"],["gossip columnist", "weather reporter", "tabloid writer"],[])
