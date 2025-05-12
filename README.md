# Proyecto_Casino_royale
Descripción del Proyecto

Version 1.0.0

Casino Royale es un simulador de juegos de azar que permite al usuario participar en tres juegos clásicos: Ruleta, Carta Alta y Blackjack, todo desde la consola. El programa está desarrollado en Python de forma modular y utiliza el paquete rich para mejorar la experiencia visual en terminal con colores, tablas e instrucciones estilizadas.

Cada jugador puede gestionar su propio saldo virtual, realizar apuestas y disfrutar de una experiencia interactiva con animaciones y reglas personalizadas para cada juego.

▶️ Instrucciones de Uso

  Requisitos previos:

  Python 3 instalado.

  Instalar la librería rich:

  pip install rich

Ejecución del programa:

1. Abre una terminal en la carpeta del proyecto.

2.  Ejecuta el archivo principal:

3.  python Main.py

4.  Flujo del programa:

Al iniciar, el usuario debe registrarse con nombre, edad y saldo inicial.

Se accede al menú principal donde podrá:

 1. Jugar (acceder a uno de los tres juegos disponibles)

 2. Ver su saldo

 3. Ingresar o retirar saldo

 4. Leer las instrucciones completas.

 5. Salir del casino

- Cada juego tiene su propia lógica de apuesta, resultado y recompensa

- El saldo se actualiza automáticamente tras cada partida

Juegos incluidos:

🎰 Ruleta: elige dos números y apuesta. Gana si aciertas uno o ambos

🃏 Carta Alta: compites contra el crupier. La carta más alta gana

♠️ Blackjack: intenta acercarte a 21 sin pasarte y vence al crupier

💡 Consejos

Todos los textos importantes están destacados con colores usando rich para facilitar la lectura
El saldo no puede ser negativo. Si llegas a 0, deberás ingresar más fichas para seguir jugando
Es un entorno simulado, por lo que todas las fichas son virtuales y sin valor real
