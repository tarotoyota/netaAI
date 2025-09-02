from dataclasses import dataclass, field
from typing import List, ClassVar, Any

from inst_factagentbinary import *


@dataclass
class Binary2:
    ALL_BINARY2: ClassVar[List['Binary2']] = []
    z_factagentbinary: 'FactAgentBinary'
    effort:list
    suffer:list
    appear:list
    action:list
    slump:list
    fail:list
    pressure_emergency:list

    charity:list
    authentic:list
    too_late:list
    just_a:list
    brand:list 
    southpaw:list
    rev_adj:list



    def __post_init__(self):
        Binary2.ALL_BINARY2.append(self)
        if self.z_factagentbinary.high_intelligence or self.z_factagentbinary.art:
           self.rev_adj.append(["<a href='#mild_yankee'>mild_yankee</a>", "<a href='#illiteracy'>illiteracy</a>"])
        if self.z_factagentbinary.high_intelligence:
           self.too_late.append(["eating blue fish", "reading a thick book", "trying to solve a Rubik’s Cube", "doing mindfulness", "watching TED Talks", "doing doing flash ANZAN", "playing chess","Watch documentaries about scientists"])# print(f"comedy script * Ali: I suddenly had to take an IQ test in an hour. So I'm {enhancement_intelligence} quickly now. - Bob: It's too late.") Add new 10 ones without any explanations.
           self.just_a.append(["不健康な","暗い", "大卒の", "目の悪い", "痩せた", "太った", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
           self.brand.append("Nootropics")
        if self.z_factagentbinary.high_strength:
           self.rev_adj.append(["<a href='#unhealthy'>unhealthy</a>", "<a href='#middle_aged'>middle_aged</a>"])
           self.too_late.append(["doing push ups", "eating a low-calorie diet", "hiking up the stairs instead of using the elevator", "staying hydrated with water","drinking protein shakes", "eating energy bars","Watch documentaries about athletes"])# print(f"comedy script * Ali: I suddenly had to take an physical fitness test in an hour. So I'm {enhancement_physical} quickly now. - Bob: It's too late.") Add new 10 ones without any explanations.
           self.just_a.append(["健康な","明るい", "高卒の", "ガタイがいい", "痩せた", "背が高い", "色黒な", "ストリート系の", "社交的な", "姿勢のいい", "日焼けした", "アウトドアな", "体育会系の", "食事に気を使ってる"])
           self.brand.append("Doping material")
        if self.z_factagentbinary.art:
           self.just_a.append(["物憂げな", "詩的な", "悲観的な", "自罰的な"])
        if self.z_factagentbinary.showbiz:
           self.action.append(["fan meet-up", "tours", "solo event"])
           self.slump.append(["Trying to be the one who explains.", "Start a restaurant.", "Trying to be the one who teaches.", "Appearing in advertisements for online casinos and marijuana.", "Run for local council elections.", "Suddenly start talking about environmental protection and feminism.", "Appear in a show at a pachinko parlor.", "Releasing a memoir that nobody asked for.", "Getting involved in reality TV for a comeback.", "Starting a clothing line that flops spectacularly.", "Collaborating with lesser-known artists in desperate attempts to stay relevant.", "Suddenly becoming an advocate for obscure causes nobody cares about."])
        if self.z_factagentbinary.showbiz or self.z_factagentbinary.service:
           self.charity.append("invite")
        if self.z_factagentbinary.showbiz:
           self.charity.append("present one's goods")
        if self.z_factagentbinary.looks_job:
           self.rev_adj.append("<a href='ugly'>ugly</a>")
        if self.z_factagentbinary.service:
           self.charity.append("offer free service")
        if self.z_factagentbinary.retail or self.z_factagentbinary.manufacturing or self.z_factagentbinary.showbiz or self.z_factagentbinary.art:
           self.charity.append("present one's work")
        if self:
           self.authentic.append(["veteran", "famous", "self-taught", "chief", "self-employed"])
           self.brand.append(["lesson", "text"])
        if self.z_factagentbinary.showbiz:
           self.authentic.append(["Affiliated with his private agency", "Exclusive"])
        if self.z_factagentbinary.sport:
           self.authentic.append(["first team", "captain"])
        if self.z_factagentbinary.extrovert_introvert == "e":
            self.rev_adj.append(["<a href='#introvert'>introvert</a>", "<a href='#nerd'>nerd</a>"])
        if self.z_factagentbinary.extrovert_introvert == "i" and not self.z_factagentbinary.high_intelligence and not self.z_factagentbinary.art:
            self.rev_adj.append("<a href='#mild_yankee'>mild_yankee</a>")
        if self.z_factagentbinary.art:
            self.effort.append(["Sketching ideas in a notebook daily","Traveling for inspiration", "Abstinence", "Sublimating one's trauma into a work of art", "Use LSD", "Meditation", "Keeping a dream journal", "Creating art in the dark"])
            self.suffer.append(["A lack of depth that comes from a lack of life experience.","Emotionless","Become a victim of plagiarism", "Conflict with producers", "Commercialism", "Creator's block", "Drug addiction", "alcohol addiction", "sex addiction", "Cannot surpass one's rival", "Cannot surpass one's past self", "Paparazzi", "Stalkers", "Stalkers", "Antis", "Paparazzis", "Plagiarism damage", "Alleged plagiarism", "Plagiarism of his past self", "Commercialism", "Pressure to only work in popular genres", "Creators' block", "Out of ideas", "Generative AI"])
            self.action.append(["Hate commercialism", "Adopting a Child from the Third World", "Being in a dark room", "Getting involved in Scientology or SGI", "Addicting drug, alcohol and sex", "Has suicidal thoughts", "Support the American Democratic Party.", "Being interested in environmental issues", "Being atheist", "Expressing support or opposition to abortion", "Creating art as a form of protest", "Challenging societal norms through provocative installations","Decline or insult the award"])
        if self:
            self.effort.append(["Quit smoking and drinking", "Experience different activities", "Seek advice.", "Conflict with others about the way one do things.", "Sacrifice family, friend and lover.", "Become estranged from a partner.", "Become ill and get injured from overwork.", "Quit college or work to pursue the dream.", "Sell personal belongings for Activity funds"])
            self.suffer.append(["Slump", "Children's school fees", "Loans for activities", "Anticipating success, buying a house, having children, etc., but not succeeding."])

        if self.z_factagentbinary.high_intelligence:
            self.southpaw.append(["has savant syndrome", "is a graduate of MIT", "has an IQ of 150"])
        if self.z_factagentbinary.high_strength:
            self.southpaw.append(["is black", "is white", "has gigantism", "is of a martial race", "is of Samoan ethnicity"])
        if self.z_factagentbinary.sport:
            self.southpaw.append(["is southpaw", "is tall", "is ambidextrous", "has six fingers"])
        if self.z_factagentbinary.art:
            self.southpaw.append(["has eidetic memory", "has six fingers", "has perfect pitch", "has synesthesia", "has schizophrenia"])
        if self.z_factagentbinary.sport or self.z_factagentbinary.art or self.z_factagentbinary.showbiz or self.z_factagentbinary.service or self.z_factagentbinary.retail or self.z_factagentbinary.manufacturing:
            self.action.append(["Declaring refusal to collaborate with a specific country, company, award or fellow industry", "Openly criticizing a specific company, award or fellow industry"])
        if self.z_factagentbinary.sport or self.z_factagentbinary.art or self.z_factagentbinary.showbiz:
            self.action.append(["Experience of child abuse", "Childhood poverty", "Experience of addiction"]) # 虐待歴だけはアスリートやな
            self.action.append(["Give lectures", "Autograph sessions"])


b2_                     = Binary2(agbn_                    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_rock_musician        = Binary2(agbn_rock_musician       ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_singer               = Binary2(agbn_singer              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_classical_musician   = Binary2(agbn_classical_musician  ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_comedian             = Binary2(agbn_comedian            ,[],[],[],[],[],[],[],[],[],[],[],[],[],["<a href='#unfunny'>unfunny</a>"])
b2_novelist             = Binary2(agbn_novelist            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_artist               = Binary2(agbn_artist              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_doctor               = Binary2(agbn_doctor              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_researcher           = Binary2(agbn_researcher          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_actor                = Binary2(agbn_actor               ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_chef                 = Binary2(agbn_chef                ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_athlete              = Binary2(agbn_athlete             ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_violent_criminal     = Binary2(agbn_violent_criminal    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_cyber_criminal       = Binary2(agbn_cyber_criminal      ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_thief                = Binary2(agbn_thief               ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_examinee             = Binary2(agbn_examinee            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_gambler              = Binary2(agbn_gambler             ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_progamer             = Binary2(agbn_progamer            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_teacher              = Binary2(agbn_teacher             ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_farmer               = Binary2(agbn_farmer              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_livestock_farmer     = Binary2(agbn_livestock_farmer    ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_director             = Binary2(agbn_director            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_model                = Binary2(agbn_model               ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_guard                = Binary2(agbn_guard               ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_patient              = Binary2(agbn_patient             ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_the_dying            = Binary2(agbn_the_dying           ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_school_club_member   = Binary2(agbn_school_club_member  ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_journalist           = Binary2(agbn_journalist          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_idol                 = Binary2(agbn_idol                ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_composer             = Binary2(agbn_composer            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_dancer               = Binary2(agbn_dancer              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_barista              = Binary2(agbn_barista             ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_masseuse             = Binary2(agbn_masseuse            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_hotel_staff          = Binary2(agbn_hotel_staff         ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_craftsman            = Binary2(agbn_craftsman           ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_photographer         = Binary2(agbn_photographer        ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_game_designer        = Binary2(agbn_game_designer       ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_engineer             = Binary2(agbn_engineer            ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_delinquent           = Binary2(agbn_delinquent          ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_groper               = Binary2(agbn_groper              ,[],[],[],[],[],[],[],[],[],[],[],[],[],[])


###########################################################################################################

# Titles of authentic. Start answer with ```python.
# For example, one type of "an authentic chef" is a self-employed chef, so "Independent" should be added.
# One type of "an authentic patient" has a severe symptoms, so "Severe" and "Chronic" should be added.

b2_rock_musician      .authentic+=["Leader", "Soloist", "Independent", "Exclusive"]
b2_singer             .authentic+=["Center position", "Main vocal"]
b2_classical_musician .authentic+=["Leader", "Soloist"]
b2_comedian           .authentic+=["Headliner"]
b2_novelist           .authentic+=[]
b2_artist             .authentic+=[]
b2_doctor             .authentic+=["Leader", "Practitioner"]
b2_researcher         .authentic+=["Associate professor"]
b2_actor              .authentic+=["Starring"]
b2_chef               .authentic+=["Owner chef", "Independent"]
b2_athlete            .authentic+=["First team"]
b2_violent_criminal   .authentic+=["Top cat", "Repeat offender", "Wanted criminal"]
b2_cyber_criminal     .authentic+=["Top cat", "Repeat offender", "Wanted criminal"]
b2_thief              .authentic+=["Top cat", "Repeat offender", "Wanted criminal"]
b2_examinee           .authentic+=["A grade", "Passed for active duty"]
b2_gambler            .authentic+=["High roller"]
b2_progamer           .authentic+=["First team"]
b2_teacher            .authentic+=[]
b2_farmer             .authentic+=["Organic farmer"]
b2_livestock_farmer   .authentic+=["Organic farmer", "free range"]
b2_director           .authentic+=[]
b2_model              .authentic+=["Runway", "Exclusive"]
b2_guard              .authentic+=[]
b2_patient            .authentic+=["Severe", "Chronic"]
b2_the_dying          .authentic+=["Severe", "Chronic"]
b2_school_club_member .authentic+=["First team"]
b2_journalist         .authentic+=["Independent "]
b2_idol               .authentic+=["Center position"]
b2_composer           .authentic+=[]
b2_dancer             .authentic+=["Soloist"]
b2_barista            .authentic+=["Independent"]
b2_masseuse           .authentic+=["Independent"]
b2_hotel_staff        .authentic+=["Independent"]
b2_photographer       .authentic+=[]
b2_game_designer      .authentic+=["Free lance"]
b2_engineer           .authentic+=["Free lance"]
b2_delinquent         .authentic+=["Top cat", "Ex-offender", "outcast"]
b2_groper             .authentic+=["Top cat", "Repeat offender", "First offense", "Outcast", "Wanted criminal"]

###########################################################################################################

b2_rock_musician      .just_a+=["薬をやっている", "ステージ慣れした", "MCスキルが高い", "声の大きい"]
b2_singer             .just_a+=["邦楽が好きな", "声が良い", "リズム感のある", "ステージ慣れした", "カラオケ上手な", "表現力豊かな", "感性の豊かな", "MCスキルが高い", "声の大きい"]
b2_classical_musician .just_a+=["家が金持ってた", "クラシック通な", "ステージ慣れした"]
b2_comedian           .just_a+=["明るい", "ステージ慣れした", "声の大きい"]
b2_novelist           .just_a+=["メンヘラな", "文章力のある"]
b2_artist             .just_a+=["メンヘラな", "創造力豊かな", "感性の豊かな", "表現力のある"]
b2_doctor             .just_a+=["物知りな", "人体に詳しい", "冷静な判断ができる"]
b2_researcher         .just_a+=["物知りな", "専門知識のある"]
b2_actor              .just_a+=["映画好きな", "表現力豊かな", "感情表現の上手い", "カメラ慣れした", "声の大きい"]
b2_chef               .just_a+=["食事に気を使ってる", "味覚の鋭い"]
b2_athlete            .just_a+=["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"]
b2_violent_criminal   .just_a+=["反社会的な", "冷酷な", "予測不可能な"]
b2_cyber_criminal     .just_a+=["反社会的な", "冷酷な", "計画的な", "技術に詳しい", "リスクを取る", "情報収集能力の高い", "デジタルネイティブな"]
b2_thief              .just_a+=["狡猾な", "計画的な", "身軽な", "逃げ足の速い", "変装のうまい", "神出鬼没の"]
b2_examinee           .just_a+=["計画的な", "記憶力の良い", "自己管理のできる", "知識欲の強い", "粘り強い"]
b2_gambler            .just_a+=["債務者の","リスク好きな", "運の良い", "勝負強い"]
b2_progamer           .just_a+=["ゲーム好きな", "反射神経の良い", "チームワークの良い", "競争心の強い"]
b2_teacher            .just_a+=["教育熱心な", "子供思いの"]
b2_farmer             .just_a+=["広い土地持ってる", "田舎に住んでる"]
b2_livestock_farmer   .just_a+=[b2_farmer.just_a]
b2_director           .just_a+=["映画好きな", "表現力豊かな", "感情表現の上手い"]
b2_model              .just_a+=["おしゃれな","写真映えする","身だしなみの良い","スタイリッシュな","魅力的な","立ち振る舞いの美しい","体型維持に気を使う","流行に敏感な","見た目の良い"]
b2_guard              .just_a+=["防犯意識の高い", "監視カメラに詳しい", "巡回ルートを知り尽くした", "防犯ベルに敏感な", "警戒心の強い", "観察力の鋭い", "護身術に長けた", "緊急時の対応力がある", "危険予知能力が高い", "規律正しい", "冷静沈着な", "状況判断力に優れた", "チームワークに優れた"]
b2_patient            .just_a+=["調子の悪い"]
b2_the_dying          .just_a+=["調子の悪い"]
b2_school_club_member .just_a+=["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"]
b2_journalist         .just_a+=["文章力のある","情報収集能力の高い","コミュニケーション能力の高い","好奇心旺盛な","締め切りを守れる","客観的な視点を持つ"]
b2_idol               .just_a+=[]
b2_composer           .just_a+=["音楽的才能のある", "創造力豊かな", "感性の豊かな", "音楽理論に詳しい", "楽器演奏のできる", "聴覚の鋭い", "リズム感のある", "和声学に精通した", "音楽史に詳しい", "編曲能力の高い"]
b2_dancer             .just_a+=["表現力豊かな", "リズム感のある", "体の柔軟な", "ステージ慣れした", "感情表現の上手い", "ダンス好きな", "チームワークの良い"]
b2_barista            .just_a+=["コーヒーに詳しい", "接客スキルの高い", "手先の器用な", "味覚の鋭い", "清潔感のある", "効率的な", "朝型の", "コミュニケーション能力の高い", "忍耐強い", "アート感覚のある"]
b2_masseuse           .just_a+=["解剖学に詳しい", "手先の器用な", "体力のある", "コミュニケーション能力の高い", "清潔感のある", "気配りのできる", "忍耐強い", "リラックスさせる能力のある", "身体感覚の鋭い"]
b2_hotel_staff        .just_a+=["接客スキルの高い", "言語能力の高い", "清潔感のある", "気配りのできる"]
b2_photographer       .just_a+=["構図に優れた", "編集スキルの高い"]
b2_game_designer      .just_a+=[]
b2_engineer           .just_a+=[]
b2_delinquent         .just_a+=[]
###########################################################################################################

"""

b2_actor                .effort+=["Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."]
b2_athlete              .effort+=["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness", "Video Analysis"]

"""

# Add new items in b2_delinquent .effort. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Define b2_tiger_parent .effort. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

b2_singer               .effort+=[]
b2_classical_musician   .effort+=[]
b2_rock_musician        .effort+=[]
b2_comedian             .effort+=["People-watching", "Turning personal tragedies into jokes", "Making fun of themselves to deflect criticism", ]
b2_novelist             .effort+=["Researching historical events for accuracy"]
b2_artist               .effort+=[]
b2_doctor               .effort+=[]
b2_researcher           .effort+=[]
b2_actor                .effort+=["Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."]
b2_chef                 .effort+=[]
b2_athlete              .effort+=["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness", "Video Analysis"]
b2_school_club_member   .effort+=[b2_athlete.effort]
b2_progamer             .effort+=["Intense physical training", "Strict diet regimen", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"]
b2_gambler              .effort+=["Learning math", "Creating and checking statistical data"]
b2_examinee             .effort+=["Study all night", "Making flashcards", "Memorizing"]
b2_teacher              .effort+=["Creating engaging lesson plans", "Mentoring students outside of class hours", "Pursuing advanced degrees", "physical punishment"]
b2_craftsman            .effort+=["Practicing techniques for hours daily", "Studying traditional methods", "Experimenting with new materials", "Apprenticeship under a master", "Perfecting a single skill for years", "Attending specialized workshops"]
b2_violent_criminal     .effort+=["Study law", "Remove his fingerprints", "Study security technologies"]
b2_cyber_criminal       .effort+=["Learning multiple programming languages","Studying network security protocols","Practicing social engineering techniques","Keeping up with latest cybersecurity trends","Developing custom malware and exploits","Participating in hacking forums and communities","Conducting extensive reconnaissance on targets","Mastering encryption and anonymization tools","Building and maintaining botnets","Reverse engineering software and systems"]
b2_thief                .effort+=["Studying security systems", "Practicing lock-picking skills", "Practicing stealth techniques", "Networking with other criminals", "Using disguises and false identities", "Conducting reconnaissance on targets", "Managing stolen goods and laundering money"]


b2_farmer               .effort+=["Waking up before dawn", "Implement organic farming.", "Working long hours in all weather conditions", "Continuous learning about crop science and animal husbandry", "Maintaining and repairing equipment", "Soil management and conservation practices", "Implementing sustainable farming techniques", "Adapting to changing climate patterns", "Market research and business planning"]
b2_livestock_farmer     .effort+=[b2_farmer.effort]
b2_director             .effort+=["Storyboarding extensively", "Scouting locations", "Studying others' films and classic films", "Experimenting with new filming techniques", "Collaborating closely with actors and crew", "Fundraising for independent projects", "Attending film festivals", "Repeatedly does retakes"]
b2_model                .effort+=["Networking with industry professionals", "Maintaining a strict diet and fitness regimen", "Practicing poses and walks", "Attending casting calls and auditions regularly"]
b2_guard                .effort+=["Physical fitness training", "Self-defense classes", "Surveillance skills development", "Conflict resolution training", "First aid certification", "Night shifts", "Continuous situational awareness"]
b2_patient              .effort+=["Participating in experimental treatments", "Seeking alternative therapies", "Maintaining hope despite grim prognoses", "Creating memory books or videos for loved ones", "Advocating for research funding", "Joining support groups for rare diseases", "Traveling long distances for specialized care", "Managing complex pain regimens", "Adapting living spaces for declining mobility", "Planning end-of-life care", "Fundraising for medical expenses", "Documenting personal experiences for future patients"]
b2_the_dying            .effort+=[b2_patient.effort]

b2_journalist           .effort+=["Investigative fieldwork","Building and maintaining a network of sources","Fact-checking","shorthanding","Developing expertise in specific beats or topics","Risking personal safety for stories in dangerous areas","Working irregular hours to meet deadlines","Maintaining objectivity in reporting"]
b2_idol                 .effort+=[]
b2_composer             .effort+=["Listening to diverse genres of music","Studying music theory and composition techniques","Experimenting with different instruments","Collaborating with other musicians","Attending concerts and music festivals","Practicing sight-reading and ear training","Composing in unconventional environments","Analyzing scores of great composers",]
b2_dancer               .effort+=["Rigorous daily physical training","Practicing choreography for hours","Cross-training in different dance styles","Flexibility and stretching exercises","Strength and conditioning workouts","Studying anatomy and kinesiology","Maintaining proper sleep schedule for recovery","Regular physiotherapy and massage","Perfecting technique through repetition","Attending workshops and masterclasses","Analyzing performance videos for improvement","Developing stage presence and expression","Learning music theory and rhythm",]
b2_barista              .effort+=["Practicing latte art for hours", "Studying coffee bean varieties and origins", "Perfecting brewing techniques", "Developing a refined palate through cupping sessions", "Attending barista competitions", "Experimenting with new flavor combinations"]
b2_masseuse             .effort+=["Studying anatomy and physiology", "Developing hand and finger strength", ]
b2_hotel_staff          .effort+=["Memorizing guest preferences and names", "Practicing multiple languages for international guests", "Learning about local attractions and services", "Perfecting the art of room presentation", "Enhancing interpersonal skills for diverse guest interactions"]
b2_photographer         .effort+=["Studying color theory and its application in photography", "Attending photography workshops and seminars", "Building a diverse portfolio across multiple genres", "Learning to use various types of camera equipment"]

b2_game_designer        .effort+=[]
b2_engineer             .effort+=[]
b2_delinquent           .effort+=["Engaging in street fights", "Building alliances with other groups", "Evading law enforcement", "Navigating turf wars","Participating in graffiti art", "Learning self-defense techniques", "Developing street smarts", "Building a reputation through loyalty and fear", "Engaging in petty theft for resources", "Forming a network for information exchange"]

#b2_tiger_parent.effort += ["Enrolling children in extra classes (music, math, languages, sports)","Strictly monitoring academic progress","Scheduling structured study time daily","Insisting on practice and repetition until mastery","Providing additional study materials and challenge problems","Limiting leisure activities to prioritize learning","Constantly communicating with teachers about performance","Pushing children to enter competitions and advanced programs","Investing in tutors and specialized instructors","Tracking milestone achievements and setting higher goals"]




###########################################################################################################

"""
b2_singer               .suffer+=["Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"]
b2_comedian             .suffer+=["Dealing with cancel culture","Bombing on stage","Hecklers in the audience","Offensive jokes backfiring","Difficulty adapting to different audiences","Fear of being replaced by newer comedians", "Being typecast in a particular style of comedy", ]


"""

# Define b2_tiger_parent.suffer  in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


l_suffer_script             =["Lacking hints", "Plot hole", "Lacking a clear message","Poor character development","Weak plot structure","Unrealistic dialogue","Lack of conflict","Cliche or predictable storylines","Poor world-building","Underdeveloped themes","Weak endings"]
l_suffer_game               =["Luck-based", "Unbalanced ","Lack of content updates","Limited customization options","Pay-to-win elements or microtransactions","Lack of endgame content","Repetitive gameplay","Poor UI design","Lack of player agency","Buggy or glitchy performance","Limited replay value","Inconsistent difficulty levels","Weak or unengaging narrative"]
l_suffer_instrumental       =["Emotionless","lacking a clear message","Inability to play in different styles","Poor improvisation skills","Lack of stage presence","Inability to tune instrument properly"]

b2_singer               .suffer+=["Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"]
b2_classical_musician   .suffer+=[]
b2_rock_musician        .suffer+=[]
b2_comedian             .suffer+=["Dealing with cancel culture","Bombing on stage","Hecklers in the audience","Offensive jokes backfiring","Difficulty adapting to different audiences","Fear of being replaced by newer comedians", "Being typecast in a particular style of comedy", ]
b2_novelist             .suffer+=["Deadline", l_suffer_script]
b2_artist               .suffer+=["Emotionless","lack of creativity","unoriginal style","lack of craftsmanship", "Struggles with Proportions"  ,  "Weak anatomy knowledge"]
b2_doctor               .suffer+=["The trauma of not being able to save a patient's life."]
b2_researcher           .suffer+=["Plagiarism", "Not being able to get research funding", "Has white hair"]
b2_actor                .suffer+=["Physical injuries from stunts", "Pressure to maintain a certain physical appearance","The damage caused by method acting", "Unconvincing Performances", "Difficulty with Accents/Dialects","Overacts","lack of stage presence","Lack of character depth","Inability to improvise","Lack of chemistry with co-stars", l_suffer_script]



# Extend 10 new items in suffer_hotel_staff in English. I will run your reply through the eval function, so don't write anything unnecessary.




b2_violent_criminal     .suffer+=[]
b2_cyber_criminal       .suffer+=["Legal consequences and imprisonment","Constant paranoia of being caught","Difficulty maintaining personal relationships due to secrecy","Ethical dilemmas and moral conflicts","Burnout from constant vigilance","Isolation from mainstream society","Struggle to find legitimate employment after being caught","Mental health issues from high-stress lifestyle","Financial instability due to illegal income sources","Physical health problems from long hours at computer","Addiction to the thrill of hacking","Trust issues within hacking communities","Difficulty adapting to rapidly changing technology","Constant fear of rival hackers or law enforcement"]
b2_thief                .suffer+=["Fear of arrest", "Betrayal by accomplices", "Loss of trust from loved ones", "Constantly looking over one's shoulder", "Living in poverty due to criminal activities", "Guilt from harming others", "Isolation from society", "Struggles with addiction", "Conflict with law enforcement", "Inability to escape one's past", "being wanted "]
b2_dancer               .suffer+=[]
b2_chef                 .suffer+=[]
b2_athlete              .suffer+=["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"]
b2_school_club_member   .suffer+=["Pressure to perform well in competitions","Conflict with club members","Strain from balancing academics and club activities","Injury from overtraining","Lack of recognition for hard work","Unmet expectations from coaches","Feeling overshadowed by talented members","Lack of motivation during tough times","Pressure to follow strict training regimens","Isolation from non-club peers","bodily punishment","Coping with the fear of not improving",]
b2_progamer             .suffer+=[l_suffer_game, "Repetitive Strain Injury", "Carpal Tunnel Syndrome", "Eye strain",   "Addiction to gaming"]
b2_gambler              .suffer+=["Addiction to gambling", "Financial ruin", "Depression and anxiety", "Lying to cover losses", "Chasing losses", "Neglecting work or family responsibilities", "Legal troubles", "Substance abuse as a coping mechanism", "Suicidal thoughts"]
b2_examinee             .suffer+=["STEM inferiority complex", "Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"]
b2_teacher              .suffer+=["punk", "Pressure from parents and administration",  "Lack of autonomy in curriculum decisions", "Testing pressure", "Large class sizes", "bullying"]
b2_craftsman            .suffer+=["Repetitive strain injuries", "Lack of successors", "Exposure to harmful materials", "Competition from mass-produced items", "Difficulty in finding apprentices", "Financial instability", "Long hours of solitary work", "burnout", "Struggles with modernization and technology"]
b2_farmer               .suffer+=["Crop failures due to weather", "Market price fluctuations", "Equipment breakdowns", "Debt from loans", "Physical strain and injuries", "Eviction request", "Isolation in rural areas", "Pressure to adopt new technologies", "Regulatory challenges", "Competition from large agribusinesses", "Succession planning difficulties"]
b2_livestock_farmer     .suffer+=[b2_farmer.suffer]
b2_director             .suffer+=["Budget constraints", "Creative differences with producers", "Pressure to meet box office expectations", "Negative critical reviews", "Challenges with difficult actors", "Technical issues during filming", "Post-production problems", "Distribution hurdles", "Balancing artistic vision with commercial viability", l_suffer_script]
b2_model                .suffer+=["Body image issues", "Pressure to maintain unrealistic beauty standards", "Casting couch", "Constant scrutiny of physical appearance", "Age-related career decline", "Eating disorders", "Social media harassment"]
b2_guard                .suffer+=["Monotonous work", "Long hours and night shifts", "Lack of recognition", "Stress from constant vigilance", "Physical strain from standing for long periods", "Dealing with aggressive individuals", "Post-traumatic stress from violent incidents", "Social isolation due to irregular work hours"]
b2_patient              .suffer+=['Overlapping surgeries', 'Repeated recovery times',"Chronic pain", "Loss of independence", "Social isolation", "Depression and anxiety", "Recurrence", "Financial burden of treatment", "Side effects from medications", "Guilt over being a burden to family", "Loss of identity and purpose", "Fear of the unknown future", "Difficulty in maintaining relationships", "Cognitive decline", "Physical deterioration", "Fatigue and exhaustion", "Frustration with healthcare system", "Grief over lost opportunities and experiences", "Stigma associated with their condition", "Difficulty in planning for the future", "Constant medical appointments and procedures", "Loss of privacy due to care needs", "Existential crisis and questioning of life's meaning", "Having to give up sports", "Having to quit work"]
b2_the_dying            .suffer+=[b2_patient.suffer]
b2_journalist           .suffer+=["Pressure to meet tight deadlines","Ethical dilemmas in reporting","Threats to personal safety in dangerous locations","Difficulty maintaining objectivity","Stress from covering traumatic events","Pressure to produce clickbait content","Difficulty verifying sources in the age of misinformation","Pressure to be active on social media","Burnout from constant news cycle","Criticism and harassment from public figures or readers","Difficulty accessing reliable sources","Pressure to break news first, potentially compromising accuracy",]
b2_idol                 .suffer+=[]
b2_composer             .suffer+=["Lack of originality in compositions","Inability to translate ideas into music","Difficulty in creating memorable melodies","Poor orchestration skills","Struggle with complex harmonies","Inability to meet deadlines for commissioned works","Criticism for experimental or avant-garde pieces","Difficulty in balancing artistic vision with commercial demands","Difficulty in finding performers or orchestras to play compositions",]
b2_barista              .suffer+=["Burns from hot liquids and equipment"]
b2_masseuse             .suffer+=["Repetitive strain injuries"]
b2_hotel_staff          .suffer+=["Dealing with rude or demanding guests"]
b2_photographer         .suffer+=["Physical strain from carrying heavy equipment",  "Emotional toll from capturing sensitive or traumatic events", "Weather-related challenges during outdoor shoots", "Loneliness during solo travel for assignments"]
b2_game_designer        .suffer+=[]
b2_engineer             .suffer+=[]
b2_delinquent           .suffer+=["Having to obey the teacher's orders", "Having to go to school every day","Strained relationships with family and friends","Fear of legal consequences","Limited future opportunities","Conflict with rival groups","Pressure to conform to gang expectations", "Getting caught by the police", "Getting into fights", "Academic problems", "Peer pressure", "Substance abuse"]

#b2_tiger_parent         .suffer += ["Strained relationship with children due to pressure","Social isolation from other parents who disagree with strict methods","Constant stress from monitoring academic performance","Guilt if children show signs of unhappiness or rebellion","Criticism from society for being too strict","Children experiencing burnout or mental health struggles","Conflict with spouse or family members over parenting style","Feeling unappreciated despite sacrifices","Exhaustion from managing demanding schedules","Fear of children resenting them in adulthood"]



# Define b2_photographer .suffer. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

###########################################################################################################
"""
b2_singer                 .appear+=["Many piercings", "Many tattoos", "Colorful hair", "split tongue"]
b2_classical_musician     .appear+=["Formal black attire","Bow tie","Slicked-back hair","Round glasses","Pale complexion","Thin frame"]
"""
# Define b2_delinquent.appear. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


b2_singer                 .appear+=["Many piercings", "Many tattoos", "Colorful hair", "split tongue"]
b2_classical_musician     .appear+=["Formal black attire","Bow tie","Slicked-back hair","Round glasses","Pale complexion","Thin frame"]
b2_rock_musician          .appear+=["Many piercings", "Many tattoos", "Colorful hair", "split tongue"]
b2_comedian               .appear+=[]
b2_novelist               .appear+=["Wears a samue", "Has a beard", "Thin and pale", "Messy hair"]
b2_artist                 .appear+=["Many piercings", "Many tattoos", "Colorful hair"]
b2_doctor                 .appear+=["White coat", "Messy hair"]
b2_researcher             .appear+=["White coat", "Messy hair", "Has bags under one's eyes", "Carries around a clipboard", "using a wheelchair"]
b2_actor                  .appear+=[]
b2_chef                   .appear+=["Kaiser moustache", "Being fat", "Wears a neckerchief", "Has a thick accent"]
b2_violent_criminal       .appear+=["Unkempt appearance", "Wild eyes", "Scars or burn marks", "Twitchy movements", "Wears all black", "Clown-like makeup", "Disheveled hair", "Pale skin", "Bloodstained clothing", "Ritualistic tattoos", "Leather gloves", "Creepy mask"]
b2_cyber_criminal         .appear+=["Anonymas mask", "Hoodie or dark clothing","Multiple computer screens","Pale complexion from lack of sunlight","Dark circles under eyes","Messy or unkempt hair","Fingerless gloves","Glasses or blue light glasses","Headphones or earbuds","Energy drinks or coffee cups","Stickers on laptop","Mechanical keyboard","Wrist brace","Fidget toys","Cyberpunk-style accessories","Backpack with tech gear","Smartwatch or fitness tracker","Graphic t-shirts with tech or hacker slogans"]
b2_thief                  .appear+=["Dark clothing", "Hooded sweatshirt", "Face partially covered", "Sneakers for quiet movement", "Gloves to avoid leaving fingerprints", "Shifty eyes", "Nervous demeanor", "Backpack or duffel bag for carrying loot", "Quick, agile movements", "Camouflage patterns or tactical gear", "Elegant cloak or cape", "Mask covering the eyes", "Stylish attire with dark colors", "Gloves for stealth", "Lightweight shoes for silent movement", "Mysterious aura", "Accessories like a cane or dagger", "Emphasis on agility and grace", "Shadowy presence", "Intricate patterns on clothing"]


b2_athlete                .appear+=["Muscular build", "Athletic wear", "Sweatbands", "Sports gear", "Taped joints or limbs", "Shaved body", "Visible tan lines", "Team jersey or uniform", "Dreadlocks"]
b2_school_club_member     .appear+=["Casual school uniform","Backpack with club patches","Sweatpants or athletic wear","Team colors or logos","Wristbands or headbands","Enthusiastic expressions","Stickers or pins on bags","Sweaty hair","Energy drinks or snacks in hand","Temporary tattoos or face paint for events","Team spirit accessories like hats or scarves","Casual shoes suitable for activities","Hair tied back or styled for practicality","Friendship bracelets or charms",]
b2_gambler                .appear+=["Disheveled appearance", "Dark circles under eyes", "Nervous twitches", "Flashy jewelry", "Expensive watch", "Rumpled suit", "Cigarette in hand", "Fidgeting with chips or cards", "Sunglasses indoors", "Sweaty brow", "Loosened tie", "Rolled-up sleeves", "Has a red pencil on his ear."]
b2_progamer               .appear+=["Headset", "Gaming chair", "Energy drinks", "Junk food", "Eyeglasses", "Acne", "Poor posture", "Headaches", "Back pain", "Wrist pain", "Messy hair", "Dark circles under eyes", "Skinny build", "Multiple monitors", "RGB lighting", "Wrist brace"]
b2_teacher                .appear+=["Glasses", "Cardigan sweater", "Sensible shoes", "Messy bun or ponytail", "Lanyard with ID badge", "Tote bag full of papers", "Elbow patches on jacket", "Chalk dust on clothes", "Coffee stains", "Comfortable, modest clothing", "Practical hairstyle", "Minimal makeup", "Wristwatch", "Reading glasses on a chain", "Colorful, quirky accessories"]
b2_craftsman              .appear+=["Leather apron", "Calloused hands", "Rolled-up sleeves", "Safety goggles", "Work boots", "Tool belt", "Weathered skin", "Muscular forearms", "Sawdust or wood shavings on clothes", "Protective gloves", "Bandana or cap", "Rugged, worn clothing", "Pencil behind ear", "Measuring tape clipped to belt", "Beard or mustache"]


# Define b2_photographer .appear. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



b2_farmer                 .appear+=["Overalls", "Plaid shirt", "Straw hat", "Work boots", "Sunburned skin", "Calloused hands", "Weathered face", "Farmer's tan", "Dirt under fingernails", "Faded jeans", "Bandana", "Belt buckle", "Leather work gloves", "Seed company cap"]
b2_livestock_farmer       .appear+=[b2_farmer.appear]
b2_director               .appear+=["Beret or flat cap", "Thick-rimmed glasses", "Scarf", "Black turtleneck", "Blazer with elbow patches", "Cargo vest with many pockets", "Comfortable, worn-in shoes", "Stubble or well-groomed beard", "Vintage watch", "Messenger bag or satchel", "Sunglasses (even indoors)", "Quirky, statement jewelry", "Fashionable, yet practical clothing", "Artsy, unconventional hairstyle", "Director's chair with name on it", "Viewfinder around neck"]
b2_model                  .appear+=["Tall and slender figure", "High cheekbones", "Long legs", "Perfect skin", "Symmetrical facial features", "Styled hair", "Designer clothing", "High heels", "Minimal makeup", "Manicured nails", "Confident posture", "Sunglasses", "Statement jewelry", "Visible collarbones", "Toned physique"]
b2_guard                  .appear+=["Uniform with badge", "Utility belt", "Earpiece", "Sunglasses", "Crew cut or short hair", "Muscular build", "Stern facial expression", "Combat boots", "Visible tattoos", "Clean-shaven face", "Bulletproof vest", "Name tag", "Flashlight", "Walkie-talkie", "Neatly pressed clothes", "Military-style posture", "Blood type tattoo", "scar"]
b2_patient                .appear+=["Pale complexion", "Significant weight loss", "Hair loss or thinning", "Dark circles under eyes", "Medical devices (e.g., oxygen tank, IV drip)", "Wheelchair or mobility aids", "Visible scars from surgeries", "Swollen limbs or joints", "Yellowing of skin or eyes (jaundice)", "Rashes or skin discoloration", "Tremors or involuntary movements", "Hunched posture", "Hospital gown or comfortable loose clothing", "Medical alert bracelet", "Nasal cannula or face mask", "Bandages or dressings", "Visible port for medication administration", "Sunken cheeks or hollow eyes", "Brittle nails and dry skin", "Bruising from blood draws or injections"]
b2_the_dying              .appear+=[b2_patient.appear]
b2_journalist             .appear+=["Press badge or lanyard","Notebook and pen","Comfortable shoes for field work","Laptop bag or backpack","Smart phone or recording device","Camera","Trench coat","Fedora hat","Glasses or sunglasses","Messenger bag","Microphone","Windbreaker with news outlet logo","Khaki vest with many pockets","Disheveled appearance from long hours","Coffee stains on clothing"]
b2_idol                   .appear+=[]
b2_composer               .appear+=["Formal black attire","Bow tie or cravat","Round glasses","Messy or wild hair","Ink-stained fingers","Slightly disheveled appearance","Eccentric accessories (e.g., colorful scarves)","Pale complexion from long hours indoors","Thoughtful or distant expression","Carries a notebook or sheet music","Wears a beret or other distinctive hat","Has a beard or mustache","Wears comfortable, loose-fitting clothing","Often seen with headphones","Has bags under eyes"]
b2_dancer                 .appear+=["Lean, muscular physique","Flexible body","Excellent posture","Toned legs and arms","Hair in a tight bun or ponytail","Leotards or form-fitting dance wear","Ballet shoes or specialized dance footwear","Leg warmers or warm-up clothes","Minimal jewelry","Natural, stage-ready makeup","Visible muscle definition","Callused feet","Dance bag with spare shoes and accessories","Sweat-wicking clothing","Compression garments for support","Kinesiology tape on joints or muscles"]
b2_barista                .appear+=["Apron with coffee shop logo", "Neat and tidy hair (often tied back)", "Black or earth-toned clothing", "Name tag", "Wristwatch for timing shots", "Tattoos (often visible)", "Ear piercings", "Callused hands from handling hot equipment", "Burn marks on hands or arms", "Coffee stains on clothing", "Neutral-colored nail polish or well-groomed nails", "Minimal jewelry for hygiene reasons"]
b2_masseuse               .appear+=["Comfortable, loose-fitting uniform", "Slip-resistant shoes", "Hair tied back neatly", "Minimal jewelry", "Well-groomed nails (short and clean)", "Subtle, natural makeup (if any)", "Name tag or identification badge", "Wristwatch for timing sessions", "Neutral-colored clothing", "Relaxed and calm facial expression", "Toned arms and hands", "Good posture", "Possible aromatherapy scent", "Soft-soled shoes for quiet movement", "Clean, moisturized hands"]
b2_hotel_staff            .appear+=["Neat, pressed uniform", "Name tag", "Polished shoes", "Well-groomed hair", "Minimal jewelry", "Subtle makeup", "Clean, manicured nails", "Tie or bow tie for men", "Scarf or neckerchief for women", "Professional smile", "Good posture", "Earpiece for communication", "Wristwatch", "Belt with hotel logo", "Crisp white shirt or blouse"]
b2_photographer           .appear+=["Camera around neck", "Multiple lenses in bag", "Comfortable, practical clothing", "Sturdy shoes for long shoots", "Vest with many pockets", "Tripod slung over shoulder", "Memory card holder on belt", "Laptop bag for editing on-the-go", "Weatherproof jacket", "Fingerless gloves for cold shoots", "Baseball cap or sun hat", "Polarizing sunglasses", "Backpack full of gear", "Lens cleaning cloth hanging out of pocket", "Smartwatch for timing shots", "Portable external hard drive"]
b2_delinquent             .appear+=["Baggy clothes", "Leather jacket", "Tattoos", "Piercings", "Shaved head", "Mohawk", "Sneakers", "Hoodies", "Sunglasses", "dyed hair","Graphic tees with band or gang logos"]

###########################################################################################################
"""

b2_rock_musician          .action+=["Suddenly starts writing music on paper", "Hate edited music", "Hate lip syncing", "Writing songs about personal struggles","Engaging with fans during concerts","Throwing guitars during performances","Making spontaneous decisions about setlists","Refusing to play the same song twice in a row","Insisting on using vintage equipment","Hosting impromptu jam sessions"]
b2_researcher             .action+=["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings.", "Forgetting to eat or sleep while working on a problem", "Wearing mismatched or stained clothing", "Carrying around stacks of papers and books everywhere", "Muttering to themselves while pacing"]



"""

# Define b2_tiger_parent.action. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

universal_action_musician = ["Hate lip sync/ instrumental mimic", "Hate edited music", "Suddenly starts writing music on paper", "Compose music based on the theme of personal conflict or political statement.", "Engage with fans during concerts", "Refuse to play the same music twice in a row", "Refuse to perform due to lack of one's ideal equipments", "Insist on using vintage/ analog equipment", "Hosting impromptu jam sessions", "Making spontaneous decisions about setlists", "Changing lyrics mid-performance"]

b2_rock_musician          .action+=[universal_action_musician, "Throw guitars during performances", "Satanism or neo-Nazi themes", "Use animal carcasses in performances", "Performance on drugs"]
b2_singer                 .action+=[universal_action_musician]
b2_classical_musician     .action+=[universal_action_musician]
b2_comedian               .action+=["Claiming that only they understand true humor.",  "Mocking popular culture while secretly loving it.", "Claiming that comedy should be offensive.", "Refusing to adapt their style for modern audiences.", "Refusing to engage with social media trends.", "Blaming the audience for the lack of laughs.", "Be hostile towards TikTok.", "Hostile to political correctness.", "Dislikes comedians who pander to young people and women", "Being an atheist.",  "Refusing to laugh at other comedians' jokes", "Performing in small, obscure venues to maintain 'authenticity'.","Criticizing the mainstream for lacking originality while secretly wanting to be part of it.","Insisting that comedy is an art form that should not be commercialized.","hostile to comedians who use props.","hostile to any form of censorship in comedy.","Being obsessed with timing and delivery.","Being dismissive of audience reactions.","Being resistant to collaboration with other comedians.",]
b2_novelist               .action+=["Hate teen novels"]
b2_artist                 .action+=[]
b2_doctor                 .action+=["Having a stethoscope draped around their neck at all times","Being overly critical of alternative medicine","Being meticulous about hygiene and cleanliness",]
b2_researcher             .action+=["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings.", "Forgetting to eat or sleep while working on a problem", "Wearing mismatched or stained clothing", "Carrying around stacks of papers and books everywhere", "Muttering to themselves while pacing"]
b2_actor                  .action+=["Looking down on lighting engineers and cinematographers.""Constantly practicing lines in public","Name-dropping famous directors or actors","Insisting on being called by their character's name","Refusing to break character even off-set","Demanding specific brands of bottled water on set","Throwing tantrums when not given enough screen time","Obsessing over their appearance and plastic surgery",]
b2_athlete                .action+=["Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk", "meathead", "Partying excessively","Constantly flexing muscles","Overusing sports metaphors in conversation","Ignoring injuries to keep playing","Developing superstitious pre-game rituals","Displaying trophies prominently","Challenging others to physical contests","Downplaying academic achievements","Overreacting to minor injuries","Having a personal trainer","Being overly competitive","Promoting sports brands on social media","Creating workout videos or blogs", "Converse with tools", "Arguing about whether weight training is necessary or not", "Having a favorite sports movie they reference frequently", "Attending every game of their favorite team", "Breaking equipment in anger over one's own mistake", "Posting workout selfies", "Critiquing others' techniques"]
# In """ b2_doctor """, Add new stereotypical actions. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Define action_criminal instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Add new 10 item in action_artist instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.






# That's what the workers should do, right? I don't ask for that. Don't generate just "job descriptions". Please try again.


b2_school_club_member     .action+=["Practicing late into the night","Engaging in friendly rivalries with other clubs","Building team spirit through bonding activities","Encouraging others to join the club","Celebrating victories together","Bullying nerds","Rehabilitating from delinquency through club activities","Confronting a childhood friend from a rival school","Creating team chants or cheers","Scouting a rival school","Encouraging members to bring friends to meetings",]
b2_chef                   .action+=["Getting angry at customers for using condiments", "Yelling at kitchen staff",  "Striving for Michelin stars", "Taking pride in sourcing ingredients locally", "Focus on seasonal ingredients", "Focus on pesticide-free ingredients"]
b2_violent_criminal       .action+=["Talking to imaginary friends", "Dissected a cat as a child", "Collecting trophies from victims", "Taking hostages", "Destroying evidence", "Defecting/fleeing the country", "Turning oneself in", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility", "Leaving cryptic clues at crime scenes", "Sending taunting messages to police", "Developing a signature kill method", "Creating disturbing artwork related to their crimes", "Displaying a fascination with death and decay", "Maintaining a calm demeanor during interrogations", "Keeping detailed journals of crimes", "Ritualistic behavior before or after crimes", "Creating alter egos or personas", "Using humor to mask sinister intentions", "Forming chaotic alliances with other criminals"]
b2_cyber_criminal         .action+=["Drinking energy drinks", "Eating pizza", "Always eat sweets", "Loving anime", "Wearing sunglasses indoors","Decorating workspace with sci-fi posters","Using multiple smartphones","Obsessively securing personal devices","Bragging about hacks anonymously online","Collecting cryptocurrency","Attending hacker conventions in disguise","Testing security systems for fun","Hoarding old computer hardware","Staying awake for days during a hack",  "Customizing computer with neon lights", "Using dual monitors"]
b2_thief                  .action+=[]

b2_gambler                .action+=["Constantly checking scores or results", "Borrowing money from friends and family",  "Lying about whereabouts or activities", "Skipping work or important events to gamble", "Celebrating wins extravagantly", "Becoming irritable when unable to gamble", "Hiding betting slips or casino receipts", "Making increasingly risky bets", "Talking excessively about past wins", "Chasing losses with bigger bets", "Steal money"]
b2_progamer               .action+=["Trash talking opponents", "Celebrating wins excessively", "Skipping meals to practice", "Neglecting personal hygiene", "Becoming irritable when unable to play", "Bragging about ranking or skills", "Forming rivalries with other players", "Rage quitting", "Streaming for hours", "Using gaming slang in everyday conversation"]
b2_teacher                .action+=["Have students write the same word on the board multiple times.", "Giving pop quizzes unexpectedly", "Showing favoritism in grading", "Writing motivational quotes on the board","gets angry when students go to cram schools or prep schools", "Constantly correcting others' grammar", "Carrying a red pen everywhere", "Assigning homework on weekends and holidays","Favoring certain students", "Talking in a condescending tone", "Struggling with technology in the classroom", "Drinking excessive amounts of coffee"]
b2_craftsman              .action+=["Obsessing over tool organization", "Refusing to use modern technology", "Criticizing mass-produced items", "Wearing traditional work attire", "Collecting rare or antique tools", "Talking extensively about material quality", "Insisting on doing everything by hand", "Becoming irritated when rushed", "Hoarding materials and supplies", "Giving unsolicited advice on craftsmanship", "Throw the failed piece onto the floor."]
b2_farmer                 .action+=["Complaining about weather", "Waking up at dawn", "Wearing overalls and a straw hat", "Chewing on a piece of straw", "Talking about crop prices", "Distrusting city folk", "Attending county fairs", "Participating in farmers' markets", "Driving a tractor on public roads", "Using farming metaphors in conversation"]
b2_livestock_farmer       .action+=[b2_farmer.action]
b2_director               .action+=["Constantly wearing a beret or scarf", "Using a megaphone unnecessarily", "Obsessively rewatching their own films", "Making grandiose statements about the power of cinema", "Insisting on unnecessary multiple takes", "Dramatically yelling 'cut!' and 'action!'", "Refusing to compromise on artistic vision", "Micromanaging every aspect of production", "Giving long, pretentious interviews about their craft", "Carrying a viewfinder everywhere"]
b2_model                  .action+=["Walking with exaggerated hip movements", "Constantly checking appearance in mirrors", "Posing for selfies frequently", "Dieting excessively", "Attending fashion shows and parties", "Networking aggressively with industry professionals", "Practicing facial expressions and poses", "Complaining about uncomfortable high heels", "Discussing latest beauty treatments", "Maintaining a strict skincare routine", "Doing yoga or pilates regularly", "Endorsing products on social media", "Comparing themselves to other models", "Rushing to castings and photo shoots", "Meticulously planning outfits for events"]
b2_guard                  .action+=["Has military experience", "Speaks in code over radio", "Wears sunglasses at night", "Constantly scans surroundings", "Stands with hands clasped in front", "Touches earpiece frequently", "Uses excessive force when provoked", "Drinks coffee excessively during night shifts", "Develops paranoia over time", "Has a tough, stoic demeanor"]
b2_patient                .action+=["Reminisce about the past", "Contact loved ones", "Obsess over unfinished business", "Seek redemption", "Have philosophical conversations", "Make peace with my mortality", "Create art as a legacy", "Find solace in spirituality", "Constantly check medical devices or monitors", "Take multiple medications throughout the day", "Keep a detailed health journal", "Research alternative treatments", "Attend support group meetings", "Undergo frequent medical tests and procedures", "Practice meditation", "Discuss end-of-life plans with family", "Seek second opinions from specialists", "Participate in clinical trials", "Advocate for increased research funding", "Share personal experiences on social media", "Create bucket lists or set short-term goals", "Rely on caregivers for daily tasks", "Struggle with insurance companies for coverage", "Express gratitude to healthcare providers", "Prepare legal documents like living wills", "Cherish moments with loved ones"]

# List of actions in first-person, without subjects






















b2_the_dying              .action+=[b2_patient.action, "Trying to communicate last words",  "Experiencing flashbacks of life moments", "Seeking help from bystanders"]

b2_journalist             .action+=["Always carrying a notebook and pen","Constantly checking multiple news sources","Asking probing questions in social situations","Refusing to reveal sources","Maintaining a cynical or skeptical worldview","Rushing to be first to break a story","Developing a thick skin against criticism",]
b2_idol                   .action+=[]

b2_composer               .action+=["Conducting imaginary orchestras","Humming or whistling constantly","Tapping out rhythms on any available surface","Suddenly stopping mid-conversation to jot down musical ideas","Critiquing background music in public places","Collecting unusual instruments","Experimenting with unconventional sound sources","Staying up all night to finish a composition","Obsessively revising and perfecting pieces","Attending concerts of various genres for inspiration","Isolating themselves for long periods to focus on work","Talking passionately about obscure musical theories","Refusing to listen to certain genres or artists","Insisting on perfect acoustic conditions for listening to music"]
b2_dancer                 .action+=["Expressing emotions through movement in daily life",]
b2_barista                .action+=["Correcting customers' pronunciation of coffee terms", "Critiquing other cafes' coffee", "Discussing coffee bean origins in detail", "Refusing to serve coffee with milk or sugar", "Posting artistic coffee photos on social media", "Judging people who order decaf", "Hates mass-produced coffee like poison"]
b2_masseuse               .action+=["Constantly cracking their own joints", "Offering unsolicited posture advice", "Critiquing massage techniques in movies", "Practicing new techniques on friends and family", "Recommending stretches to everyone", "Promoting alternative healing methods", ]
b2_hotel_staff            .action+=["Always maintaining a polite smile", "Speaking in a hushed tone", "Carrying multiple items effortlessly", "Memorizing guest names and preferences", "Walking briskly but quietly", "Anticipating guest needs before they ask", "Providing detailed local recommendations",  "Folding towels into decorative shapes", "Inspecting rooms with a keen eye for detail", "Practicing different languages during breaks", "Expertly handling luggage of all sizes", "Mediating conflicts between guests"]
b2_photographer           .action+=["Constantly adjusting camera settings", "Crouching or lying down for unique angles", "Directing subjects for poses", "Obsessively checking and rechecking equipment", "Talking about light quality and composition", "Stopping abruptly to capture spontaneous moments", "Carrying multiple cameras for different situations", "Waking up extremely early for 'golden hour' shots", "Climbing or positioning themselves in precarious spots for the perfect shot", "Asking strangers if they can take their photo", "Spending excessive amounts on new gear", "Constantly looking for interesting compositions in everyday life", "Posting daily on social media platforms", "Offering unsolicited photography advice to others"]
b2_delinquent             .action+=["Skipping school", "Vandalizing property", "Stealing", "Selling drugs", "Shoplifting", "Bullying nerds", "Loudly interrupting lessons", "Getting into fights", "Drinking alcohol", "Using drugs", "Dropping out of school", "Joining a gang", "Engaging in risky behavior", "Rappes about their crimes", "graffiti"]
b2_delinquent             .action+=["暴走行為", "たかり", "恐喝", "傷害", "未成年飲酒", "喫煙", "補導歴", "鑑別所", "授業をサボる", "校内暴力", "万引き", "喧嘩", "違法薬物の使用", "シンナーの使用", "中退", "暴走族に加入", "非行を自慢する", "制服の改造", "夜遊び", "不良グループの結成", "教師への反抗", "恐喝", "器物損壊", "タバコを吸う", "バイクの無免許運転", "カンニング", "学校の備品を盗む"]
b2_groper                 .action+=["Claims that their hand just accidentally touched the train.","Claims that the cause was the shaking of the train.","Claims that the cause was the crowding.","Escape by running along the tracks.","Claims that they were innocent.","Commits the crime on the day of the high school entrance exams.","Touch the victim with the back of their hand to hide their criminal intent.","Target women who appear timid."]

#b2_tiger_parent.action = ["Checking children's homework every day","Frequently comparing their children to higher-achieving peers","Enrolling children in multiple extracurricular activities","Criticizing less-than-perfect grades or performances","Attending parent-teacher conferences aggressively","Setting strict rules about study and leisure balance","Scheduling extra tutoring sessions","Monitoring children's online activities and friendships","Pushing children to enter academic competitions","Dictating career or college choices for children","Correcting children's mistakes publicly to enforce discipline","Sacrificing personal time to supervise study sessions","Rewarding achievements with more responsibilities instead of leisure","Using other successful children as examples in front of their own","Withholding praise unless the result is exceptional"]




# Define b2_photographer .action. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



# Define stereoaction_model in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.
###########################################################################################################




###########################################################################################################
'''
# Add new specific harmful eccentricities in b2_journalist with the person name. Start answer with ```python
# All you have to do is google "singer eccentricities" or "singer anecdote" and extract the specific parts of the information that comes up.

b2_novelist             .action+=["Became far-right and attempted a coup (Yukio Mishima)", "attempted suicide many times with women who were codependent on him (Osamu Dazai)"]
b2_artist               .action+=["Cutting off his own ear (Van Gogh)"]
b2_researcher           .action+=["Overthinking leads to pseudoscience (Linus Pauling)", "Believing in psychic phenomena (Edison)"]
b2_actor                .action+=["Method acting unearths trauma and leads to psychosis (Edward Montgomery Clift)"]
b2_director             .action+=["Try to destroy a house that gets in the way of filming (Akira Kurosawa)", "Held the cast at gunpoint to get a performance he desired (Akira Kurosawa)"]
b2_gambler              .action+=["Hundreds of hours spent observing roulette wheel deflection at casinos (Joseph Jagger)"]


# 上記プロンプトを受けて誤答したyou.comに "That's not specific. That's not uncommon. Try again."と投げる。
'''

b2_rock_musician        .action+=["Stay silent for hours in the recording booth until you feel the best to record (Sambo Master)", "Engaged in destructive behavior, including trashing hotel rooms (Keith Moon)", "Using small explosives to destroy drum sets during performances (Keith Moon)","Defecating on stage during performances (GG Allin)","Threatening to commit suicide during a set (GG Allin)"]
b2_singer               .action+=["Stay silent for hours in the recording booth until you feel the best to record (Sambo Master)"]
b2_classical_musician   .action+=[]
b2_comedian             .action+=["Arguing with the audience (George Carlin)", "Refused to perform in front of audiences that didn't understand his humor (Bill Hicks)", "Engaged in spontaneous, unscripted performances leading to chaotic shows (Robin Williams)"]
b2_novelist             .action+=["Became far-right and attempted a coup (Yukio Mishima)", "attempted suicide many times with women who were codependent on him (Osamu Dazai)"]
b2_artist               .action+=["Cutting off his own ear (Van Gogh)"]
b2_doctor               .action+=[]
b2_researcher           .action+=["Overthinking leads to pseudoscience (Linus Pauling)", "Believing in psychic phenomena (Edison)"]
b2_actor                .action+=["Method acting unearths trauma and leads to psychosis (Edward Montgomery Clift)"]
b2_chef                 .action+=[]
b2_athlete              .action+=["Biting opponents during matches (Luis Suarez)", "Refused to leave the pool for hours, obsessively practicing strokes until his hands bled (Michael Phelps)"]
b2_violent_criminal     .action+=[]
b2_cyber_criminal       .action+=[]
b2_thief                .action+=[]
b2_examinee             .action+=[]
b2_gambler              .action+=["Hundreds of hours spent observing roulette wheel deflection at casinos (Joseph Jagger)"]
b2_progamer             .action+=[]
b2_teacher              .action+=[]
b2_farmer               .action+=[]
b2_livestock_farmer     .action+=[]
b2_director             .action+=["Try to destroy a house that gets in the way of filming (Akira Kurosawa)", "Held the cast at gunpoint to get a performance he desired (Akira Kurosawa)"]
b2_model                .action+=[]
b2_guard                .action+=[]
b2_patient              .action+=[]
b2_the_dying            .action+=[]
b2_school_club_member   .action+=[]
b2_journalist           .action+=[] # "Pretended to be mentally ill to expose asylum conditions (Nellie Bly)"
b2_idol                 .action+=[]
b2_composer             .action+=[]
b2_dancer               .action+=[]
b2_barista              .action+=[]
b2_masseuse             .action+=[]
b2_hotel_staff          .action+=[]
b2_craftsman            .action+=[]
b2_photographer         .action+=[]

###########################################################################################################


b2_rock_musician        .slump+=[]
b2_singer               .slump+=["playing country music and rapping.", "Starts singing sexual songs with revealing clothes.","Making a rockabilly arrangement of one's past hits.","Releasing a Christmas album","Collaborating with a DJ on EDM tracks","Starring in a reality TV show about their family"]
b2_classical_musician   .slump+=[]
b2_comedian             .slump+=[ "Doing magic tricks", "Performing at retirement homes", "Attempting to become a motivational speaker"]
b2_novelist             .slump+=["Writing fan fiction", "Writing erotic novels", "Writing self-help books","Ghostwriting celebrity autobiographies"]
b2_artist               .slump+=["Use excrement and genital as motifs.", "Presenting a blank canvas or just trash as a work of art."]
b2_doctor               .slump+=[]
b2_researcher           .slump+=["Focusing on quantity over quality of publications","Engaging in pseudoscience or fringe theories","Becoming a paid consultant for industries related to their field","Writing popular science books that oversimplify complex topics","Appearing on sensationalist documentaries or TV shows"]
b2_actor                .slump+=["Starring in a low-budget movie with sharks", "Appearing on a TV shopping show"]
b2_chef                 .slump+=["Start serving curry with superficial knowledge", "Serve trendy food with superficial knowledge","Opening a food truck","Starting a catering business"]
b2_athlete              .slump+=["Endorsing questionable health products or fad diets", "Appearing on reality TV shows", "Becoming a motivational speaker for corporate events","Trying to switch to another sport."]
b2_violent_criminal     .slump+=[]
b2_cyber_criminal       .slump+=[]
b2_thief                .slump+=[]
b2_examinee             .slump+=[]
b2_gambler              .slump+=[]
b2_progamer             .slump+=[]
b2_teacher              .slump+=[]
b2_farmer               .slump+=[]
b2_livestock_farmer     .slump+=[]
b2_director             .slump+=[]
b2_model                .slump+=[]
b2_guard                .slump+=[]
b2_patient              .slump+=[]
b2_the_dying            .slump+=[]
b2_school_club_member   .slump+=[]
b2_journalist           .slump+=[]
b2_idol                 .slump+=[]
b2_composer             .slump+=["Writing jingles for commercials","Composing background music for elevators or shopping malls","Creating ringtones for mobile phones","Writing simple pop songs under a pseudonym","Arranging covers of popular songs for wedding bands","Composing music for children's TV shows","Creating soundtracks for low-budget indie games","Writing theme songs for local businesses","Producing generic stock music for video content","Composing music for fitness classes or guided meditations"]
b2_dancer               .slump+=[]
b2_barista              .slump+=[]
b2_masseuse             .slump+=[]
b2_hotel_staff          .slump+=[]
b2_craftsman            .slump+=[]
b2_photographer         .slump+=[]


###########################################################################################################
# さらば青春の光　猿回しでどうやってスベる
b2_rock_musician        .fail+=["Wrong note", "Forgetting lyrics"]
b2_singer               .fail+=["Wrong note", "Forgetting lyrics"]
b2_classical_musician   .fail+=["Wrong note"]
b2_comedian             .fail+=["Bombing", "Forgetting lines"]
b2_novelist             .fail+=["Plot hole", "Negative review"]
b2_artist               .fail+=[]
b2_doctor               .fail+=["Misdiagnosis"]
b2_researcher           .fail+=["Paper rejection"]
b2_actor                .fail+=["Retake"]
b2_chef                 .fail+=["Burning food"]
b2_athlete              .fail+=["Flying", "Getting hurt"]
b2_violent_criminal     .fail+=["Being grabbed by passers-by"]
b2_cyber_criminal       .fail+=[]
b2_thief                .fail+=["Being grabbed by passers-by"]
b2_examinee             .fail+=[]
b2_gambler              .fail+=[]
b2_progamer             .fail+=[]
b2_teacher              .fail+=[]
b2_farmer               .fail+=[]
b2_livestock_farmer     .fail+=[]
b2_director             .fail+=[]
b2_model                .fail+=[]
b2_guard                .fail+=[]
b2_patient              .fail+=[]
b2_the_dying            .fail+=[]
b2_school_club_member   .fail+=[]
b2_journalist           .fail+=[]
b2_idol                 .fail+=[]
b2_composer             .fail+=[]
b2_dancer               .fail+=[]
b2_barista              .fail+=[]
b2_masseuse             .fail+=[]
b2_hotel_staff          .fail+=[]
b2_craftsman            .fail+=[]
b2_photographer         .fail+=[]


###########################################################################################################

b2_                   .pressure_emergency+=[]
b2_rock_musician      .pressure_emergency+=["Sudden Vacancy"]
b2_singer             .pressure_emergency+=["Sudden Vacancy"]
b2_classical_musician .pressure_emergency+=["Sudden Vacancy"]
b2_comedian           .pressure_emergency+=["Sudden Vacancy"]
b2_novelist           .pressure_emergency+=["Ghost Writer"]
b2_artist             .pressure_emergency+=[]
b2_doctor             .pressure_emergency+=["Sudden Vacancy", "Suddenly ill", "Zombie pandemic", "Triage"]
b2_researcher         .pressure_emergency+=["Bomb Defusal", "Death Game", "Zombie Pandemic", "Mystery Deduction"]
b2_actor              .pressure_emergency+=["Sudden Vacancy"]
b2_chef               .pressure_emergency+=["Sudden Vacancy"]
b2_athlete            .pressure_emergency+=["Sudden Vacancy", "Life Saving Scene", "Death Game", "Zombie Pandemic"]
b2_school_club_member .pressure_emergency+=["Sudden Vacancy", "Life Saving Scene", "Death Game", "Zombie Pandemic"]
b2_violent_criminal   .pressure_emergency+=["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"]
b2_cyber_criminal     .pressure_emergency+=["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"]
b2_thief              .pressure_emergency+=["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"]
b2_progamer           .pressure_emergency+=[]
b2_gambler            .pressure_emergency+=[]
b2_examinee           .pressure_emergency+=[]
b2_teacher            .pressure_emergency+=[]
b2_craftsman          .pressure_emergency+=[]
b2_farmer             .pressure_emergency+=[]
b2_director           .pressure_emergency+=[]
b2_model              .pressure_emergency+=[]
b2_guard              .pressure_emergency+=["Death Game", "Zombie Pandemic", "Undercover Operation"]
b2_patient            .pressure_emergency+=[]
b2_the_dying          .pressure_emergency+=[]
b2_journalist         .pressure_emergency+=["Undercover Operation"]
b2_idol               .pressure_emergency+=[]
b2_composer           .pressure_emergency+=[]
b2_livestock_farmer   .pressure_emergency+=[]
b2_dancer             .pressure_emergency+=[]
b2_barista            .pressure_emergency+=[]
b2_masseuse           .pressure_emergency+=[]
b2_hotel_staff        .pressure_emergency+=[]
b2_photographer       .pressure_emergency+=[]
b2_delinquent         .pressure_emergency+=[]



###########################################################################################################

rephrase_singer             = []
rephrase_classical_musician = []
rephrase_rock_musician      = []
rephrase_comedian           = []
rephrase_writer             = []
rephrase_artist             = []
rephrase_doctor             = []
rephrase_researcher         = []
rephrase_actor              = []
rephrase_chef               = []
rephrase_athlete            = []
rephrase_violent_criminal   = []
rephrase_cyber_criminal     = []
rephrase_thief              = []

rephrase_examinee           = []
rephrase_gambler            = []
rephrase_progamer           = []
rephrase_teacher            = []
rephrase_farmer             = []
rephrase_director           = [] # ■■■
rephrase_model              = []
rephrase_guard              = []
rephrase_patient            = []
rephrase_the_dying            = []
rephrase_school_club_member = []
rephrase_journalist         = []
rephrase_idol               = []

rephrase_composer           = []
rephrase_livestock_farmer   = []
rephrase_dancer             = []
rephrase_barista            = []
rephrase_masseuse           = []
rephrase_hotel_staff        = []
rephrase_photographer       = []
rephrase_delinquent         = []
# s_rephrase lists depend on the hypo_i

###########################################################################################################



universal_rephrase = { # [print(f"If competence people do, that's {i.values()}. If incompetence people do, that's {i.keys()}") for i in universal_rephrase]
 "Unemployment":"Retirement"
,("Trip", "vacation"):"Study Trip"
,"Injury":"Work-related injury"
,("Being a NEET", "hobby"):"Working"
,"Gathering": ["Team up", "Meeting", "Discussion"]
} # Add new items without any explanations. Start answer with ```python

rephrase_ = universal_rephrase

'''
# Start answer with ```python. Each value in rephrase dicts should be a real word, not an invented word.
chef_v_mcdonalds_employee               = {"rephrase_dict_name": "chef_v_mcdonalds_employee"                # comedy script. A McDonald's employee, meets his girlfriend's parents and misleads them into thinking his occupation is high-end restraunt chef, a higher social occupation by rephrasing.
    ,"French fry": "French cuisine", "Patty": "Steak", "Teriyaki Burger": "Japanese cuisine", "Happy meal": "Full course meal", "McDonald's employee": "Chef", "McDonald's": "Restaurant", "Cashier": "Maitre d' station", "Part-time worker": "Apprentice"
    }
progamer_v_rock_paper_scissors_player   = {"rephrase_dict_name": "progamer_v_rock_paper_scissors_player"    # comedy script. A rock-paper-scissors player, meets his girlfriend's parents and misleads them into thinking his occupation is progamer, a higher social occupation by rephrasing.
    ,"Rock paper scissors": ("PvP game", "Luck based", "RNG"), ("Hand", "Throw"): ("Input commands", "Mix-Up", "Move", "Input"), "Win": "Kill", "Player": ("Casual player", "Beginner", "Noob"), "Win rate": "K/D", "rock can beat paper": "rock is meta of paper", "Rule": ("Metagame", "環境"), "Loosing": "Feeding", "Hand shape": "UI", "Opponent": "Enemy"
    }
actor_v_porn_star                       = {"rephrase_dict_name": "actor_v_porn_star"                        # comedy script. A porn star, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"Porn star": "Actor", "Fuck": "Act", ("Adult film", "Porn"): ("Movie", "Romance movie", "Art", "PG-rated movie"), "Sex scene": ("Romance scene", "Bed time scene"), "Fluffer": "Assistant", ("Money shot", "Cum shot", "Bukkake"): ("Climactic moment", "Final act"), "Facial": "Makeup application", ("Gangbang", "Orgy"): ("Ensemble cast", "Large cast scene"), "squirter": ("Side character", "Extra"), ("Dildo", "Sex toy"): "Prop", "Bukkake": "Group performance", "Creampie": "Plot twist", "Undercover porn": "Suspence movie", "BDSM": ("Violence action", "Psycho thriller"), "Solo tease": "monodrama", "Medieval": "Epic drama", "Nurse porn": "Medical drama"
    }

cancer_patient_v_lice_patient     = {"rephrase_dict_name": "cancer_patient_v_lice_patient"                  # comedy script. A lice sufferer exaggerates his symptoms in an attempt to gain sympathy.
    ,"Shaving": ("Treatment", "Invasion"), "Scalp": ("Head area", "Crown"), "Lice removal": "Extraction", "Pubic hair": "Affected tissue", "Lice shampoo": "Chemical therapy",
    }


Add new items in cancer_patient_v_pubic_lice_patient. No explanations. Start answer with ```python

define cancer_patient_v_pubic_lice_patient. No explanations. Start answer with ```python


'''

# Start answer with ```python. Each value in rephrase dicts should be a real word, not an invented word.

chef_v_mcdonalds_employee               = {"rephrase_dict_name": "chef_v_mcdonalds_employee"                # comedy script. A McDonald's employee, meets his girlfriend's parents and misleads them into thinking his occupation is high-end restraunt chef, a higher social occupation by rephrasing.
    ,"French fry": "French cuisine", "Patty": "Steak", "Teriyaki Burger": "Japanese cuisine", "Happy meal": "Full course meal", "McDonald's employee": "Chef", "McDonald's": "Restaurant", "Cashier": "Maitre d' station", "Part-time worker": "Apprentice"
    }
progamer_v_rock_paper_scissors_player   = {"rephrase_dict_name": "progamer_v_rock_paper_scissors_player"    # comedy script. A rock-paper-scissors player, meets his girlfriend's parents and misleads them into thinking his occupation is progamer, a higher social occupation by rephrasing.
    ,"Rock paper scissors": ("PvP game", "Luck based", "RNG"), ("Hand", "Throw"): ("Input commands", "Mix-Up", "Move", "Input"), "Win": "Kill", "Player": ("Casual player", "Beginner", "Noob"), "Win rate": "K/D", "rock can beat paper": "rock is meta of paper", "Rule": ("Metagame", "環境"), "Loosing": "Feeding", "Hand shape": "UI", "Opponent": "Enemy"
    }
actor_v_porn_star                       = {"rephrase_dict_name": "actor_v_porn_star"                        # comedy script. A porn star, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"Porn star": "Actor", "Fuck": "Act", ("Adult film", "Porn"): ("Movie", "Romance movie", "Art", "PG-rated movie"), "Sex scene": ("Romance scene", "Bed time scene"), "Fluffer": "Assistant", ("Money shot", "Cum shot", "Bukkake"): ("Climactic moment", "Final act"), "Facial": "Makeup application", ("Gangbang", "Orgy"): ("Ensemble cast", "Large cast scene"), "squirter": ("Side character", "Extra"), ("Dildo", "Sex toy"): "Prop", "Bukkake": "Group performance", "Creampie": "Plot twist", "Undercover porn": "Suspence movie", "BDSM": ("Violence action", "Psycho thriller"), "Solo tease": "monodrama", "Medieval": "Epic drama", "Nurse porn": "Medical drama"
    }
journalist_v_tabloid_writer             = {"rephrase_dict_name": "journalist_v_tabloid_writer"              # comedy script. A tabloid writer, meets his girlfriend's parents and misleads them into thinking his occupation is journalist, a higher social occupation by rephrasing.
    ,("rumor", "lie"): "unconfirmed source", "tabloid": ("news", "report"), "SNS": ("grapevine", "authority"), "Checking SNS": ("researching", "fieldwork"), "paparazzi": "reporter"
    }
actor_v_karaoke_background_video_actor  = {"rephrase_dict_name": "actor_v_karaoke_background_video_actor"   # comedy script. A karaoke background video actor, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"Karaoke background video": "Short film","When a musician's song is playing, your image will be played on the karaoke machine": "Co-starring"
}
athlete_v_progamer                      = {"rephrase_dict_name": "athlete_v_progamer"                       # comedy script. A progamer, meets his girlfriend's parents and misleads them into thinking his occupation is athlete, a higher social occupation by rephrasing.
    ,"progamer": "athlete", "e-sports": "indoor sports", "tenosynovitis": "ligament injury"
}
cancer_patient_v_lice_patient     = {"rephrase_dict_name": "cancer_patient_v_lice_patient"                  # comedy script. A lice sufferer exaggerates his symptoms in an attempt to gain sympathy.
    ,"Shaving": ("Treatment", "Invasion"), "Scalp": ("Head area", "Crown"), "Lice removal": "Extraction", "Pubic hair": "Affected tissue", "Lice shampoo": "Chemical therapy",
    }

'''
cancer_patient_v_frailty                = {"rephrase_dict_name": "cancer_patient_v_frailty"                # comedy script. A frailty man, meets his girlfriend's parents and misleads them into thinking he is cancer patient. He wants to be a tragic character to gain sympathy.
    ,"":""
}
'''



# Add new items in cancer_patient_v_frailty. Respond with only the new items.


athlete_v_billiards_player              = {"rephrase_dict_name": "athlete_v_billiards_player"               #
    ,"billiards player": "athlete", "billiards": "indoor sports", "table": "field", "pool hall": "arena"
}






# Add new items in athlete_v_progamer

rephrase_journalist     += [ # comedy script. rephrases performed by a tabloid writer who has a complex with journalists.
    "[rumor, lie], [unconfirmed source]", "[tabloid], [news, report]", "[SNS], [grapevine, authority]", "[Checking SNS], [researching, fieldwork]", "[paparazzi], [reporter]"
]


rephrase_chef           += [# comedy script. rephrases performed by a McDonald's employee who has a complex with high-end restaurant chefs.
    "[French fry], [French cuisine]", "[Patty], [Steak]", "[Teriyaki Burger], [Japanese cuisine]", "[Happy Meal], [Full course meal]", "[McDonald's employee], [Chef]", "[McDonald's], [restaurant]", "[Cashier], [Maitre d' station]", "[Part-time worker], [Apprentice]"
]

rephrase_progamer       += [# comedy script. rephrases performed by a rock-paper-scissors player who has a complex with progamers.
    "[rock paper scissors], [PvP game]", "[Rock paper scissors], [Luck based]", "[Hand], [Input commands]", "[Win], [Kill]", "[Player], [Casual player]", "[Win rate], [K/D]", "[Rock can beat paper], [Rock is meta of paper]", "[Rock loses to paper, paper loses to scissors, and scissors loses to rock], [Metagame, Rule, 環境]", "[Luck], [RNG]", "[Losing], [Feeding]", "[Throw], [Input]", "[Hand shape], [UI]", "[Opponent], [Enemy]", "[Beginner], [Noob]"
]

rephrase_actor          += [ # comedy script. rephrases performed by a porn star who has a complex with actors.
    "[porn], [romance]", "[having sex], [love scene]", "[undercover porn], [suspense movie]", "[BDSM], [violence action]", "[BDSM], [psycho thriller]", "[porn star], [actor]", "[porn], [PG-rated movie]", "[adult film], [indie film]", "[porn star], [co-actor]", "[money shot], [climactic scene]", "[fluffer], [production assistant]","[squirter], [side character]", "[squirter], [extra]", "[solo tease], [monodrama]", "[medieval], [epic drama]", "[nurse], [medical dramas]", "[cum shot], [final scene]", "[gangbang], [ensemble cast]", "[dildo], [prop]"
]



# Add new rephrases in rephrase_journalist


rephrase_director       += rephrase_actor


rephrase_writer         +=[ # "Ali, a tabloid writer, feels inferior to novelists, so he speaks like a novelist. Ali calls [0] [1]. Ali hides the fact that he is a tabloid writer and pretends to be a novelist."
    ["lying", "creation"],["gossip", "character development"],["clickbait", "hook"],["expose", "revealing chapter"],["tabloid", "literary work"],["lie", "fiction"],["lie", "fantasy"],["fabrication","dramatization"], ["tabloid writer", "novelist"], ["tabloid writer", "creator"]
]

rephrase_athlete        +=[ # "Ali, a e-sports player, feels inferior to athletes, so he speaks like a athlete. Ali calls [0] [1]. Ali hides the fact that he is an e-sports player and pretends to be an athlete."
    ["e-sports", "indoor sports"], ["tenosynovitis", "ligament injury"]
]



# Add new 10 pairs in rephrase_comedian in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

rephrase_singer         +=[ # "Ali, a back chorus, feels inferior to vocalists, so he speaks like a vocalist. Ali calls [0] [1]."
    ["back chorus", "lead vocalist"], ["singing as a back chorus", "performing"]
]

rephrase_athlete        +=[ # "Ali, a billiards player, feels inferior to athletes, so he speaks like an athlete. Ali calls [0] [1]."
    ["billiards", "indoor sports"], ["billiards players", "athletes"], ["table", "field"], ["pool hall", "arena"],
]

rephrase_comedian       +=[ # "Ali, a hospital clown, feels inferior to comedians, so he speaks like a comedian. Ali calls [0] [1]."
    ["clown makeup", "hook"], ["magic tricks", "misdirection"],["hospital clown", "comedian"],["funny faces", "punch line"],["stage", "hospital"],["病院", "ハコ"] # 終末病棟 客が重い
]

rephrase_gambler        +=[ # "Ali, a coin pusher player, feels inferior to gamblers, so he speaks like a gambler. Ali calls [0] [1]."
    ["coin", "chip"],["pushing coins", "placing bets"],["coin stack", "pot"],["prize", "payout"],["game over", "bust"],
]

rephrase_classical_musician+=[ # "Ali, a cymbalist, feels inferior to normal instrumentalists, such as pianists and violinists. so he speaks like an instrumentalist. Ali calls [0] [1]."
    ["crash", "crescendo"],["hitting cymbals", "performing"],["cymbal stand", "instrument stand"],["cymbal bag", "instrument case"],["cymbal polish", "instrument maintenance"],
]

rephrase_violent_criminal       +=[ # "Ali, a petty criminal, feels inferior to famous criminals, so he speaks like a famous criminal. Ali calls [0] [1]."
    ["shoplifting", "looting"], ["County Sheriff", "State power"],["arrest", "capture"],["parole", "clemency"],["forced to wear a GPS ankle strap.", "monitored by satellite."]
]

rephrase_cyber_criminal  +=[ # Ali, a wannabe of cracker, feels inferior to famous crackers.
    ["Illegal download, spamming", "cyber attack"], ["", ""]
]

# Define rephrase_cybercriminal


###########################################################################################################

# Listed below are some examples of how negative concepts have been elegantly rephrased in the media.
# Define rephrase_novelist list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.



# for i in rephrase_lists:
#  print(f"comedy script : If incompetence people do, it's {i[0]}; if competence people do, it's just {i[0]}.")

rephrase_rock_musician  +=[
 ["drug addiction, crime, arrest, dispute", "rock'n'-roll, scandal, inspiration, rebellion, charisma"]
,["drug addiction", "chemical muse"]
,["unemployment", "retirement, career transition"]
,["self-neglect, self-harm", "rock'n'-roll"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["mental illness, authism", "rock'n'-roll, charisma"]
,["infidelity", "passionate love, romantic scandal"]
,["mental illness", "artistic temperament"]
]

rephrase_athlete        +=[
 ["injury", "badge, medal"]
,["doping", "performance enhancement"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["trip", "training camp"]
,["exercise, leisure, hobby, recreation, healthy living, fitness", "training, sport, match"]
,["being friendly", "teamwork"]
,["gathering", "team activity"]
,["outing", "field experience, match, sport"]
,["friend", "team member"]
,["bodily punishment", "assault"]
]

rephrase_school_club_member +=[
 ["trip", "training camp"]
,["exercise, leisure, hobby, recreation, healthy living, fitness", "training, sport, match"]
,["being friendly", "teamwork"]
,["gathering", "team activity, discussion"]
,["outing", "field experience, match, sport"]
,["friend", "team member"]
,["bodily punishment", "assault"]
]

rephrase_actor += [
 ["weight gain", "method acting, character transformation"]
,["plastic surgery", "career investment, image enhancement"]
,["typecasting", "signature role, iconic performance"]
,["unemployment", "selective career choices, between projects"]
,["public meltdown", "passionate outburst, intense emotion"]
,["scandal", "publicity, career-defining moment"]
,["rehab", "personal growth journey, career reset"]
,["aging", "seasoned performer, distinguished veteran"]
,["divorce", "high-profile romance, tabloid sensation"]
,["paparazzi altercation", "defending privacy, standing up to media intrusion"]
]



# Put a casual word in [0] and a classy word in [1]. e.g. If pro teams do, it's team activity, if amateur team do, it's just gathering.
# Extend 10 new items to rephrase_school_club_member list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.

rephrase_journalist += [
    ["libel, stalking, hacking, voyeurism, harassment", "reporting"],
]

rephrase_researcher     +=[
 ["scholarship", "debt"]
,["unemployment", "retirement, career transition"]
,["failure, mistake", "learning experience, growth opportunity"]
,["psychopass", "charisma, genius"]
]

rephrase_writer         +=[
 ["depression, anxiety", "writer's block, slump"]
,["mental illness", "artistic temperament, charisma"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
]




# ,["obsession", "dedication"],["recklessness", "fearless approach"]





# for i in rephrase_lists:
#  print(f"comedy script : If competence people do, it's {i[1]}; if incompetence people do, it's just {i[0]}.")


# Add new 20 ones.

###########################################################################################################

"""
@dataclass
class GarnishIv:
    garnishiv:list

giv_researcher  =GarnishIv([])
giv_farmer      =GarnishIv([])
giv_student     =GarnishIv([])
giv_delinquent  =GarnishIv([])

# Add new items without any explanations. Start answer with ```python

# How they are evaluated
giv_researcher  .partially_go=[]
giv_farmer      .partially_go=[]
giv_student     .partially_go=["Submit assignments", "Attend classes", "Have good grades"]
giv_delinquent  .partially_go=["Strong in fights", "Lack ethics", giv_student.partially_g]

# Should be noun
giv_researcher  .different_ep=["Mad scientist"]
giv_farmer      .different_ep=["Bumpkin"]
giv_student     .different_ep=["Serious", "Grind"]
giv_delinquent  .different_ep=["Unethical", "Delinquent"]

# How their personality downfall
giv_researcher  .different_do=["Be shut up in an ivory", "Have too high IQ"] # if mentally_work: self.different_do.append("Have too high IQ")
giv_farmer      .different_do=["Be a bumpkin"]
giv_student     .different_do=["Studied too much"]
giv_delinquent  .different_do=["Abused drugs"]

# What kind of prompt for attribute for frequently_verbal is good?
giv_researcher  .frequently_ve=[]
giv_farmer      .frequently_ve=[]
giv_student     .frequently_ve=[]
giv_delinquent  .frequently_ve=[] # You've been disrupting classes for three years.

"""


###########################################################################################################
###########################################################################################################
@dataclass
class FactAgentEasa:
  ALL_FACTAGENTEASA: ClassVar[List['FactAgentEasa']] = []
  z_Binary2: Binary2
  z_rephrase: list

  def __post_init__(self):
    FactAgentEasa.ALL_FACTAGENTEASA.append(self)

easa_singer                =FactAgentEasa(b2_singer              , rephrase_singer             )
easa_classical_musician    =FactAgentEasa(b2_classical_musician  , rephrase_rock_musician      )
easa_rock_musician         =FactAgentEasa(b2_rock_musician       , rephrase_classical_musician )
easa_comedian              =FactAgentEasa(b2_comedian            , rephrase_comedian           )
easa_writer                =FactAgentEasa(b2_novelist            , rephrase_writer             )
easa_artist                =FactAgentEasa(b2_artist              , rephrase_                   )
easa_doctor                =FactAgentEasa(b2_doctor              , rephrase_                   )
easa_researcher            =FactAgentEasa(b2_researcher          , rephrase_                   )
easa_actor                 =FactAgentEasa(b2_actor               , rephrase_actor              )
easa_chef                  =FactAgentEasa(b2_chef                , rephrase_chef               )
easa_athlete               =FactAgentEasa(b2_athlete             , rephrase_athlete            )
easa_criminal              =FactAgentEasa(b2_violent_criminal    , rephrase_violent_criminal   )
easa_examinee              =FactAgentEasa(b2_examinee            , rephrase_                   )
easa_student               =FactAgentEasa(b2_examinee            , rephrase_                   )
easa_gambler               =FactAgentEasa(b2_gambler             , rephrase_                   )
easa_progamer              =FactAgentEasa(b2_progamer            , rephrase_progamer           )
easa_teacher               =FactAgentEasa(b2_teacher             , rephrase_                   )
easa_farmer                =FactAgentEasa(b2_farmer              , rephrase_                   )
easa_livestock_farmer      =FactAgentEasa(b2_livestock_farmer    , rephrase_                   )
easa_director              =FactAgentEasa(b2_director            , rephrase_director           )
easa_model                 =FactAgentEasa(b2_model               , rephrase_model              )
easa_guard                 =FactAgentEasa(b2_guard               , rephrase_guard              )
easa_patient               =FactAgentEasa(b2_patient             , rephrase_patient            )
easa_the_dying             =FactAgentEasa(b2_the_dying           , rephrase_the_dying          )
easa_school_club_member    =FactAgentEasa(b2_school_club_member  , rephrase_school_club_member )
easa_journalist            =FactAgentEasa(b2_journalist          , rephrase_journalist         )
easa_cybercriminal         =FactAgentEasa(b2_cyber_criminal      , rephrase_cyber_criminal     )
easa_thief                 =FactAgentEasa(b2_thief               , rephrase_thief              )
easa_composer              =FactAgentEasa(b2_composer            , rephrase_composer           )
easa_dancer                =FactAgentEasa(b2_dancer              , rephrase_dancer             )
easa_barista               =FactAgentEasa(b2_barista             , rephrase_barista            )
easa_masseuse              =FactAgentEasa(b2_masseuse            , rephrase_masseuse           )
easa_hotel_staff           =FactAgentEasa(b2_hotel_staff         , rephrase_hotel_staff        )
easa_photographer          =FactAgentEasa(b2_photographer        , rephrase_photographer       )
easa_delinquent            =FactAgentEasa(b2_delinquent          , rephrase_delinquent         )
easa_                      =FactAgentEasa(b2_                    , rephrase_                   )

