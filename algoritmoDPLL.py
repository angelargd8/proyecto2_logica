
#entrada: una formula boleana A en formas de clausalas e asignacion vacia
#salida: reporta si A es unsatisfacible con asignacion prcial vacia o si A es satisfacible.
#verdadero si A es satisfacible, falso si A no es satisfacible

def DPLL(B, I): 
    # Propagación de unidades
    while True:
        unit_clauses = [c for c in B if len(c) == 1]
        if not unit_clauses:
            break
        for clause in unit_clauses:
            literal = clause[0]
            B = eliminar_literal(literal, B)
            I[abs(literal)] = literal > 0
            
    # Si B es vacía, entonces regresar true e I
    if len(B) == 0:
        return True, I
    
    # Si hay alguna disyunción vacía en B, regresar false e I
    if [] in B:
        return False, None
    
    # Seleccionar literal no asignado
    L = seleccionar_literal(B)
    
    # Eliminar todas las cláusulas que contienen el literal L en B y las ocurrencias de -L en B
    B_prima = eliminar_literal(L, B)
    
    # Asignar L como verdadero
    I_prim = I.copy()
    I_prim[abs(L)] = L > 0
    
    # Llamada recursiva
    resultado, I0 = DPLL(B_prima, I_prim)
    if resultado:
        return True, I0
    
    # Intentar asignar L como falso
    B_prima = eliminar_literal(-L, B)
    I_prim = I.copy()
    I_prim[abs(L)] = L < 0
    
    # Llamada recursiva
    resultado, I1 = DPLL(B_prima, I_prim)
    if resultado:
        return True, I1
    
    return False, None

def eliminar_literal(L, B):
    B_prima = []
    for clausula in B:
        if L not in clausula:
            nueva_clausula = [x for x in clausula if x != -L]
            B_prima.append(nueva_clausula)
    return B_prima

def seleccionar_literal(B):
    # Selecciona el primer literal no asignado
    for clausula in B:
        for literal in clausula:
            return literal
    return None

def formato_conjunto(formula):
    # Convierte una lista de listas en un conjunto de conjuntos
    return [{literal for literal in clausula} for clausula in formula]

def main():
    # Fórmulas en forma clausal
    forma_clausal = [
        [[1, 2, 3], [-1, -2], [1, -3]],         # (p OR q OR r) AND (NOT p OR NOT q) AND (p OR NOT r)
        [[1, -2], [2, -3], [-1, 3], [-3]],      # (p OR NOT q) AND (q OR NOT r) AND (NOT p OR r) AND (NOT r)
        [[-1, 2], [1, -3], [3]],                # (NOT p OR q) AND (p OR NOT r) AND (r)
        [[-1, -2, -3], [-1, 2, 3], [1, -2]],    # (NOT p OR NOT q OR NOT r) AND (NOT p OR q OR r) AND (p OR NOT q)
        [[1, 2], [-1, 3], [-2, 3], [-3]],       # (p OR q) AND (NOT p OR r) AND (NOT q OR r) AND (NOT r)
        [[-1, 2], [-2, 3], [-3, 4], [-4]],      # (NOT p OR q) AND (NOT q OR r) AND (NOT r OR s) AND (NOT s)
        [[1], [-1], [2], [-2]],                 # (p) AND (NOT p) AND (q) AND (NOT q)
        [[1, -2, 3], [-1, 2], [2, -3]]          # (p OR NOT q OR r) AND (NOT p OR q) AND (q OR NOT r)
    ]
    
    # Evaluar cada fórmula
    for i, formula in enumerate(forma_clausal, 1):
        resultado, asignacion = DPLL(formula, {})
        print(f"Fórmula {i}: {formato_conjunto(formula)}")
        if resultado:
            print("Satisfacible con asignación:", asignacion)
        else:
            print("Insatisfacible con asignación vacía")
        print()


main()
