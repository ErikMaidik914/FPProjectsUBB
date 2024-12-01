

class Taxi:
    def __init__(self,id,x,y,fare):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__fare = fare

    def get_id(self):
        self.__id = id



    def set_id(self, new_id):
        self.__id = new_id



    def get_y(self, y):
        self.__y = y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __repr__(self):
        return(f"{self.__id} - {self.__x} - {self.__y}")


class Ride:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def __repr__(self):
        return(f" {self.__x} - {self.__y}")
