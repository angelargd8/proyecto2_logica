#Algoritmo utilizando fuerza bruta

from itertools import product  

def es_satisfacible(fórmula):
    # Extraemos todas las variables únicas de la fórmula. Utilizamos el valor absoluto de los literales 
    # para asegurarnos de que tomamos en cuenta tanto las variables como sus negaciones.
    variables = sorted(set(abs(lit) for cláusula in fórmula for lit in cláusula))
    
    # Generamos todas las combinaciones posibles de valores de verdad para las variables.
    for valores in product([True, False], repeat=len(variables)):
        # Creamos una asignación de valores de verdad para cada variable.
        asignación = {var: val for var, val in zip(variables, valores)}
        
        # Evaluamos si esta asignación satisface la fórmula.
        if evaluar_fórmula(fórmula, asignación):
            return True, asignación  # Si es satisfacible, retornamos True junto con la asignación que lo logró.
    
    # Si ninguna asignación satisface la fórmula, retornamos False con una asignación vacía.
    return False, {}

def evaluar_fórmula(fórmula, asignación):
    # Evaluamos cada cláusula de la fórmula con la asignación dada.
    for cláusula in fórmula:
        # Verificamos si al menos un literal en la cláusula se evalúa como True con la asignación.
        # Si todos los literales en una cláusula se evalúan como False, la fórmula no es satisfacible con esta asignación.
        if not any(asignación.get(abs(lit), False) if lit > 0 else not asignación.get(abs(lit), True) for lit in cláusula):
            return False  # Si encontramos una cláusula que no es verdadera, la fórmula no es satisfacible.
    
    # Si todas las cláusulas son verdaderas con la asignación dada, la fórmula es satisfacible.
    return True

def mostrar_resultado(formula_num, formula, resultado, asignacion):
    print(f"Fórmula {formula_num}: {formula}")
    if resultado:
        print(f"Satisfacible con asignación: {asignacion}")
    else:
        print("Insatisfacible con asignación vacía.")

formulas = [
    [{1, 2, 3}, {-1, -2}, {1, -3}],        
    [{1, -2}, {2, -3}, {-1, 3}, {-3}],      
    [{-1, 2}, {1, -3}, {3}],                
    [{-1, -2, -3}, {-1, 2, 3}, {1, -2}],    
    [{1, 2}, {-1, 3}, {-2, 3}, {-3}],       
    [{-1, 2}, {-2, 3}, {-3, 4}, {-4}],      
    [{1}, {-1}, {2}, {-2}],                 
    [{1, -2, 3}, {-1, 2}, {2, -3}],         
]

# Iterar sobre cada fórmula, evaluar y mostrar el resultado
for i, formula in enumerate(formulas, start=1):
    resultado, asignacion = es_satisfacible(formula)
    mostrar_resultado(i, formula, resultado, asignacion)
    print()  