# Träd med grenar

class BinNode(object):   # Nod - pekar till höger och vänster (None)
    def __init__(self,v):
        self.value=v
        self.right=None
        self.left=None

class BinTree(object):   # Binärt Träd
    def __init__(self):
        self.root=None   # Startar tomt

    def exists(self,value):
        return self.__finns(value, self.root)   # Kallar på funktionen under

    def __finns(self, value, r):  # Privat funktion (Nås bara inom filen) 
        while r!=None :           # Säger om value finns i trädet eller inte
            if value < r.value:   # Om value<X går den till vänster och vise versa
                r = r.left
            elif value > r.value:
                r = r.right
            else:
                return True
        return False

    def put(self,value):   # Lägger in value
        self.root = self.__insert(value, self.root)  # Kallar på funktionen under   

# Rekursiv funktion- kallar på sig själv (upprepar sig)
    def __insert(self, value, r):   # Sätter in noden
        if r == None:
            r = BinNode(value)
            return r
        if value < r.value:   # Om value<X utgår den från en ny rot från vänster och vv.
            r.left = self.__insert(value, r.left)  
        elif value > r.value:
            r.right = self.__insert(value, r.right)
        else:
            print("Dubblett: " , value)
        return r

    def write(self):  # Kallar på skriv 
        self.__skriv(self.root)
    
    def __skriv(self, r):   # Skriver ut allting i trädet rekursivt
        if r == None:
            return   # Går till botten av trädet och returnerar ingenting
        self.__skriv(r.left) 
        print(r.value)   # Printar ut alla delar (Ordning: Vänster, Mitten, Höger)
        self.__skriv(r.right)

    def nElements(self):   # Kallar på funktionen under
        return self.__antalElementer(self.root)

    def __antalElementer(self,r):   # Letar och för varje gång den hittar en nod lägger
        if r == None:		    # den till 1
            return 0;
        return 1+self.__antalElementer(r.left)+self.__antalElementer(r.right);
