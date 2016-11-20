from bintree import BinTree
import random   # Importerar funktionen random som slumpvis genererar ett tal
fil=open("word5", encoding="latin-1") 
ord=fil.readlines()
ordlista=[] # Skapar en tom ordlista
spegladeOrd=BinTree()  # Skapar ett träd som är tomt
wordTree=BinTree()  # Samma sak
nylista=[] # Skapar en till tom ordlista
for n in ord:  # Tar bort enter
    ordlista.append(n.rstrip("\n"))

def spegla(word): # Från lab 3 - inverterar ord (lazy asses we are)
    outputlist=[]
    output=""
    for letter in word:
        outputlist.append(letter)
    for n in range((len(outputlist)-1),-1,-1):
        output+=outputlist[n]
    return output


while len(ordlista)>0:  # ordlistan innehåller alla våra ord. Flyttar över orden i
    nylista.append(ordlista.pop(random.randrange(len(ordlista)))) # random ordning ett i taget

for word in nylista:  # Lägger in vår nya lista i trädet wordtree
    wordTree.put(word)

for word in nylista:  # För varje ord i nya listan, om det speglade ordet finns i wordtree så  
    if wordTree.exists(spegla(word)): # då kollar det om ordet redan finns i trädet spegladeord
       if not spegladeOrd.exists(word):# och om det inte finns så lägger det in det i spegladeord
            spegladeOrd.put(spegla(word)) # och skriver ut det!
            print(word,spegla(word)) 
