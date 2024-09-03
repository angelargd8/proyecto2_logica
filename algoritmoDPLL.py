
#entrada: una formula boleana A en formas de clausalas e asignacion vacia
#salida: reporta si A es unsatisfacible con asignacion prcial vacia o si A es satisfacible.
#verdadero si A es satisfacible, falso si A no es satisfacible
def DPLL(B, I): 
    #B: formula booleana en forma de clausalas
    #I: asignacion parcial
    #A es formula y la asignacion parcial vacia
    
    #Si B es vacia, entonces regresar true e I
    if len(B) == 0:
        return True, I
    #si hay laguna disyuncion vacia en B, entonces regresar false e I
    if [] in B:
        I = None
        return False, I
    
    #L <- conjunto de literales en B 
    #L <- seleccionar_literal(B) #pone en forma positiva
    #el algoritmo DPLL es no deterministico: se debe seleccionr una literal 
    #no asignada en la asignacion parcial y luego seleccionar el valor de verdad
    L = seleccionar_literal(B)

    #elimine todas las clausulas que contiene la literal L en B y 
    # elimine las ocurrencias en las clausulas de la literl complementaria de L en B, 
    # construyendo B'
    #B' <- B con L eliminado
    B_prima = eliminar_literal(L, B)

    #--esto en adelante ya les toca pues
    #I' <- I U {L = true}






def eliminar_literal(L, B):
    #L: literal
    #B: formula booleana en forma de clausalas
    #regresa B con L eliminado
    B_prima = []
    for clausula in B:
        if L not in clausula:
            nueva_clausula = [x for x in clausula if x != -L]
            B_prima.append(nueva_clausula)
    return B_prima
    
def seleccionar_literal(B):
    #B: formula booleana en forma de clausalas
    #regresa un literal en B
    #L <- conjunto de literales en B 
    for clausula in B:
        for literal in clausula:
            return literal
    return None
