class Tire():
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        pass


class Carrigan(Tire):
    def needs_service(self):
        for num in self.sensor:
            if num >= 0.9:
                return True
        return False


class Octoprime(Tire):
    def needs_service(self):
        for num in self.sensor:
            if num >= 3:
                return True
        return False