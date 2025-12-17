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

class RomanNumberError( Exception ):
    pass

#a. 1994 -> MCMXCIV
def in_to_roman(number):
    number= list(str(number))#Lo transformamos a cadena y lo descomponemos ["1","9"]
    print(number)
    values= ""
    for i in range(0,len(number)):
        if i == 0:
            number[i] = int(number[i]) * 1000
            values += millares.get(number[i])
        elif i == 1:
            number[i] = int(number[i]) * 100
            values +=centenas.get(number[i])
        elif i == 2:
            number[i] = int(number[i]) * 10
            values +=decenas.get(number[i])
        elif i == 3:
            number[i] = int(number[i])
            values +=unidades.get((number[i]))


    
    print(values)
    return values

in_to_roman(1994)