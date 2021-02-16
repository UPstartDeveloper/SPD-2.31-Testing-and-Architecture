# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        # Each wheel has a single tpms attached to it. 
        self.tpms_list = list()  # Tire Pressure Monitoring System.
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)
            self.tpms_list.append(w.tpms)
        self.cabin = cabin
        self.fuel_tank = fuel_tank

    
class Wheel:
    def __init__(self, tpms, car = None, wheel_location = None):
        self.tpms = tpms
        self.car = car
        self.wheel_location = wheel_location

    def install_tire(self):
        print('remove old tube.')
        print('cleaned tpms: ', self.tpms.get_serial_number(), '.')
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        return self.tpms.get_pressure()
    
    def set_car(self, car):
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System.
    """
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number
    
class Engine:
    def __init__(self):
        pass
    
class FuelTank:
    def __init__(self):
        pass
    
class Cabin:
    def __init__(self):
        pass    
    

engine = Engine()
tpms_di = {'front-right': Tpms(983408543), 'front-left':Tpms(4343083),
               'back-right':Tpms(23654835), 'back-left':Tpms(3498857)}

wheels = [
    Wheel(tpms_di['front-right'], wheel_location='front-right'), 
    Wheel(tpms_di['front-left'], wheel_location='front-left'), 
    Wheel(tpms_di['back-right'], wheel_location='back-right'), 
    Wheel(tpms_di['back-left'], wheel_location='back-left')]

cabin  = Cabin()


fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)
