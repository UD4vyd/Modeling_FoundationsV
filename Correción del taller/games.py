class Games:
    """
this class represent the behavior of a general videogame
    """

    def __init__(self, code: int, name:str, description:str):
        self.__code = code
        self.__name = name 
        self.__description = description
    
    def get_code(self):
        """
        this method return the code of the videogame.

        retunrn:
        An intenger whit the code of yhe videogame.
        """
        return self.__code
    
    def set_description(self, Description: str):
        self.__description = Description
    
    def __str__(self):
        return f"{´=´*10}\nCode: {self.__code}\n\
             Name: {self.__name}\nDescription: {self.__description}"
    