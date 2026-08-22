#----- EJERCICIO EN CLASE COMPU NUMERICA LAB ----
# integrante : Renato Ortiz Inostroza

def obtener_notacion(num_str):
    c = len(num_str) - 1
    if c > 0:
        a = float(num_str[0] + "." + num_str[1:])
    else:
        a = float(num_str)
        
    return a, c

def operaciones_exactas(x_str, y_str):
    n1 = int(x_str)
    n2 = int(y_str)
    
    suma = n1 + n2
    resta = n1 - n2
    mult = n1 * n2
    div = n1 / n2 if n2 != 0 else 0 
    
    return suma, resta, mult, div

if __name__ == "__main__":
    x = input('Ingresar el primer numero (sin decimales): ').strip()
    y = input('Ingresar el segundo numero (sin decimales): ').strip()
    base = 10
    
    # Sacamos A y C para cada numero
    a1, c1 = obtener_notacion(x)
    a2, c2 = obtener_notacion(y)

    sum_res, rest_res, mult_res, div_res = operaciones_exactas(x, y)
    resultado_x = {"A": a1, "B": base, "C": c1}
    resultado_y = {"A": a2, "B": base, "C": c2}
    
    resultado_operaciones = {
        "SUMA": sum_res, 
        "RESTA": rest_res, 
        "MULTIPLICACION": mult_res, 
        "DIVIDIR": div_res
    }
    
    print("\nValores en notación:")
    print(f"Num 1: {resultado_x}")
    print(f"Num 2: {resultado_y}")
    
    print("\nResultados operando los números completos:")
    for op, val in resultado_operaciones.items():
        print(f"{op}: {val}")