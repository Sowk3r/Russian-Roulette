from random import*

#variables des coups joué
def setting():
  global z, y, x, w, v, b, c, a
  z=0
  y=0
  x=0
  w=0
  v=0

  #variables de la victoire qui bloque le jeu
  c=0

  #b variable du coups du joueur
  b=0

  #a variable aléatoire de la balle
  a=randint(1,6)
  #print(a)

def décor():
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print("                                     ")
  print("                                    ")
  print("                             ")
  print("  ______                              ")
  print("   |  |                               ")
  print("   |  |                             ")
  print("___|  |_______                 ___________________")
  print("   |__|       \               /                    ")
  print("               \             /___                  ")
  print("__________      \           /|\ __\   _____________")
  print("          \      \         / | |  /  /  ")
  print("           \      \       /  \ | /  /   ")
  print("            \      \     /    \|/  /     ")
  print("             \     /|   |\        /      ")
  print("_______       \   / |   | \      /              _____")
  print("       \_______\ /  |   |  \    /              /   ")
  print("        \  ____ |   |   |   \  /      ___     /    ")
  print("         \|_|_| |   /   \    \/      |\ __\  /     ")
  print("\         \_|_| |  /     \    |\     | |  / /       ")
  print(" \         \    | /       \   ||\    \ | / /       ")
  print("  \        /|___|/         \  || \    \|/ /        ")
  print("   \      / |               \ ||  \      /         ")
  print("    \    /  |                \||   \    /           ")
  print("     \  /   |                 \|    \  /            ")
  print("______\/ /| |                  \     \/_____________")
  print("      || || /                   \    ||")
  print("      || ||/                     \   ||")
  print("      || |/                       \  ||")
  print("      || /                         \ ||")
  print("______||/                           \||____________")
  print(" ")
  print("                              _______")
  print("                             |       |")
  print("      ______              ___|_______|___")
  print("    /[=]____)     ---- D    (   O O   )")
  print("   /_P                       (   I   )")
  print(" ")
  print(" ")
  print("    ____________________________________")
  print("   |                                    |")
  print("   |  Welcome in the russian roulette ! |")
  print("   |____________________________________| ")
  print(" ")

#si le coup joué ne tue pas
def clic():
  print("_________________________________________________")
  print("")
  print("")
  print("")
  print("                   . . .")
  print("")
  print("")
  print("              Nothing happend ")
  print("_______________________________________________ ")

#message GG
def GG():
  print("________________________________________________")
  print(" ")
  print("               _____      _____ ")
  print("              /|    \    /|    \ ")
  print("              ||         ||      ")
  print("              ||         ||      ")
  print("              ||   __    ||   __ ")
  print("              ||    |    ||    |")
  print("              \|____/    \|____/")
  print(" ")
  print("_______________________________________________ ")
#fonction pour afficher les coups joué
def affiche():
  global z, y, x, w, v
  print("   The number used are ",z,y,x,w,v,"")
  print("")

#le jeu
def game():
  global z, y, x, w, v, a, b, c
  while a!=b:
    print("        Pick a number between 1 and 6.")
    print("")
    b=int(input())
    if(c==12 or b==99):
      GG()
      print("")
      print("   You finish the game, thanks you for playing")
      c=12
    elif(b==z or b==y or b==x or b==w or b==v):
      print("")
      print("   This number is already used,")
      print("   try an other one !")
      print("")
    elif(a!=b and b<=6):
      if(c!=4):
        clic()
        print("")
        print("   Pass the revolver, you are all right.")
      else:
        v=b
        affiche()
        GG()
        print(" ")
        print("   You are not Dead, incredible !")
        print(" ")
        c=12
        break
      if(c==3):
        w=b
        affiche()
        c=c+1
      elif(c==2):
        x=b
        affiche()
        c=c+1
      elif(c==1):
        y=b
        affiche()
        c=c+1
      elif(c==0):
        z=b
        affiche()
        c=c+1
    elif(b>6):
      print("__________________________________________________")
      print("01010110111000101010101010010001101001001010101000")
      print("1010001110101101011011101000010  Error  0100001001")
      print(" 01010101101000010101010100101010110101010101010101")
      print(" 1010101010101101  Error  010101011101010100010101100")
      print("010101010110011110101010101010001011101010101010010")
      print("11000110101101110100011101101010001010100110100110")
      print("01011  Error  1101011010110001011101010010100101010")
      print("1010101010001010110100010101010  Error  1010110101")
      print("01010110111000101010101010010001101001001010101000")
      print("10100011101011010110111010000101010010100100001001")
      print("__________________________________________________")
      print("")
    else:
      print("_____________________________________________")
      print("                ____________ ")
      print("               /            \ ")
      print("              |              | ")
      print("              |   X      X   | ")
      print("              |              | ")
      print("               \__        __/ ")
      print("                  |      | ")
      print("                  | ++++ | ")
      print("                  \______/ ")
      print("_____________________________________________")
      print("")
      print("               You are Dead ! ")
  print("")
  print("   Thanks for playing !")
  print("")
  answer =input("   Wanna play again ?: ")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  if answer == "yes" or "Yes" or "1" or "y" or "Y":
    setting()
    print("    ____________________________________")
    print("   |                                    |")
    print("   |  Welcome in the russian roulette ! |")
    print("   |____________________________________| ")
    print(" ")
    game()

def main():
  setting()
  décor()
  game()

main()
