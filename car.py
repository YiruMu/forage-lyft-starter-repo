from abc import ABC, abstractmethod
from battery import *
from engine import *
from tire import *


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, Engine, Battery, Tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        else:
            return False
    

def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tireType='Carrigan',sensor=[0,0,0,0]):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    if tireType == 'Carrigan':
        tire = Carrigan(sensor)
    else:
        tire = Octoprime(sensor)
    return Car(engine, battery,tire)


def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tireType='Carrigan', sensor=[0,0,0,0]):
    engine =  WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    if tireType == 'Carrigan':
        tire = Carrigan(sensor)
    else:
        tire = Octoprime(sensor)
    return Car(engine, battery, tire)


def create_palindrome(current_date, last_service_date, warning_light_on, tireType='Carrigan', sensor=[0,0,0,0]):
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(last_service_date, current_date)
    if tireType == 'Carrigan':
        tire = Carrigan(sensor)
    else:
        tire = Octoprime(sensor)
    return Car(engine, battery, tire)


def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tireType='Carrigan',sensor=[0,0,0,0]):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    if tireType == 'Carrigan':
        tire = Carrigan(sensor)
    else:
        tire = Octoprime(sensor)
    return Car(engine, battery, tire)


def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tireType='Carrigan',sensor=[0,0,0,0]):
    engine =  CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(last_service_date, current_date)
    if tireType == 'Carrigan':
        tire = Carrigan(sensor)
    else:
        tire = Octoprime(sensor)
    return Car(engine, battery, tire)