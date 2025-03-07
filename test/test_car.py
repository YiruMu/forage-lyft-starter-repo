import unittest
from datetime import datetime
from car import * 


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4) # testing for improved battery
        current_mileage = 0
        last_service_mileage = 0

        car = create_calliope(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())

    # unit testing for tires; same for all car models
    def test_carrigan_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0
        tireType = 'Carrigan'
        sensor = [0, 0.9, 1, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, tireType, sensor)
        self.assertTrue(car.tire.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0
        tireType = 'Carrigan'
        sensor = [0, 0.8, 0.7, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, tireType, sensor)
        self.assertFalse(car.tire.needs_service())

    def test_octoprime_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0
        tireType = 'Octoprime'
        sensor = [3, 3, 2, 3]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, tireType, sensor)
        self.assertTrue(car.tire.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today
        current_mileage = 0
        last_service_mileage = 0
        tireType = 'Octoprime'
        sensor = [0, 0.8, 0.7, 0]

        car = create_calliope(today, last_service_date, current_mileage, last_service_mileage, tireType, sensor)
        self.assertFalse(car.tire.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4) # year changed for improved tire
        current_mileage = 0
        last_service_mileage = 0

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
