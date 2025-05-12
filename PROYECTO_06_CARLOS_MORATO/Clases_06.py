import random
import time
import os
from rich import print
from rich.console import Console
from rich.table import Table


console = Console()

def llamar_menu():
    from Funciones import menu_principal
    menu_principal()
    
def llamar_comprobar_saldo():
    from Funciones import comprobar_saldo
    comprobar_saldo()

class Jugador:
    def __init__(self,nombre,edad, saldo):

        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo

    def __str__(self):

        return(f"Nombre: {self.nombre} - Edad: {self.edad} - Saldo: {self.saldo}")
    
    def depositar_saldo(self):
        os.system("cls")

        print("[yellow]INGRESAR SALDO[/yellow]")
        print("-"*20)

        try:
            saldo_añadir = int(input("\nEscribe cuánto saldo deseas ingresar: "))
            self.saldo = self.saldo + saldo_añadir

        except ValueError:
            print("[red]Dato introducido no válido, vuelve a intentarlo[red]")
            input("\nPulsa ENTER para continuar...")

        print("[green]\nSaldo ingresado correctamente[/green]")
        input("\nPulsa ENTER para volver al menú...")
        return llamar_menu()

    def retirar_saldo(self):
        llamar_comprobar_saldo()
        os.system("cls")

        print("[yellow]RETIRAR SALDO[/yellow]")
        print("-"*20)

        try:
            saldo_retirar = int(input("\nEscribe cuánto saldo deseas retirar: "))
            self.saldo = self.saldo - saldo_retirar
        except:
            print("[red]Dato introducido no válido, vuelve a intentarlo[red]")
            input("\nPulsa ENTER para continuar...")

        print("[green]\nSaldo retirado correctamente[/green]")
        
        input("\nPulsa ENTER para volver al menú...")
        return llamar_menu()

    def mostrar_saldo(self):
        os.system("cls")

        print("[yellow]MOSTRAR SALDO[/yellow]")
        print("-"*20)
        tabla = Table(title="SALDO")
        tabla.add_column("Nombre", style="yellow", justify="center")
        tabla.add_column("Resultado", style="green", justify="center")

        if self.saldo <= 0:
            self.saldo = 0
            
        tabla.add_row(f"{self.nombre}", f"{self.saldo}")
        
        console.print(tabla)

        input("\nPulsa ENTER para volver al menú...")
        return llamar_menu()



class Ruleta:
    
    def girar_ruleta(self):
        numeros = list(range(37))  
        print("[bold green]\nGirando la ruleta...[/bold green]")
        print("\n")
        for i in range(30):  
            numero_mostrado = random.choice(numeros)
            print(f"\r🎡 Número {i}: {numero_mostrado}", end='', flush=True)
            time.sleep(0.1) 

        resultado1 = random.choice(numeros)
        resultado2 = random.choice(numeros)

        print(f"[bold green]\n\n🎯 ¡La ruleta se detuvo en los números: {resultado1} y {resultado2}![/bold green]")
        return resultado1, resultado2

    def jugar(self, jugador):
        llamar_comprobar_saldo()
        os.system("cls")
        print("🎰[bold green] Bienvenido a la Ruleta[/bold green] 🎰")
        print("-"*30)
        print(f"[bold green]Tienes {jugador.saldo} fichas\n[/bold green]")

        
        while True:
            try:
                apuesta = int(input("¿Cuánto quieres apostar?: "))
                if 0 < apuesta <= jugador.saldo:
                    break
                else:
                    print("[bold green]La apuesta debe ser mayor que 0 y menor o igual a tu saldo[/bold green]")
            except ValueError:
                print("[bold green]Por favor, ingresa solo números[/bold green]")

        
        while True:
            try:
                eleccion1 = int(input("\nElige el primer número (0-36): "))
                eleccion2 = int(input("\nElige el segundo número (0-36): "))
                if 0 <= eleccion1 <= 36 and 0 <= eleccion2 <= 36 and eleccion1 != eleccion2:
                    break
                else:
                    print("[bold green]Ambos números deben ser distintos y entre 0 y 36 [/bold green]")
            except ValueError:
                print("[bold green]Por favor, ingresa números válidos [/bold green]")

        resultado1, resultado2 = self.girar_ruleta()

        if eleccion1 in (resultado1, resultado2) and eleccion2 in (resultado1, resultado2):
            print("\n🎉[bold green] ¡Felicidades, acertaste los dos números![/bold green]")
            jugador.saldo += apuesta * 2
            print(f"[bold green]Nuevo saldo: [/bold green][green]{jugador.saldo}[/green]")
            input("\nPulsa ENTER para volver: ")
            return jugador.saldo
            
        elif eleccion1 in (resultado1, resultado2) or eleccion2 in (resultado1, resultado2):
            print("\n🎉[bold green] ¡Felicidades, acertaste uno![/bold green]")
            jugador.saldo = jugador.saldo + (apuesta*1.5)

            print(f"[bold green]Nuevo saldo: [/bold green][green]{jugador.saldo}[/green]")
            input("\nPulsa ENTER para volver: ")
            return jugador.saldo
        else:
            print("💔[bold green] Lo siento, no acertaste[/bold green]")
            jugador.saldo -= apuesta
            print(f"[bold green]Nuevo saldo: [/bold green][green]{jugador.saldo}[/green]")
            input("\nPulsa ENTER para volver: ")
            return jugador.saldo  
            
class CartaAlta:
    def __init__(self):
        self.lista_valores0 = ["2","3","4","5","6","8","9","10","11","12","13","14"]
        self.lista_valores1 = ["2","3","4","5","6","8","9","10","11","12","13","14"]
        self.lista_simbolos = ["🂲","🂳","🂴","🂵","🂶","🂷","🂸","🂹","🂺","🂻","🂼","🂼","🂾"]
        
    def generar_cartas(self):
        print("\n")
        
        for i in range(12):  
            numero_mostrado0 = random.choice(self.lista_simbolos)
            numero_mostrado00 = random.choice(self.lista_valores0)
            print(f"\r🎡 Número {i} : {numero_mostrado0}", end='', flush=True)
            time.sleep(0.1)

        resultado00 = numero_mostrado00
        print("\n")
        print(f"\n[green]Tu carta es {resultado00}[/green]")
        print("\n")

        for i in range(12):  
            numero_mostrado1 = random.choice(self.lista_simbolos)
            print(f"\r🎡 Número {i} : {numero_mostrado1}", end='', flush=True)
            time.sleep(0.1)

        resultado01 = random.choice(self.lista_valores1)
        print("\n")
        print(f"\nEl Crupier sacó la carta {resultado01}")
        print("\n")
        return resultado00, resultado01

    def jugar(self,jugador):
        llamar_comprobar_saldo()
        os.system("cls")
        print("♦️♠️[bold blue] Bienvenido a Carta Alta [/bold blue]♣️♥️")
        print("-"*20)
        print(f"[bold blue]Tienes {jugador.saldo} fichas\n[/bold blue]")
        while True:
            try:
                apuesta = int(input("¿Cuánto quieres apostar?: "))
                
                if apuesta > jugador.saldo:
                    print("[bold blue]Su apuesta debe ser [/bold blue][green]menor o igual a su saldo[/green]")
                else:
                    break

            except ValueError:
                print("[red]Valor inválido[/red],  y sólo debe constar de [green]valores númericos[/green]")
                
        
        resultado1, resultado2 = self.generar_cartas()
        
        if resultado1 > resultado2:
            print("🎉[bold blue] ¡Felicidades, ganaste![/bold blue]")
            jugador.saldo = jugador.saldo + (apuesta*2)
            print(f"\n[bold blue]Nuevo saldo: [/bold blue][green]{jugador.saldo}[/green]")
            input("\nPulsa ENTER para volver: ")
            return jugador.saldo
        
        else:
            jugador.saldo = jugador.saldo - apuesta
            print("💔[bold blue] Lo siento, perdiste[/bold blue]")
            print(f"[bold blue]\nNuevo saldo: [/bold blue][green]{jugador.saldo}[/green]")
            input("\nPulsa ENTER para volver: ")
            return jugador.saldo
    


class Blackjack:
    
    def __init__(self):
        self.mazo = [1,2,3,4,5,6,7,8,9,10]*4 

    def repartir_carta(self):
        return random.choice(self.mazo)

    def calcular_puntaje(self, mano):
        return sum(mano)

    def jugar(self, jugador):
        llamar_comprobar_saldo()
        os.system("cls")
        print("🃏[bold magenta] Bienvenido al Blackjack[/bold magenta] 🃏")
        print("-"*30)
        print(f"[bold magenta]Saldo actual: {jugador.saldo} fichas[/bold magenta]\n")

        while True:
            try:
                apuesta = int(input("¿Cuánto deseas apostar?: "))
                if 0 < apuesta <= jugador.saldo:
                    break
                else:
                    print("[bold magenta]Apuesta no válida[/bold magenta]")
            except ValueError:
                print("[bold magenta]Ingresa un número válido[/bold magenta]")

        
        mano_jugador = [self.repartir_carta(), self.repartir_carta()]
        mano_crupier = [self.repartir_carta(), self.repartir_carta()]

        print(f"[bold magenta]\nTu mano: {mano_jugador} (Total: {self.calcular_puntaje(mano_jugador)})[/bold magenta]")
        print(f"[bold magenta]Carta visible del crupier: {mano_crupier[0]}[/bold magenta]")

       
        while True:
            opcion = input("¿Quieres pedir carta? (s/n): ").lower()
            if opcion == 's':
                carta = self.repartir_carta()
                mano_jugador.append(carta)
                total = self.calcular_puntaje(mano_jugador)
                print(f"[bold magenta]\nRecibiste: {carta} - Tu mano: {mano_jugador} (Total: {total})[/bold magenta]")
                if total > 21:
                    print("💥 [red]Te pasaste de 21. Pierdes[/red]")
                    jugador.saldo -= apuesta
                    break
            elif opcion == 'n':
                break
            else:
                print("[bold magenta]Opción no válida[bold magenta]")

        
        if self.calcular_puntaje(mano_jugador) <= 21:
            print(f"[bold magenta]\nTurno del crupier...[/bold magenta]")

            while self.calcular_puntaje(mano_crupier) < 17:
                time.sleep(1)
                carta = self.repartir_carta()
                mano_crupier.append(carta)
                print(f"[bold magenta]El crupier recibe: {carta} > Mano: {mano_crupier}[/bold magenta]")

            puntaje_jugador = self.calcular_puntaje(mano_jugador)
            puntaje_crupier = self.calcular_puntaje(mano_crupier)

            print(f"[bold magenta]\nTu total: {puntaje_jugador}[/bold magenta]")
            print(f"[bold magenta]Total del crupier: {puntaje_crupier}[/bold magenta]")

            if puntaje_crupier > 21 or puntaje_jugador > puntaje_crupier:
                print("🎉 [green]¡Ganaste![/green]")
                jugador.saldo += apuesta*2
            elif puntaje_jugador < puntaje_crupier:
                print("💔 [red]Perdiste [/red]")
                jugador.saldo -= apuesta
            else:
                print("🤝 [bold magenta]Empate. Se devuelve la apuesta [/bold magenta]")

        print(f"[bold magenta]\nSaldo actualizado:[/bold magenta][green] {jugador.saldo} fichas[/green]")
        input("Presiona ENTER para continuar...")

        return jugador.saldo


        