
class Battery():
    def needs_service(self):
        pass


class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date


    def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < self.current_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date


    def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 4) < self.current_date
