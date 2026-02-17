#Codigo interno
import funtions
from colorama import init, Fore, Back, Style
init(autoreset=True)
while True:
	entrada = input(Fore.CYAN + ">>>")
	if entrada.lower() == "quit":
		break
	elif (entrada == "+"):
		funtions.suma()
	elif (entrada == "-"):
		funtions.resta()
	elif (entrada == "*"):
		funtions.multiplicacion()	
	elif (entrada == "/"):
		funtions.divicion()