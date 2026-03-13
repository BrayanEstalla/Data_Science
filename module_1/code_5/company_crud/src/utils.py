import os
WIDTH = 50

def clear():
    #os.system("clear") #(Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear') #Windows  

def pause():
    input("Press ENTER to continue")

def title(text):
    print("=" * WIDTH)
    print(" " * 10 + text)
    print("=" * WIDTH)