import sys
lettere= "abcdefghijklmnopqrstuvwxyz"
play={}
pos1=""
pos2=""
pos3=""
rot={1:{
    'a': 'e', 'b': 'k', 'c': 'm', 'd': 'f', 'e': 'l',
    'f': 'g', 'g': 'd', 'h': 'q', 'i': 'v', 'j': 'z',
    'k': 'n', 'l': 't', 'm': 'o', 'n': 'w', 'o': 'y',
    'p': 'h', 'q': 'x', 'r': 'u', 's': 's', 't': 'p',
    'u': 'a', 'v': 'i', 'w': 'b', 'x': 'r', 'y': 'c',
    'z': 'j'
}, 2: {
    'a': 'a', 'b': 'j', 'c': 'd', 'd': 'k', 'e': 's',
    'f': 'i', 'g': 'r', 'h': 'u', 'i': 'x', 'j': 'b',
    'k': 'l', 'l': 'h', 'm': 'w', 'n': 't', 'o': 'm',
    'p': 'c', 'q': 'q', 'r': 'g', 's': 'z', 't': 'n',
    'u': 'p', 'v': 'y', 'w': 'f', 'x': 'v', 'y': 'o',
    'z': 'e'
},3:{
    'a': 'b', 'b': 'd', 'c': 'f', 'd': 'h', 'e': 'j',
    'f': 'l', 'g': 'c', 'h': 'p', 'i': 'r', 'j': 't',
    'k': 'x', 'l': 'v', 'm': 'z', 'n': 'n', 'o': 'y',
    'p': 'e', 'q': 'i', 'r': 'w', 's': 'g', 't': 'a',
    'u': 'k', 'v': 'm', 'w': 'u', 'x': 's', 'y': 'q',
    'z': 'o'
},4:{
    'a': 'e', 'b': 's', 'c': 'o', 'd': 'v', 'e': 'p',
    'f': 'z', 'g': 'j', 'h': 'a', 'i': 'y', 'j': 'q',
    'k': 'u', 'l': 'i', 'm': 'r', 'n': 'h', 'o': 'x',
    'p': 'l', 'q': 'n', 'r': 'f', 's': 't', 't': 'g',
    'u': 'k', 'v': 'd', 'w': 'c', 'x': 'm', 'y': 'w',
    'z': 'b'
},5:{
    'a': 'v', 'b': 'z', 'c': 'b', 'd': 'r', 'e': 'g',
    'f': 'i', 'g': 't', 'h': 'y', 'i': 'u', 'j': 'p',
    'k': 's', 'l': 'd', 'm': 'n', 'n': 'h', 'o': 'l',
    'p': 'x', 'q': 'a', 'r': 'w', 's': 'm', 't': 'j',
    'u': 'q', 'v': 'o', 'w': 'f', 'x': 'e', 'y': 'c',
    'z': 'k'
} }

riflettore = {
    'a': 'y',
    'b': 'r',
    'c': 'u',
    'd': 'h',
    'e': 'q',
    'f': 's',
    'g': 'l',
    'h': 'd',
    'i': 'p',
    'j': 'x',
    'k': 'o',
    'l': 'g',
    'm': 'n',
    'n': 'm',
    'o': 'k',
    'p': 'i',
    'q': 'e',
    'r': 'b',
    's': 'f',
    't': 'w',
    'u': 'c',
    'v': 'z',
    'w': 't',
    'x': 'j',
    'y': 'a',
    'z': 'v'
}

def gira(dic1,dic2,dic3,count1,count2,count3):
    dicc1=dic1.copy()
    dicc2=dic2.copy()
    dicc3=dic3.copy()
    for n, char in enumerate(lettere):      
        dic1[char]=dicc1[lettere[(n+1)%26]]
    count1+=1
    if count1==26:
        count1=0
        for n, char in enumerate(lettere):
                 dic2[char]=dicc2[lettere[(n+1)%26]]
        count2+=1
    if count2 ==26:
         for n, char in enumerate(lettere):
                  dic3[char]=dicc3[lettere[(n+1)%26]]
         count3+=1
         count2=0
    if count3==26:
        count3=0
    return(dic1,dic2,dic3,count1,count2,count3)
    
def ordina(dic1,dic2,dic3,pos1,pos2,pos3):
    
    for chiave, valore in dic1.items():
            if valore==pos1:
                break
    imp2=lettere.index(chiave)
    dic=dic1.copy()
    for char in lettere:
         dic1[char]=dic[lettere[imp2%26]]
         imp2+=1

    for chiave, valore in dic2.items():
                if valore==pos2:
                    break
    imp2=lettere.index(chiave)
    dic=dic2.copy()
    for char in lettere:
             dic2[char]=dic[lettere[imp2%26]]
             imp2+=1
    for chiave, valore in dic3.items():
                if valore==pos3:
                    break
    imp2=lettere.index(chiave)
    dic=dic3.copy()
    for char in lettere:
             dic3[char]=dic[lettere[imp2%26]]
             imp2+=1

def enigma(dic1,dic2,dic3,text,riflettore,pos1,pos2,pos3,play):
    dic1=dic1.copy()
    dic2=dic2.copy()
    dic3=dic3.copy()
    finale=[]
    count1,count2,count3=0,0,0
    ordina(dic1,dic2,dic3,pos1,pos2,pos3)
    for char in text:
        
        dic1,dic2,dic3,count1,count2,count3=gira(dic1,dic2,dic3,count1,count2,count3)
        final=playground(char,play)
        final=dic1[final]
        final=dic2[final]
        final=dic3[final]
        final=riflettore[final]
        for chiave, valore in dic3.items():
            if valore==final:
                final=chiave
                break
        
        for chiave, valore in dic2.items():
                    if valore==final:
                        final=chiave
                        break
        for chiave, valore in dic1.items():
                    if valore==final:
                        final=chiave
                        break
        final=playground(final,play)
        finale.append(final)
    text="".join(finale)
    return(text)
def playground(char, play):
    for chiave, valore in play.items():
        if valore==char:
            final=chiave
            break
        elif chiave==char:
             final=valore
             break
        else:
            final=char
    return(final)
def menu():
     print(r"""    _______   ______________  ______      ______  __
   / ____/ | / /  _/ ____/  |/  /   |    / __ \ \/ /
  / __/ /  |/ // // / __/ /|_/ / /| |   / /_/ /\  / 
 / /___/ /|  // // /_/ / /  / / ___ |_ / ____/ / /  
/_____/_/ |_/___/\____/_/  /_/_/  |_(_)_/     /_/   
                                                    """)
def main():
    menu()
    let=""
    text=input("inserisci un testo: ")
    text="".join(c for c in text.casefold() if c in lettere)
  
    try:
            n=int(input("quale deve essere il primo rotore? "))
            dic1=rot[n]
            
    except:
              sys.exit("Coglione, deve essere UN NUMERO da 1 A 5!! ")
    
    del rot[n]
    while n not in rot:
            try:
                n=int(input("quale deve essere il secondo rotore? "))
            except:
                  sys.exit("Coglione, deve essere UN NUMERO!! ")
    dic2=rot[n]
    del rot[n]
    while n not in rot:
                    try:
                        n=int(input("quale deve essere il terzo rotore? "))
                    except:
                          sys.exit("Coglione, deve essere UN NUMERO!! ")
    dic3=rot[n]
    pos1="@@"
    pos2="@#"
    pos3="@#"
    while pos1 not in lettere or len(pos1)!=1:
        pos1=input("prima posizione del primo rotore: ").casefold()
    while pos2 not in lettere or len(pos2)!=1:
        pos2=input("prima posizione del secondo rotore: ").casefold()
    while pos3 not in lettere or len(pos3)!=1:
        pos3=input("prima posizione del terzo rotore: ").casefold()
    for i in range(6): 
         while True :
            let=input(f"1° lettera del collegamento numero {i+1}/6").casefold()
            if let not in play and let not in play.values() and let in lettere and len(let)==1:
                  break
         while True:
            let2=input(f"2° lettera del collegamento numero {i+1}/6").casefold()
            if let2 not in play and let2 not in play.values() and let2!=let and let2 in lettere and len(let2)==1:
                  break
         play[let]=let2
    testo=enigma(dic1,dic2,dic3, text,riflettore,pos1,pos2,pos3, play)
    print(testo)

if __name__=="__main__":
    main()



