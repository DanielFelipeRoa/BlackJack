from random import shuffle

# Define las cartas
def baraja():
  return [(n,p) for n in (['A','J','Q','K'] + [str(x) for x in range(2,11)]) for p in ['♥','♦','♣','♠']]

# Mezcla una lista
def mezclar(baraja):
  shuffle(baraja)
  return baraja

# Retorna el valor de una carta
def valor_carta(carta):
  if carta[0] in ['J','Q','K']:
    return 10
  elif carta[0] == 'A':
    return 1
  else:
    return int(carta[0])

# Retorna el valor de todas lcas cartas de una mano
def valor_mano(mano):
  if mano == []:
    return 0
  return valor_carta(mano[0]) + valor_mano(mano[1:])

# Cambia el valor de la carta A entre 1 o 10
def valor_juego(mano):
  if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
    return valor_mano(mano) + 10
  else:
    return valor_mano(mano)

# Main
def empezar_juego(mazo, jugador, dealer):
  jugar(mazo[4:], jugador+[mazo[0]]+[mazo[1]], dealer+[mazo[2]]+[mazo[3]])
  
# Repartir cartas al jugador
def jugar(mazo, jugador, dealer):
  print('Tu mazo es: ', [jugador[1:]])
  if len(mazo) > 2 and valor_juego(jugador) < 21 and input("Pulsa 'p' para solicitar una carta, o cualquier letra para plantarte: ")=="p":
    jugar(mazo[1:], jugador+[mazo[0]], dealer)
  else:
    print("Cartas jugador: \n" + str(jugador))
    repartir_casa(mazo, dealer, jugador)
    
# Repartir cartas a la casa
def repartir_casa(mazo, dealer, jugador):
    if valor_juego(jugador) > 21 or valor_juego(jugador) <= valor_juego(dealer):
      print("Cartas dealer: \n" + str(dealer))
      ganador(valor_juego(jugador),valor_juego(dealer))
    elif valor_juego(dealer) < 21:
      repartir_casa(mazo[1:], dealer+[mazo[0]], jugador)
    
# Define ganador
def ganador(jugador, dealer):
  if jugador > 21:
    print("Gana dealer")
    return False
  elif dealer > 21:
    print("Gana jugador")
    return False
  elif jugador > dealer:
    print("Gana jugador")
    return False
  else:
    print("Gana dealer")
    return False
  return True

empezar_juego(mezclar(baraja()),[],[])