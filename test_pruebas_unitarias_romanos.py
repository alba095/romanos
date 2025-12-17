"""from main import *""" #Importa todo lo de main
from main import in_to_roman #Solo importa la funcion de intoroman

def test_in_to_roman_1994():
    assert in_to_roman(1994)== "MCMXCIV"


def test_prueba2():
    assert 10<20

def test_prueba3():
    assert 10 != 20