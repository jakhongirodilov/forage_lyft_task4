from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tires_condition = []) -> None:
        self.tires_condition = tires_condition

    def needs_service(self):       
        return sum(self.tires_condition) >= 3