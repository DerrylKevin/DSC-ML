thriller = ["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy = ["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]

def genre(string):
    
    for x in thriller:
        if (string.lower() == x.lower()):
            print("It is a thriller")
            return
    
    for x in comedy:
        if (string.lower() == x.lower()):
            print("It is a comedy")
            return
    
    print("It's neither comedy nor thriller")
    return

string = input("Enter the movie/series name: ")
genre(string)
