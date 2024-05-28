from dataclasses import dataclass


@dataclass
class Go_retailer:
    Retailer_code : int
    Retailer_name : str
    Type : str
    Country : str

    def __str__(self):
        return f"{self.Retailer_code} - {self.Country}"

    def __hash__(self):
        return hash(self.Retailer_code)

