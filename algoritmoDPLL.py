
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
    
    # I' = I ∪ {valor de L es verdadero}
    I_prim = I.copy()
    I_prim[abs(L)] = L > 0
    
    # Llamada recursiva a DPLL con B' e I'
    resultado, I0 = DPLL(B_prima, I_prim)
    if resultado:
        return True, I0
    
    # Eliminar todas las cláusulas que contienen el literal complementario L en B y las ocurrencias del literal L en B
    B_prima = eliminar_literal(-L, B)

    # I' = I ∪ {valor de L es falso }
    I_prim = I.copy()
    I_prim[abs(L)] = L < 0

    # el resultado de I1 <- DPLL(B', I') es verdadero, entonces regresar verdadero e I1
    # Llamada recursiva a DPLL con B' e I'
    resultado, I1 = DPLL(B_prima, I_prim)
    
    #si el resultado es verdader, entonces regresar True e I2
    if resultado:
        return True, I1
        
    # Regresar False y la asignación vacía o nula
    return False, None

def eliminar_literal(L, B):
    #L: literal
    #B: formula booleana en forma de clausalas
    #regresa B con L eliminado
    B_prima = []
    for clausula in B:
        if L not in clausula:
            nueva_clausula = [x for x in clausula if x != -L]
            if nueva_clausula:  # Solo agrega la cláusula si no está vacía
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


def parse_formula(formula_str):
    # Convierte una cadena de texto en una lista de listas de enteros
    formula_str = formula_str.replace("{", "").replace("}", "")
    clausulas = formula_str.split(", ")
    formula = []
    for clausula in clausulas:
        literales = clausula.split(",")
        formula.append([int(literal) for literal in literales])
    return formula

# forma_clausal = [
    #"{{p},{¬p}}",
    #"{{q,p,¬p}}",
    #"{{¬p,¬r,s},{¬q,p,s}}",
    #"{{¬p,q},{q,s},{¬p,s},{¬q,s}}",
   # "{{¬p,q,¬r},{q,¬r,p},{¬p,q,r}}",
  #  "{{r},{q,r},{p,q,¬r},{q}}"
#]

def main():
    forma_clausal = [
        "{{1}, {-1}}",
        "{0}",
        "{{2, 1, -1}}",
        "{{-1, -3, 4}, {-2, 1, 4}}",
        "{{-1, 2}, {2, 4}, {-1, 4}, {-2, 4}}",
        "{{-1, 2, -3}, {2, -3, 1}, {-1, 2, 3}}",
        "{{3}, {2, 3}, {1, 2, -3}, {2}}"
    ]

    for i, formula_str in enumerate(forma_clausal, 1):
        formula = parse_formula(formula_str)
        resultado, asignacion = DPLL(formula, {})
        print(f"Fórmula {i}: {formula_str}")
        if resultado:
            print("Satisfacible con asignación:", asignacion)
        else:
            print("Insatisfacible")
        print()
        
        
main()