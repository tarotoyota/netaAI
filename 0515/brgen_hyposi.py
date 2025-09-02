from inst_factagent import*

def func_brgen_hyposi(arg: FactAgent):
    x=[]
    if arg.z_factagenteasa:
        for i in arg.z_factagenteasa:
            x.append(i.z_Binary2.action)
    if x:
        print(f'''** Fast assignment of Ali's past actions **

1. The script will have a very short air time. Rapidly pack in the information that Ali has performed the actions in the list X. 
2. Select actions from the list X for X1 to X3. You can get a high score by assigning two actions per line.
3. Adapt the dialogue to suit X1 to X3. 

X = {x}
              
dialogue = """ 
Line1: [Ali mentions about he did {{X1}}]
Line2: [Bob blames Ali for doing {{X2}}]
Line3: [Ali ignores it or is defensive about it. Then mentions about he did {{X3}}]
Line4: [Bob says 'Cut it out!']
"""

answer_example = """

X1="Uses dead animals in performances" + "Hold solo event"
X2="Become interested in devil worship or Nazism" + "Addict drugs"
X3="Hate commercialism" + "Writing songs about personal struggles"

Ali: Shut up, I'm busy! I'm thinking about how to use a pig carcass at the next solo event now!
Bob: Stop with such satanic performance. You've been acting crazy ever since you started using cocaine.
Ali: No! I don't make commercial music. My struggles are not for sale!
Bob: Cut it out!
"""''')
    
func_brgen_hyposi(atag_rock_musician)