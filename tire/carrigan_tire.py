from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tires_condition = []) -> None:
        self.tires_condition = tires_condition

    def needs_service(self):
        for tire in self.tires_condition:
            if tire >= 0.9:
                return True
        
        return False