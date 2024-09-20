from games import Games 
class machines

def_init_(self,material:str):
    """this class represent the behavior on ar arcade videogames"""
    self.material = material 
    self.__games = """aca deben ir corchetes"""
def add_games(self, games:Games):
    """
    this method adds a videogame to recurrent machine.

    In this method a videogam is recived as argument, following a Videogame
    abstract data type, and it is add internal game list

    Args: 
    games (Games): games to be added
    """

    self.__Games.append()
    
def add_videogames(self, code:int):
self.__videogames.append(videogames):




 def remove_videogames(self, code:int):
    index = -1
    for i, vg in enumerate(self.__videogames):
        if vg.get_code() == code:
            index = 1
            break

        if index != -1:
            self.__videogames.pop(index)
        else:
            print(f"Video Game whit code {code}it not in the machine")



def show_videogames(self):
    if len(self.__videogames) > 0:
        print ("code/tname")
        for vg in self.__videogames:
            print(vg)
    else:
        print("no video games have been added.")     
           

