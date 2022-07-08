from abc import ABC, abstractmethod
from battery import Battery, SpindlerBattery, NubbinBattery
from engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine 


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.last_service_date = last_service_date
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return self.engine.needs_service or self.battery.needs_service
    

def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    engine =  WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_palindrome(current_date, last_service_date, warning_light_on):
    engine =  SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    engine =  WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    engine =  CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)