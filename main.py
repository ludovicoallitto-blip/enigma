import sys
from collections import Counter
lettere= "abcdefghijklmnopqrstuvwxyz"
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
    count1+=1
    if count1==27:
        count1=0
        count2+=1
    if count2 ==27:
         count3+=1
         count2=0
    if count3==27:
        count3=0
    for n, char in enumerate(lettere):
         dic1[char]=dic1[lettere[(n+1)%26]]
         dic2[char]=dic2[lettere[(n+1)%26]]
         dic3[char]=dic3[lettere[(n+1)%26]]
    return(dic1,dic2,dic3,count1,count2,count3)
    
def ordina(dic1,dic2,dic3,pos1,pos2,pos3):
    
    for chiave, valore in dic1.items():
            if valore==pos1:
                break
    imp2=lettere.index(chiave)
    dic=dic1
    for char in lettere:
         dic1[char]=dic[lettere[imp2]]
         imp2+=1

    for chiave, valore in dic2.items():
                if valore==pos2:
                    break
    imp2=lettere.index(chiave)
    dic=dic2
    for char in lettere:
             dic2[char]=dic[lettere[imp2]]
             imp2+=1
    for chiave, valore in dic3.items():
                if valore==pos3:
                    break
    imp2=lettere.index(chiave)
    dic=dic3
    for char in lettere:
             dic3[char]=dic[lettere[imp2]]
             imp2+=1

def enigma(dic1,dic2,dic3,text,riflettore,pos1,pos2,pos3):
    finale=[]
    count1,count2,count3=0,0,0
    ordina(dic1,dic2,dic3,pos1,pos2,pos3)
    for char in text:
        
        dic1,dic2,dic3=gira(dic1,dic2,dic3,count1,count2,count3)
        final=playground(char)
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
        final=playground(final)
        finale.append(final)
    text="".join(finale)
    return(text)
def playground(finale):
    if finale=="a":
        return("j")
    elif finale=="j":
        return("a")
    else:
        return(finale)

def main():
    text=input("inserisci un testo: ")
    text="".join(c for c in text.casefold() if c in lettere)
    n=int(input("quale deve essere il primo rotore? "))
    dic1=rot[n]
    del rot[n]
    while n not in rot:
        n=int(input("quale deve essere il secondo rotore? "))
    dic2=rot[n]
    del rot[n]
    while n not in rot:
            n=int(input("quale deve essere il secondo rotore? "))
    dic3=rot[n]
    testo=enigma(dic1,dic2,dic3, text,riflettore,pos1,pos2,pos3)
    print(testo)

if __name__=="__main__":
    main()
