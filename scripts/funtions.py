#FUNTIONS
from colorama import init, Fore, Back, Style
init(autoreset=True)
#Suma FUNTION
def suma():
	primer_num = float(input("Primer número: "))
	segundo_num = float(input("Segundo número: "))
	resultado = primer_num + segundo_num
	print(Fore.GREEN + "El resultado es: ", resultado)
#Resta FUNTION
def resta():
	primer_num = float(input("Primer número: "))
	segundo_num = float(input("Segundo número: "))
	resultado = primer_num - segundo_num
	print(Fore.GREEN + "El resultado es: ", resultado)
#Multiplicar FUNTION
def multiplicacion():
	primer_num = float(input("Primer número: "))
	segundo_num = float(input("Segundo número: "))
	resultado = primer_num * segundo_num
	print(Fore.GREEN + "El resultado es: ", resultado)
#Divicion FUNTION
def divicion():
	primer_num = float(input("Primer número: "))
	segundo_num = float(input("Segundo número: "))
	resultado = primer_num / segundo_num
	print(Fore.GREEN + "El resultado es: ", resultado)