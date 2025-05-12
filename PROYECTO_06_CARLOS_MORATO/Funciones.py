import os
import time
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from Clases_06 import CartaAlta,Blackjack,Ruleta,Jugador


ruleta = Ruleta()
cartas = CartaAlta()
blackjck = Blackjack()

def comprobar_saldo():
    if jugador.saldo <= 0:
        os.system("cls")
        jugador.saldo = 0
        print("\n[red]No tienes saldo, para seguir jugando debes ingresar[/red]")
        input("Pulsa ENTER para volver al menú principal")
        return menu_principal()
    else:
        pass
        
                
def registrar_jugador():
    os.system("cls")

    nombre = input("Introduce tu nombre: ").upper()
    
    while True:
        try:
            edad = int(input("\nIntroduce tu edad: "))

            if edad < 18:
                    print("⚠️ [red]Control de acceso denegado (motivo: -18 años)[/red] ⚠️")
                    continue
            else:
                break
            
        except ValueError:
             print("⚠️ [red]Edad inválida. Introduce un número entero[/red] ⚠️")
    while True:
        try:     
            saldo = int(input("\nIntroduce un saldo: "))
            if saldo < 0:
                print("\n[red]El saldo debe ser mayor que 0[/red]")
                continue
            else:
                break
        except ValueError:
            print("⚠️ [red] Valor no permitido[/red] ⚠️ ")

    global jugador
    jugador = Jugador(nombre,edad,saldo)

    print("\n[green]Jugador registrado correctamente[/green]")

def menu_principal():
    while True:
        
        os.system("cls")
        print("""[blue]

 ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗
██║     ███████║███████╗██║██╔██╗ ██║██║   ██║
██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║
╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝

    [/blue]""")
        print("""[red] 
██████╗  ██████╗ ██╗   ██╗ █████╗ ██╗     ███████╗
██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔══██╗██║     ██╔════╝
██████╔╝██║   ██║ ╚████╔╝ ███████║██║     █████╗  
██╔══██╗██║   ██║  ╚██╔╝  ██╔══██║██║     ██╔══╝  
██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
              [/red] 
""")
        print(f"[red]\n¡Bienvenido al Casino {jugador.nombre}![/red]")
        print("\n[bold blue]1. Jugar[/bold blue]")
        print("[yellow]2. Depositar saldo[/yellow]")
        print("[yellow]3. Retirar saldo[/yellow]")
        print("[yellow]4. Ver tu saldo[/yellow]")
        print("[bold blue]5. Instrucciones[/bold blue]")
        print("[red]6. Salir[/red]")

        opcion = input("\n¿Qué quieres hacer?: ")
        
        if opcion == "1":
            menu_juegos()
        elif opcion == "2":
            jugador.depositar_saldo()
        elif opcion == "3": 
            jugador.retirar_saldo()
        elif opcion == "4":
            jugador.mostrar_saldo()
        elif opcion == "5":
            instrucciones()
        elif opcion == "6":
            print("[red]Saliendo...[/red]")
            time.sleep(0.2)
            break
       

def menu_juegos():
    while True:
        os.system("cls")

        print(f"[red]\nBIENVENIDO AL MENÚ DE JUEGOS {jugador.nombre}[/red]")
        print("\n[bold green]\n1. Ruleta[/bold green]")
        print("[bold blue]2. Carta Alta[/bold blue]")
        print("[bold magenta]3. BlackJack[/bold magenta]")
        print("[red]4. Salir[/red]")

        opcion = input("\n¿A qué quieres jugar?: ")
        
        if opcion == "1":
            ruleta.jugar(jugador)
        elif opcion == "2":
            cartas.jugar(jugador) 
        elif opcion == "3": 
            blackjck.jugar(jugador)
        elif opcion == "4":
            return menu_principal()

    
def instrucciones():
    os.system("cls")
    console = Console()

    console.print(Panel.fit("🎮 [bold cyan]INSTRUCCIONES DE JUEGO[/bold cyan]", border_style="cyan"))

    print("\n")
    
    ruleta = Table(title="🎰 Ruleta", title_style="bold green", border_style="green")
    
    ruleta.add_column("Descripción")
    ruleta.add_row("El jugador elige dos números del 0 al 36.")
    ruleta.add_row("La ruleta gira y se detiene mostrando dos números aleatorios.")
    ruleta.add_row("Si aciertas un número, ganas x1.5 tu apuesta.\nSi aciertas ambos, ganas el doble.\nSi fallas, pierdes tu apuesta.")

    
    carta_alta = Table(title="🃏 Carta Alta", title_style="bold blue", border_style="blue")
    
    carta_alta.add_column("Descripción")
    carta_alta.add_row("El jugador apuesta una cantidad.")
    carta_alta.add_row("Se reparten dos cartas y se comparan.")
    carta_alta.add_row("Si tu carta es mayor que la del crupier, ganas el doble.\nSi no, pierdes la apuesta.")

    
    blackjack = Table(title="♠️  Blackjack", title_style="bold magenta", border_style="magenta")
    
    blackjack.add_column("Descripción")
    blackjack.add_row("El jugador elige cuánto quiere apostar.")
    blackjack.add_row("Recibe 2 cartas y puede 'pedir' más o 'plantarse'.")
    blackjack.add_row("El crupier saca cartas hasta llegar a 17 o más.")
    blackjack.add_row("Ganas si tienes más puntos sin pasarte de 21.\nSi empatan, se devuelve la apuesta.\nSi te pasas o el crupier gana, pierdes la apuesta.")

    
    console.print(ruleta)
    console.print(carta_alta)
    console.print(blackjack)
    console.print("\n[bold yellow]¡Buena suerte![/bold yellow] 🍀\n")

    input("\nPulsa ENTER para volver...")
    return menu_principal()