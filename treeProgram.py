from bintree import BinTree
swedish=BinTree()  # Skapar ett tomt träd
oldwords=BinTree() # Skapar ett tomt träd
fil=open("word3", encoding="latin-1") 
ord=fil.readlines() # Filen word3 läses in i lisan ord
ordlista=[]
for n in ord:  # Tar bort alla enter
    ordlista.append(n.rstrip("\n"))
for n in ordlista:  # Lägger in alla ord i svenska trädet
    swedish.put(n)
fil.close()
fil=open("english", encoding="latin-1") # Läser in en engelsk fil 
ord=fil.readlines()  # Läser in den i listan ord
ordlista=[]
for n in ord:   # Delar in meningarna i ord och lägger in dem i listan ordlista
    for i in n.split():
        ordlista.append(i)
for n in ordlista:  # För varje ord i ordlistan kollar vi om de finns i svenska trädet
    if swedish.exists(n) and not oldwords.exists(n):	# och kollar om de finns i 
        oldwords.put(n)   # oldwors-trädet så vi inte får dubletter
        print(n)   # Finns ett sådant ord läggs det in i oldwords-trädet och skrivs ut
fil.close()
