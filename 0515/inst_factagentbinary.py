from dataclasses import dataclass, field
from typing import List, ClassVar
#from test_output import tablize_attr_and_iv



@dataclass
class FactAgentBinary:
    ALL_FACTAGENTBINARY: ClassVar[List['FactAgentBinary']] = []
    INST_FactAgentBinary:str
    high_intelligence:str
    high_strength:str
    extrovert_introvert:str
    sport:str
    showbiz:str
    art:str
    service:str
    retail:str
    manufacturing:str
    looks_job:str
    not_job:str

    def __post_init__(self):
        FactAgentBinary.ALL_FACTAGENTBINARY.append(self)
    #@staticmethod
    #def tablize():
    #    return tablize_attr_and_iv(FactAgentBinary.ALL_FACTAGENTBINARY)

agbn_                       = FactAgentBinary("agbn_                  ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_cop                    = FactAgentBinary("agbn_cop               ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_bodyguard              = FactAgentBinary("agbn_bodyguard         ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_jail_keeper            = FactAgentBinary("agbn_jail_keeper       ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_firefighter            = FactAgentBinary("agbn_firefighter       ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_teacher                = FactAgentBinary("agbn_teacher           ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_husband                = FactAgentBinary("agbn_husband           ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"y")
agbn_sitter                 = FactAgentBinary("agbn_sitter            ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" )
agbn_director               = FactAgentBinary("agbn_director          ","" ,"" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"" )
agbn_sports_coach           = FactAgentBinary("agbn_sports_coach      ","y","y","e","y","" ,"" ,"" ,"y","" ,"" ,"" )
agbn_counselor              = FactAgentBinary("agbn_counselor         ","y","" ,"e","" ,"" ,"" ,"" ,"y","" ,"" ,"" )
agbn_parent                 = FactAgentBinary("agbn_parent            ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_masseuse               = FactAgentBinary("agbn_masseuse          ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" )
agbn_doctor                 = FactAgentBinary("agbn_doctor            ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_veterinarian           = FactAgentBinary("agbn_veterinarian      ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_obstetrician           = FactAgentBinary("agbn_obstetrician      ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_caregiver              = FactAgentBinary("agbn_caregiver         ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" )
agbn_livestock_farmer       = FactAgentBinary("agbn_livestock_farmer  ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" )
agbn_pet_owner              = FactAgentBinary("agbn_pet_owner         ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_student                = FactAgentBinary("agbn_student           ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_baby                   = FactAgentBinary("agbn_baby              ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_animal                 = FactAgentBinary("agbn_animal            ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_survivor               = FactAgentBinary("agbn_survivor          ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_criminal               = FactAgentBinary("agbn_criminal          ","y","y","e","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_cyber_criminal         = FactAgentBinary("agbn_cyber_criminal    ","y","" ,"i","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_zoophilia              = FactAgentBinary("agbn_zoophilia         ","" ,"" ,"i","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_pedophilia             = FactAgentBinary("agbn_pedophilia        ","" ,"" ,"i","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
#
agbn_rock_musician          = FactAgentBinary("agbn_rock_musician     ","" ,"" ,"e","" ,"y","y","" ,"" ,"" ,"y","" )
agbn_singer                 = FactAgentBinary("agbn_singer            ","" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"y","" )
agbn_classical_musician     = FactAgentBinary("agbn_classical_musician","" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,"" )
agbn_comedian               = FactAgentBinary("agbn_comedian          ","" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,"" )
agbn_novelist               = FactAgentBinary("agbn_novelist          ","y","" ,"i","" ,"" ,"y","" ,"" ,"" ,"" ,"" )
agbn_artist                 = FactAgentBinary("agbn_artist            ","y","" ,"i","" ,"" ,"y","" ,"" ,"" ,"" ,"" )
agbn_researcher             = FactAgentBinary("agbn_researcher        ","y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_actor                  = FactAgentBinary("agbn_actor             ","" ,"" ,"e","" ,"y","y","" ,"" ,"" ,"y","" )
agbn_chef                   = FactAgentBinary("agbn_chef              ","" ,"" ,"" ,"" ,"" ,"" ,"y","y","y","" ,"" )
agbn_athlete                = FactAgentBinary("agbn_athlete           ","" ,"y","e","y","y","" ,"" ,"" ,"" ,"" ,"" )
agbn_violent_criminal       = FactAgentBinary("agbn_violent_criminal  ","" ,"y","e","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_cyber_criminal         = FactAgentBinary("agbn_cyber_criminal    ","y","" ,"i","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_thief                  = FactAgentBinary("agbn_thief             ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_examinee               = FactAgentBinary("agbn_examinee          ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_gambler                = FactAgentBinary("agbn_gambler           ","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_progamer               = FactAgentBinary("agbn_progamer          ","" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" )
agbn_teacher                = FactAgentBinary("agbn_teacher           ","y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_farmer                 = FactAgentBinary("agbn_farmer            ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" )
agbn_livestock_farmer       = FactAgentBinary("agbn_livestock_farmer  ","" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" )
agbn_director               = FactAgentBinary("agbn_director          ","y","" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,"" )
agbn_model                  = FactAgentBinary("agbn_model             ","" ,"" ,"e","" ,"y","" ,"" ,"" ,"" ,"y","" )
agbn_guard                  = FactAgentBinary("agbn_guard             ","" ,"y","e","" ,"" ,"" ,"y","" ,"" ,"" ,"" ) ###
agbn_patient                = FactAgentBinary("agbn_patient           ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_the_dying              = FactAgentBinary("agbn_the_dying         ","", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_school_club_member     = FactAgentBinary("agbn_school_club_member","" ,"y","e","y","" ,"" ,"" ,"" ,"" ,"" ,"" )
agbn_journalist             = FactAgentBinary("agbn_journalist        ","y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_idol                   = FactAgentBinary("agbn_idol              ","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y","" )
agbn_composer               = FactAgentBinary("agbn_composer          ","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" )
agbn_dancer                 = FactAgentBinary("agbn_dancer            ","" ,"y","e","" ,"y","y","" ,"" ,"" ,"y","" )
agbn_barista                = FactAgentBinary("agbn_barista           ","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_masseuse               = FactAgentBinary("agbn_masseuse          ","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_hotel_staff            = FactAgentBinary("agbn_hotel_staff       ","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_craftsman              = FactAgentBinary("agbn_craftsman         ","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" )
agbn_photographer           = FactAgentBinary("agbn_photographer      ","" ,"" ,"" ,"" ,"y","" ,"y","" ,"" ,"" ,"" )
agbn_game_designer          = FactAgentBinary("agbn_game_designer     ","y","" ,"i","" ,"" ,"" ,"" ,"" ,"y","" ,"" )
agbn_engineer               = FactAgentBinary("agbn_engineer          ","y","" ,"i","" ,"" ,"" ,"" ,"" ,"y","" ,"" )
agbn_delinquent             = FactAgentBinary("agbn_delinquent        ","" ,"" ,"e","" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_groper                 = FactAgentBinary("agbn_groper            ","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
agbn_old                    = FactAgentBinary("agbn_old"               ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
