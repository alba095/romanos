"""
1- Crear una funcion que pase de entero >0 y <4000 a romano
2- Cualquier otra entrada da error
3- Limite 3999

Casos de prueba
a. 1994 -> MCMXCIV
b. 4000 -> RomanNumberError() el valor debe ser menor a 4000
c."unacadena" -> RomanNumberError() Debe ser un numero entero

M -> 1000
D -> 500
C -> 100
L -> 50
X -> 10
V -> 5
I -> 1
"""

diccionario= { 1000 : "M", 500 : "D", 100 : "C", 50 : "L", 10 : "X", 5 : "V", 1 : "I"}
unidades= { 1: "I", 2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
decenas={10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70: "LXX",80:"LXXX",90:"XC"}
centenas= {100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM"}
millares={1000: "M", 2000: "MM", 3000: "MMM"}
valores={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
restas={ 'I': ['V', 'X'],'X': ['L', 'C'],'C': ['D', 'M']}

class RomanNumberError( Exception ):
    pass

def romano_valido(roman):
    if roman == "":
        return False

    # Solo letras romanas
    for letra in roman:
        if letra not in valores:
            return False

    # Repeticiones incorrectas
    repeticiones = 1
    for i in range(1, len(roman)):
        if roman[i] == roman[i - 1]:
            repeticiones += 1
            if roman[i] in ['V', 'L', 'D'] or repeticiones > 3:
                return False
        else:
            repeticiones = 1

    # Restas válidas
    for i in range(len(roman) - 1):
        actual = valores[roman[i]]
        siguiente = valores[roman[i + 1]]

        if actual < siguiente:
            if roman[i] not in restas:
                return False
            if roman[i + 1] not in restas[roman[i]]:
                return False

    return True


def num_to_roman(number):
    if not isinstance(number, int):
        raise TypeError("El número debe ser entero")

    if number <= 0 or number > 3999:
        raise ValueError("El número debe estar entre 1 y 3999")

    rev = str(number)[::-1]
    new = []

    mult = 1   # empezamos por la unidad

    for n in rev:
        num = int(n)
        value = num * mult
        if value != 0:
            new.append(value)
        mult = mult * 10   # añadimos un cero

    rome=[]

    for n in new[::-1]:
        if n in unidades:
            rome.append(unidades[n])
        elif n in decenas:
            rome.append(decenas[n])
        elif n in centenas:
            rome.append(centenas[n])
        elif n in millares:
            rome.append(millares[n])
    
    resultado = ""
    for r in rome:
            resultado += r

    return resultado
print(num_to_roman(1994))

def roman_to_num(roman:str)-> int:
    roman = roman.strip().upper()

    if not romano_valido(roman):
        raise ValueError("Número romano inválido")
    
    total = 0

    for i in range(len(roman)):
        valor_actual = valores[roman[i]]

        if i + 1 < len(roman):
            valor_siguiente = valores[roman[i + 1]]

            if valor_actual < valor_siguiente:
                total -= valor_actual
            else:
                total += valor_actual
        else:
            total += valor_actual

    return total
print(roman_to_num("MCMXCIV"))




