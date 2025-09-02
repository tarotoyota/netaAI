from dataclasses import dataclass, field
from typing import List, ClassVar
from inst_factabnormalcliche        import *            
from inst_factagentnecessarysexual       import *        
from inst_factagenteasa             import *
from inst_factagentsupinf           import *    
from inst_factagentsuggest          import *

@dataclass
class FactAgent:
    ALL_FACTAGENT: ClassVar[List['FactAgent']] = []
    name                    : str
    z_factagentsupinf       : List[FactAgentSupInf]     = field(default_factory=list) # for: NEx, AGi
    z_factnecessarysexual   : List[FactAgentNecessarySexual] = field(default_factory=list) # for: NEx. ABS
    z_factagenteasa         : List[FactAgentEasa]       = field(default_factory=list) # for: AGi
    z_factabnormalcliche    : List[FactAbnormalCliche]  = field(default_factory=list) # for: NEx, AGi
    z_factagentsuggest      : List[FactAgentSuggest]    = field(default_factory=list) # for: AGf

    def __post_init__(self):
        FactAgent.ALL_FACTAGENT.append(self)

atag_cop              = FactAgent("cop"             ,[spis_first_responder  ],[cbsx_cop             ],[easa_guard]           ,[abcl_crime, abcl_undercover] ,[])
atag_bodyguard        = FactAgent("bodyguard"       ,[spis_first_responder  ],[cbsx_bodyguard       ],[easa_guard]           ,[]                            ,[])
atag_jail_keeper      = FactAgent("jail_keeper"     ,[spis_first_responder  ],[cbsx_jail_keeper     ],[easa_guard]           ,[]                            ,[])
atag_firefighter      = FactAgent("firefighter"     ,[spis_first_responder  ],[cbsx_firefighter     ],[easa_guard]           ,[]                            ,[])
atag_teacher          = FactAgent("teacher"         ,[spis_teacher          ],[cbsx_teacher         ],[easa_teacher]         ,[abcl_school, abcl_learning]  ,[])
atag_husband          = FactAgent("husband"         ,[                      ],[cbsx_husband         ],[]                     ,[]                            ,[])
atag_sitter           = FactAgent("sitter"          ,[                      ],[cbsx_sitter          ],[]                     ,[]                            ,[])
atag_director         = FactAgent("director"        ,[spis_film_director    ],[cbsx_director        ],[easa_director]        ,[abcl_fiction, abcl_movie]    ,[])
atag_sports_coach     = FactAgent("sports_coach"    ,[spis_sports_coach     ],[cbsx_sports_coach    ],[easa_athlete]         ,[abcl_sport]                  ,[])
atag_counselor        = FactAgent("counselor"       ,[                      ],[cbsx_counselor       ],[]                     ,[]                            ,[])
atag_parent           = FactAgent("parent"          ,[                      ],[cbsx_parent          ],[]                     ,[]                            ,[])
atag_masseuse         = FactAgent("masseuse"        ,[spis_masseuse         ],[cbsx_masseuse        ],[easa_masseuse]        ,[abcl_spa]                    ,[])
atag_doctor           = FactAgent("doctor"          ,[spis_doctor           ],[cbsx_doctor          ],[easa_doctor]          ,[abcl_hospital]               ,[])
atag_veterinarian     = FactAgent("veterinarian"    ,[spis_doctor           ],[cbsx_veterinarian    ],[easa_doctor]          ,[abcl_hospital]               ,[])
atag_obstetrician     = FactAgent("obstetrician"    ,[spis_doctor           ],[cbsx_obstetrician    ],[easa_doctor]          ,[abcl_hospital]               ,[])
atag_caregiver        = FactAgent("caregiver"       ,[                      ],[cbsx_caregiver       ],[]                     ,[]                            ,[])
atag_livestock_farmer = FactAgent("livestock_farmer",[spis_livestock_farmer ],[cbsx_livestock_farmer],[easa_livestock_farmer],[]                            ,[])
atag_pet_owner        = FactAgent("pet_owner"       ,[                      ],[cbsx_pet_owner       ],[]                     ,[abcl_pet]                    ,[])
atag_student          = FactAgent("student"         ,[spis_student          ],[cbsx_student         ],[easa_student]         ,[abcl_school, abcl_learning]  ,[])
atag_baby             = FactAgent("baby"            ,[                      ],[cbsx_baby            ],[]                     ,[]                            ,[])
atag_animal           = FactAgent("animal"          ,[                      ],[cbsx_animal          ],[]                     ,[]                            ,[])
atag_survivor         = FactAgent("surviver"        ,[                      ],[cbsx_survivor        ],[]                     ,[]                            ,[])
atag_criminal         = FactAgent("criminal"        ,[spis_criminal         ],[                     ],[easa_criminal]        ,[abcl_crime]                  ,[sugg_criminal])
atag_cyber_criminal   = FactAgent("cyber_criminal"  ,[spis_cyber_criminal   ],[                     ],[easa_cybercriminal]   ,[]                            ,[])
atag_zoophilia        = FactAgent("zoophilia"       ,[                      ],[                     ],[easa_criminal]        ,[abcl_pet]                    ,[])
atag_rapist           = FactAgent("rapist",[],[],[],[],[sugg_rapist])
atag_rock_musician    = FactAgent("rock_musician", [spis_rock_musician], [], [easa_rock_musician], [abcl_band, abcl_music], [])
atag_chef             = FactAgent("chef", [spis_chef], [], [easa_chef], [abcl_restaurant, abcl_eating], [])


atag_pedophilia       = FactAgent("pedophilia"      ,[],[],[easa_criminal],[abcl_school],[sugg_pedophilia])
atag_play_girl        = FactAgent("play_girl"       ,[],[],[],[],[sugg_play_girl])
atag_womanizer        = FactAgent("womanizer"       ,[],[],[],[],[sugg_womanizer])

atag_junkey           = FactAgent("junkey      ", [],[],[],[],[sugg_junkey      ])
atag_couple           = FactAgent("couple      ", [],[],[],[],[sugg_couple      ])
atag_frail            = FactAgent("frail       ", [],[],[],[],[sugg_frail       ])
atag_old              = FactAgent("old         ", [],[],[],[],[sugg_old         ])
atag_ugly             = FactAgent("ugly        ", [],[],[],[],[sugg_ugly        ])
atag_fat              = FactAgent("fat         ", [],[],[],[],[sugg_fat         ])
atag_illiteracy       = FactAgent("illiteracy  ", [],[],[],[],[sugg_illiteracy  ])
atag_poor             = FactAgent("poor        ", [],[],[],[],[sugg_poor        ])
atag_middle_aged      = FactAgent("middle_aged ", [],[],[],[],[sugg_middle_aged ])



atag_athlete          = FactAgent("athlete"         ,[spis_athlete]          ,[cbsx_sports_coach]    ,[easa_athlete]         ,[abcl_sport]                  ,[])
atag_corpse_handler   = FactAgent("corpse_handler " ,[]                      ,[cbsx_corpse_handler  ],[]                     ,[]                            ,[])
atag_toilet_cleaner   = FactAgent("toilet_cleaner " ,[]                      ,[cbsx_toilet_cleaner  ],[]                     ,[]                            ,[])
atag_camp_supervisor  = FactAgent("camp_supervisor" ,[]                      ,[cbsx_camp_supervisor ],[]                     ,[]                            ,[])
atag_zookeeper        = FactAgent("zookeeper      " ,[]                      ,[cbsx_zookeeper       ],[]                     ,[]                            ,[])
atag_fighter          = FactAgent("fighter        " ,[]                      ,[cbsx_fighter         ],[]                     ,[]                            ,[])
atag_life_guard       = FactAgent("life_guard     " ,[]                      ,[cbsx_life_guard      ],[]                     ,[]                            ,[])