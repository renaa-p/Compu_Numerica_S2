#----- EJERCICIO EN CLASE COMPU NUMERICA LAB ----
# integrante : Renato Ortiz Inostroza

def notacion(x, base):
    exp1 = len(x) - 1
    a = (float(x) / base** exp1)
    return a

def notacion2(y, base):
    exp2 = len(y) - 1
    k = (float(y)/ base** exp2)
    return k

def cifras_sig(x):
    c = len(x) - 1
    return c

def suma(a, k):
    result_suma = a + k
    return result_suma

def resta(a, k):
    result_resta = a - k
    return result_resta

def multiplicar(a, k):
    result_multiply = a * k
    return result_multiply

def dividir(a, k):
    result_dividir = a / k
    return result_dividir

if __name__ == "__main__":
    x = input('Ingresar el primer numero:').replace("\n","")
    y = input('Ingresar el segundo numero:')
    base = 10
    a = notacion(x, base)
    k = notacion(y, base)
    c = cifras_sig(x)
    sum = suma(a,k)
    rest = resta(a,k)
    mult = multiplicar(a,k)
    div = dividir(a,k)
    resultado = {"A": a, "B": base,"C": c}
    resultado2 = {"SUMA": sum, "RESTA": rest, "MULTIPLICACION": mult, "DIVIDIR": div}
    print(resultado, resultado2)
    
