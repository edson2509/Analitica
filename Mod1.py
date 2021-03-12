class Racional():
#numero base
    nm = 0; dn = 0;

class RS1():
#coef: lista de racionales
#rad: lista de enteros
    coef = []; rad = [];
    latex = "";

    def genltx(self):
        lt = "";
        for i in range(len(coef)):
            lt += coef[i]; lt += "\sqrt{"
            lt += rad[i]; lt += "}+";

        lt = lt[0..len(lt)-1];
        latex = lt;

class RS2():
#tienes dos elementos RS1
    nm = 0; dn = 0;
    latex = "";

    def genltx(self):
        lt = "";

class grafo():
# varios tipos de nodos
    head = 0;
    ady = [][];

#head: estructura primera del grafo
    def __init__(self, head):
        head = head;

#sel: numero del nodo al que se lo esta indexando la artista
#op: operacion asociada a la arista
#ag: nodo para agragar al grafo
    def agrenodo(self, sel, op, ag):
#buscar nodo
    
