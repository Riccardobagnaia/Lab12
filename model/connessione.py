from dataclasses import dataclass

from model.go_retailer import Go_retailer


@dataclass
class Connessione:

    retailer1 : Go_retailer
    retailer2 : Go_retailer
    peso : int

    def __hash__(self):
        return hash(self.retailer1),hash(self.retailer2)