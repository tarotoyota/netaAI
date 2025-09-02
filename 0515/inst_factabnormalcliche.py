from dataclasses import dataclass, field
from typing import List, ClassVar, Optional

@dataclass
class FactAbnormalCliche:
    ALL_ABNORMALCLICHE: ClassVar[List['FactAbnormalCliche']] = []
    INST_FactAbnormalCliche:str
    abn_hypo :list[str] # Abnormal hyponyms or ways, in other words, ones that doesn't come to mind first.
    nor_obj  :list[str] # Cliche elements that doesn't appear in .abn_hypo
    nor_agent:list[str] # Agents who doesn't appear in .abn_hypo
    def __post_init__(self):
        FactAbnormalCliche.ALL_ABNORMALCLICHE.append(self)


# Abnormal hyponyms, in other words, hyponyms that doesn't come to mind first.

abcl_restaurant =FactAbnormalCliche("abcl_restaurant"
                                , ["soup kitchen", "hot pillow hotel kitchen", "Competitive eating", "fast food restaurant"]
                                , ["reservation", "Call the chef and tell him one's opinion of the taste", "YELP review", "Table Manners", "Tipping", "Instagramming food", "Food delivery", "Dress code", "Farm-to-table", "Sommelier recommendation", "Celemony", "Seasonal menu", "Palate cleanser", "Tableside preparation"]
                                , ["Food critic", "Repeat customer"])
abcl_sport      =FactAbnormalCliche("abcl_sport"
                                , ["Billiards", "Table tennis", "Chess", "Judged sports (such as figure skating)"]
                                , ["Team spirit", "Sportsmanship", "Doping", "Half-time show", "Training camp", "Admission by sports recommendation", "rookie draft", "Inter-university competition", "Fan loyalty", "Championship rings", "Athlete sponsorships", "Game day rituals", "Rough play", "Injury"]
                                , ["Hooligan", "Referee", "Coach", "Sports commentator", "Cheerleader", "Team mascot", "Bettor", "Amateur", "Rookie"])
abcl_school     =FactAbnormalCliche("abcl_school"
                                , ["Blind school", "Handicraft class", "Special needs school", "Low-tier university", "Crammer school", "Driving school", "Kindergarten", "Vocational School", "Prep school", "Free school", "Reform school", "Homeschool", "Online university", "Night school"]
                                , ["Ronin", "Boarding", "Repeat a degree", "Alumni visit", "Hazing", "School club activity", "Cheating on exam", "Boarding", "deviation value", "Alumni association", "Prom night", "Prohibition of heterosexual relations", "Uniform", "Dress code", "Bullying", "Fighting", "Mixed relations", "Sex education", "Suspension", "Delinquent", "Student activity", "class observation day", "Stool and urine tests", "three-year system", "dropout", "vandalism", "School festival", "Entrance ceremony", "Graduation ceremony", "Field trip", "Parent-teacher conference", "School newspaper", "Student council", "Detention", "Honor roll", "Perfect attendance award", "Detention", "Study abroad", "Entrance exam"]
                                , ["Bully/ Bullied", "School shooter", "Ronin", "Repeated student", "Drill sergeant", "Delinquent", "Student activist", "Senior/ Junior", "Reserve player"])

abcl_school.nor_obj += ["下駄箱にラブレターを入れる","喧嘩をするために校舎裏に呼び出す","教師に逆らう","友達と放課後に遊ぶ","授業中に寝る","好きな人に告白する","友達と一緒に昼食を食べる","バレンタインにチョコを渡す","友達を介して好きな人にメッセージを送る","放課後に好きな人とデートする","転校", "喧嘩", "好きな子の隣の席になれて嬉しい"]

# 正攻法 クーデター->選挙 強盗->就職

abcl_copyright_infringement = FactAbnormalCliche("abcl_copyright_infringement"
                                , ["Memorization", "Re-enactment/ Reproduce", "Mimic/ Inpersonate"]
                                , ["Sell"]
                                , [])

abcl_tourist_spot = FactAbnormalCliche("abcl_tourist_spot"
                                , ["The Atomic Bomb Dome", "Auschwitz concentration camp"]
                                , ["Selfie", "View from the hotel","Postcard", "Stamp rally / Passport stamping", "Overpriced bottled water", "Souvenir photo with mascot", "Tourist trap shop", "propose", "VR reenactment attraction", "Picnic"]
                                , ["Tour guide", "Pickpocket", "Street vendor", "Photographer-for-hire", "Scammer", "Backpacker", "Honeymoon couple", "Local tout", "Street performer"])

abcl_deadbody = FactAbnormalCliche("abcl_deadbody"
                                , ["Lenin's corpse", "The corpses of my family", "bone", "meat", "Freshly dead corpses", "The corpse of the person who died protecting me", "Mummy", "Medical school cadaver", "Incorruptibility"]
                                , ["Disgusted by corpses", "Fear of corpses", "Vomiting at the sight of a corpse", "Call the police", "Mosaic", "Post to the YNC",  "Body bag", "Chalk outline",]
                                , ["coroner"])

abcl_stigmatized_property = FactAbnormalCliche("abcl_stigmatized_property"
                                , ["The Atomic Bomb Dome", "Auschwitz concentration camp", "Lenin's Mausoleum", "Gettysburg Battlefield", "Pyramid", "Church with an incorruptibility"]
                                , ["Obligation to disclose", "Declining rents and land prices", "Test of courage", "TV documentary crew visit", "Complaints from neighbors," "Building demolition", "Ghost story retold as urban legend", "Religious ritual", "‘Too cheap to be true’ deals"]
                                , ["YouTuber investigating haunted spots","Paranormal investigator","Medium / exorcist","Thrill-seeking tourist"])










abcl_eating     =FactAbnormalCliche("abcl_eating"
                                , ["Gastrostomy", "Cannibalism during disasters", "Bone-chewing culture at funerals", "Communion", "Funeral feasts", "School meals", "Competitive eating", "Mukbang", "Food challenges on social media"]
                                , [abcl_restaurant.nor_obj, "Refills", "Table condiments", "Detailed orders", "Vegan menu", "Calorie counting", "Cheat day", "Takeout" ]
                                , [abcl_restaurant.nor_agent])

abcl_learning = FactAbnormalCliche("abcl_learning"
                                , ["Home ec", "Sex education"]
                                , ["listening questions", "Practical exam", "cramming", "Oral reading", "written questions", "oral questions", "essay questions", "passive listening study", "sleep learning", "flashcards", "Audio flashcards", "multiple-choice exam (mark sheet method)", "quiz", "cram school", "mnemonic song", "memory stickers"]
                                , ["Tiger parent", "Tutor"])

abcl_comedian   =FactAbnormalCliche("abcl_comedian"
                                , ["clown"]
                                , ["podcast", "f-word", "solo concert", "peform at the comedy club", "roast battle", "open mic night", "improv show", "heckler management", "punchline delivery", "crowd work", "comedic timing", "stand-up special", "callback joke", "comedy writing workshop", "joke book", "comedy tour"]
                                , ["Plagiarist", "Hater", "Follower"])
abcl_fiction    =FactAbnormalCliche("abcl_fiction"
                                , ["fan fiction", "choose your own adventure", "hentai novel", "self-insert character", "hentai comic", "history book", "Paper storytelling", "ASMR"]     
                                , ["spoil", "fan fiction", "analyze"]
                                , ["critic", "fan artist", "analyzer"])
abcl_music      =FactAbnormalCliche("abcl_music"
                                , ["free music", "elevator music", "Jingle", "Covered music", "Nursery rhymes"]                                                                           
                                , ["Music video", "Dance", "Live performance", "Music festival", "Remix"]
                                , ["Remixer"])
abcl_band       =FactAbnormalCliche("abcl_band"
                                , ["Cover band", "Choir", "Marching band", "Wedding band", "Military band", "School band", "Backing band", abcl_music.abn_hypo]
                                , [abcl_music.nor_obj, "encore", "merchandise", "fan club", "cover band", "plagiarism", "MC time", "Have sex with their fans", "Autograph session", "Stage dive", "Music video", "Reunion", "Creative differences"]
                                , ["Impersonator", "Groupie", "Cover band"])
abcl_hotel      =FactAbnormalCliche("abcl_hotel"
                                , ["capsule hotel", "hot-pillow hotel", "Internet cafe"]
                                , ["Room service", "Concierge service", "Complimentary breakfast", "Loyalty programs", "Have sex", "Hotel amenities", "Valet parking", "Business center","Spa services","Room upgrades","Massage service","dress code"]
                                , ["Concierge", "Housekeeper", "Bellhop"])
abcl_crime      =FactAbnormalCliche("abcl_crime"
                                , ["Cousin marriage", "Art forgery", "Grave robbing"]
                                , ["Rapping about their crime", "voluntary surrender", "shootout with police", "Death sentence", "torture", "Gang team", "Bribing a public official", "Lynching", "Fleeing the country", "Undercover operation", "Taking hostages in order to gain innocence"]
                                , ["Bounty hunter","Undercover cop","Crime boss","Gang member","Wanted criminal", "Juvenile offender"])

abcl_fashion    =FactAbnormalCliche("abcl_fashion"
                                , ["underwear", "sexual costumes"]                                                                                                                        
                                , ["Fashion show","Trend","Seasonal collections","Catwalk models","Style guide","Fashion faux pas", "Fake branded goods"]
                                , ["Fashion influencer", "Model", "Fashion photographer", "Fashion critic"])
abcl_lover      =FactAbnormalCliche("abcl_lover"
                                , ["prostitute", "arranged marriage", "rape victim", "mail-order bride","sugar daddy/sugar baby relationship","polyamorous relationship","open relationship","green card marriage","virtual reality dating","AI companion relationship","age-gap relationship (with significant age difference)","relationship with a fictional character"]
                                , ["propose", "dating", "cheating", "blind date", "long-distance relationship", "double date", "anniversary celebration", "meeting the parents", "marriage", "rut", "romantic getaway", "public display of affection", "surprise", "breakup", "swapping", "fight", "make-up after fight"]
                                , ["Cheat mate", "Matchmaker","Wingman","Ex-partner","Love rival","Relationship counselor","Wedding planner","Divorce lawyer","Couples therapist","Dating coach"])
abcl_undercover =FactAbnormalCliche("abcl_undercover"
                                , ["Ab illegal prostitution group", "A restaurant violating the Food Sanitation Act", "Unlicensed daycare center"]                                         
                                , ["Torture", "Wire tapping", "Surveillance", "Code names", "Safe house", "Dead drop", "Disguise", "Encrypted communication", "Blackmail", "Bribery", "False identity", "Covert photography", "Stake out", "Tailing suspect", "Interrogation", "Sting operation", "Witness protection"]
                                , ["Double-cross", "Double Agent", "Informant", "Whistleblower"])
abcl_spa        =FactAbnormalCliche("abcl_spa"
                                , ["FKK", "Massage parlor", "Soap land"]                                                                                                                  
                                , ["Massage", "Facial treatment", "Body scrub", "Meditation session", "Skin care consultation", "Fitness classes", "Couples massage", "Yoga instruction", "Accommodation package"]
                                , ["Wellness coach", "Yoga instructor"])
abcl_gamble     =FactAbnormalCliche("abcl_gamble"
                                , ["coin pusher", "lottery", "bingo", "raffle"]
                                , ["Bluff", "Online casino", "Shark rates", "Underground casino", "Bunco", "Data analyze", "VIP lounge"]
                                , ["Tipster", "Bookie", "High roller", "Gamblaholic", "Bust", "Bankrupt", "Colluder/ Ring"])
abcl_hospital   =FactAbnormalCliche("abcl_hospital"
                                , ["cosmetic surgery", "ED clinic", "phimosis clinic", "dental clinic", "School nurse's office", "mental hospital", "Veterinary Clinic"]
                                , ["Home health care", "Blood work", "Testament", "Visitation", "Praying patient", "Emergency case", "Inpatient", "Triage", "Rounds", "Code blue", "Organ donation", "Urine and stool tests", "Palpation", "Surgery", "Will", "Anesthesia", "Medical malpractice", ]
                                , ["Chaplain", "Inpatient", "Praying family", "Visitor", "Baseball player promising a home run", "Quack Doctor"])
abcl_game       =FactAbnormalCliche("abcl_game"
                                , ["rock paper scissors", "escape room", "idle game", "Eroge", "Virtual pet simulation", "Tabletop RPGs", "Chess"]                                                                                
                                , ["tournament", "rage", "voice chat" ,"Escape room", "Cheat code", "Tier sheet", "Smurfing", "Pay to Win", "Professional league", "Lag",  "Toxic chat",  "speedrunner",]
                                , ["cheater", "streamer", "Cheater", "Pro gamer", "shoutcaster"])
abcl_movie      =FactAbnormalCliche("abcl_movie"
                                , ["porn", "Karaoke background movie", "commericial"]                                                     
                                , [abcl_fiction.nor_obj, "Ad-lib", "Red carpet premiere", "Oscar nomination", "Sequel", "Prequel", "Director's cut", "Behind the scenes", "Audio commentary", "Foreshadowing", "Theme song", "Plot twist","Cliffhanger ending","Easter eggs","Post-credits scene","Product placement","Cameo appearance","Montage sequence","Flashback","Voice-over narration","Green screen effects"]
                                , [abcl_fiction.nor_agent])
abcl_death      =FactAbnormalCliche("abcl_death"
                                , ["murder", "sweetdeath", "suicide", "natural death", "execution"]
                                , ["cheerful funeral", "ghostly visitation", "the grieving widow/widower", "life flashing before eyes", "Curse of the Dead"]
                                , ["grieving family member", "necromancer", "Ghost"])
abcl_pet        =FactAbnormalCliche("abcl_pet"
                                , ["Robotic pet","Miniature pig","Snake","Insect"]
                                , ["Pet show","Pet cafe","Pet adoption event","Culling","Pet store","Pet grooming","Breeding","Obedience training","Pet insurance","Pet hotel","Walking the pet","Scratching post","Chew toy","Kennel club","Pet food","Lost pet poster","Microchipping","Pet vaccination","Pet loss","Pet funeral", "Pet abuse", "Pet welfare"]
                                , ["Veterinarian","Pet walker","Pet sitter","Animal shelter worker","Pet groomer","Pet store clerk","Animal trainer","Breeder","Rescue volunteer"])
abcl_meat       =FactAbnormalCliche("abcl_meat"
                                , ["Lab-grown meat","Insect protein","Cultured meat","Roadkill cuisine","Exotic game meat","Human flesh","Fugu liver sashimi","Horse meat sashimi","Dog meat",]
                                , ["Barbecue","Steakhouse","Meat locker","Charcuterie board","Gravid meat", "Sausage making","Marbling","Aging beef","Smoke","Meat thermometer","Carving station","Meat raffle",]
                                , ["Butcher","Rancher","Slaughter","Meat inspector","Chef","Grill master","Meat packer","Charcutier","Livestock farmer"])
#abcl_sexual     =FactAbnormalCliche("abcl_sexual"
#                                , ["Pistil/ Stamen", "Animal mating", "Sperm/ Egg", "Pollen", "Artificial insemination"]
#                                , ["Porn", "Strip", "Imagine to jerk off", "Use as a jerk-off material", "POV","Safe sex","Foreplay","Afterglow","One-night stand","Sexual consent","Sex education","Casual relationship","Swapping","Hentai manga", "Doujin ASMR", "Sex toy", "Cheating", "First sexual intercourse", "Foreplay", ]
#                                , ["Sex worker","Porn actor","Pickup artist","Sex educator","Swinger","Brothel manager","Matchmaker","Sex toy designer", "Dating coach"])
abcl_have_sex   =FactAbnormalCliche("abcl_have_sex"
                                , ["Car sex", "Rape", "Telephone sex", "Sexting", "Group sex", "Sexual roleplay", "Matsurbation", "Prostitution"]
                                , ["Porn", "Strip", "Imagine to jerk off", "Use as a jerk-off material", "POV","Safe sex","Foreplay","Afterglow","One-night stand","Sexual consent","Sex education","Casual relationship","Swapping","Hentai manga", "Doujin ASMR", "Sex toy", "Cheating", "First sexual intercourse", "Foreplay", ]
                                , ["Sex worker","Porn actor","Pickup artist","Sex educator","Swinger","Brothel manager","Matchmaker","Sex toy designer", "Dating coach"])


abcl_vehicle = FactAbnormalCliche(
    "abcl_vehicle",
     ["Train", "Bus", "lunar rover", "Test drive", "tuk-tuk", "Bike", "ambulance", "Hearse", "Taxy", "Ice cream truck", "Armored car", "Limousine", "Monster truck", "Food truck", "Mobile library", "Popemobile","Bloodmobile","Houseboat", "Tank"]
    ,["road trip", "carpool lane", "Bikini car wash", "hitchhiking", "valet parking", "Race", "Dashcam","Traffic jam", "Car sex", "Speed limit", "Parking ticket","Road rage", "Staged crash", "Filling up with gas", "Getting a license", "Driving test", "Rush hour", "GPS navigation", "DWD", "Roadside assistance", "Car insurance", "Annual inspection", "Toll roads", "Rental", "Vehicle recall"]  # nor_obj
    ,["valet", "mechanic", "Car-dweller", "traffic cop", "hitchhiker", "car designer", "Biker gang", "Driver", "Passenger", "Mechanic", "Grooper", "Traffic cop", "Car salesperson", "Driving instructor", "Valet", "Car designer", "Commuter", "Joyrider", "Motorist", "Hitchhiker", "Chauffeur"]  # nor_agent
)
abcl_book = FactAbnormalCliche(
    "abcl_book",
    ["pop-up book", "palimpsest", "codex", "flip book", "zine", "artist's book", "photobook", "dictionary", "coloring book", "scrapbook", "textbook", "phone book", "address book", "album", "cookbook", "children's book", "Porngraphy", "e-book", "audiobook", "travel guide", "catalogue", "diary", "journal"]
    ,["book club", "bestseller list", "book signing", "bed-time story", "dust jacket", "dog-eared pages", "library", "library fine", "reading nook", "book review", "foreword", "afterword", "dedication page", "Browsing", "bookmark", "page-turner", "making notes in margins", "sequel", "prequel", "trilogy", "series", "adaptation (movie/TV)", "book review", "literary award", "first edition", "print run", "Figure/ Chart"]
    , ["illustrator", "translator", "bookworm", "storyteller"]
)
abcl_pleasure = FactAbnormalCliche(
    "abcl_pleasure"
    ,["Schadenfreude", "Absenteeism", "Reconciliation", "Shower", "Runners' high", "Procrastination", "Petting animal", "Doing nothing"]
    ,["Addiction", "Orgasm", "Withdrawal symptoms", "Recreational activity", "Regulate", "Overdose", "gateway drug", "Addiction Treatment Camp", "Peer pressure", "bankruptcy", abcl_have_sex.nor_obj]
    ,["Junkey", "Addiction Counselor", "Dealer", abcl_have_sex.nor_agent] 
)




# You're like Stalone -> Skinny -> You're (acting is) like Stalone 
# Mixed -> War rape
# akina の toriyan no neta ha AGi(abcl_pet: "bird")