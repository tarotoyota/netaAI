
from dataclasses import dataclass, field
from typing import List, ClassVar

@dataclass
class Progression:
    ALL_PROGRESSION: ClassVar[List['Progression']] = []
    name:str
    ivfact_owner:list[str]
    example:list[str]
    description_broad:str
    description_format:str

    necessity   :str = ""
    agent       :str = ""
    norm        :str = ""
    object      :str = ""
    adjective   :str = ""
    def __post_init__(self):
        Progression.ALL_PROGRESSION.append(self)




nel     = Progression("NEl" ,["FactNecessitySexual", "FactSex"]        , []
                      ,"ある者が、x.ivfactを実行する際、その必要性を欠く事で加害性が生じる脚本。"
                      ,"Ali, a {name} does {FaceNecessitySexual}, despite {cbsx_to_despite}.", necessity="l")
nol     = Progression("NOl" ,["FactNecessitySexual", "FactSex"]        , []
                      ,"ある者が、x.ivfactを実行する際、その方法が異常である事で加害性が生じる脚本。"
                      ,"Ali, a {name} does {FactNecessitySexual}, in the sexual ways, such as {FactSexual}.", norm="l")
agw     = Progression("AGw" ,["FactAgent", "FactNecessitySexual"]      , ["さらば青春の光: 女子高"]
                      ,"Agent xが、y.ivfactを実行する事で加害性が生じる脚本。"
                      ,"Ali, a {name} does {FactNecessitySexual}, but actually he is a {abn_hypo}.", agent="w")
agwm    = Progression("AGwm",["FactAgent"]      , ["アンジャッシュ: (全般)", "Plautus: Menaechmi"]
                      ,"Agent xであると誤解されている者が、y.ivfactを実行する事で加害性が生じる脚本。"
                      ,"Ali, a {name(1)} does {FactNecessitySexual}, but Bob mistakenly believes that Ali is a {name(2)}", agent="w(misidentify)")
agwia   = Progression("AGwia",["FactAgent"]      , ["さらば青春の光: 男優", "SNL: The Actress"]
                      ,"Agent xの、劣った、又はアブノーマルな下位分類が、Agent xの優れた、又はノーマルな下位分類のivfactを実行する事で加害性が生じる脚本。"
                      ,"Ali, a {name} does {stereos}, but actually he is a {hypo_i, abn_hypo}.", agent="w(inferior, abnormal)") 
agf     = Progression("AGf" ,["FactAgent"]      , ["ファイヤーサンダー: 透明人間の薬", "SNL: Rosetta Stone", "パンサー: 旅行の計画", "Kee and Peele: Alien", "ロビンフット: 結婚相手", "さらば青春の光: 後継者, 例の件: 無農薬農家, ニューヨーク: ファッション"]
                      ,"ある者が、それ自体が加害的であるAgent xである事により加害性が生じる脚本。"
                      ,"Ali is a {name}.", agent="f") 
obw     = Progression("OBw" ,["FactObject"]     , ["バイきんぐ: 野球用品"]
                      ,"ある者が、Object xに対し、y.ivfactを実行する事により加害性が生じる脚本。"
                      ,"Ali uses {FactObject1} as {FactObject2}", object="w") 
agflt   = Progression("AGflt",["FactAgent"]     , ["ロビンフット: 結婚相手", "ザ・ギース: 大人の階段"]
                      ,"ある者のAgent xとしての携行が強まる、または弱まる事により加害性が生じる脚本。"
                      ,"Ali does {FactTaper}Ali does {FactTaper}", agent="f, l, t") 



# slur, ugly, criminalは全てagentとして処理する

# Exclude corpus, Frequency corpusはProgressionではない

def progression_tablize_simple():
    col=""

    for i in Progression.ALL_PROGRESSION:
        col+=f"<tr><th>{i.name}</th><td>{i.necessity}</td><td>{i.agent}</td><td>{i.norm}</td><td>{i.object}</td><td>{i.adjective}</td><td>{', '.join(i.ivfact_owner)}</td><td>{i.example[0] if i.example else ''}</td><td>{i.description_broad}</td><td>{i.description_format}</td></tr>"

    table1=f"""<table>
    <tr><th>Name</th><th>NEcessity</th><th>AGent</th><th>NOrm </th><th>OBject </th><th>ADjective</th><th>Ivfact Owner</th><th>One Example</th><th>Broad Description</th></tr>
    {col}
    </table>"""

    table1+="""<table>
    <tr><th>Symbol  </th><th>Meaning                      </th></tr>
    <tr><td>l       </td><td>Should exist, but is lacking.</td></tr>
    <tr><td>f       </td><td>Should not exist; Forbidden. </td></tr>
    <tr><td>w       </td><td>Is wrong by normal standards.</td></tr>
    </table>"""

    return ''.join(table1)

html_content = progression_tablize_simple()
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_content)