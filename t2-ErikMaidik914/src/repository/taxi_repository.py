

class TaxiRepo:

    def __init__(self):
        self.__all_taxis = {}


    def save_taxi(self,taxi):
        self.__all_taxis[taxi.get_id()] = taxi

    def show_all_taxies(self):
        return (list(self.__all_taxis.values()))

