"""by Kami Bigdely
Docstrings and blank lines"""

class OnBoardTemperatureSensor:

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        '''Instaniates a new OnBoardTemperatureSensor object.'''
        pass

    def read_voltage(self):
        '''Returns the value 2.7'''       
        return 2.7

    def get_temperature(self):
        '''Returns the voltage, converted to a temperature value.'''
        return (
            self.read_voltage() * 
            OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]
        )
  

class CarbonMonoxideSensor:

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor=None):
        """Instaniates a new CarbonMonoxideSensor object. 
        
        Args:
            temperature_sensor: an instance of OnBoardTemperatureSensor.
                                Use to initialize self.on_board_temp_sensor.
                                If not provided, we'll make a new instance.
                        
        Returns: None
        """
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Computes the CO level given the voltage on the sensor.

        We multiply the voltage on the sensor (2.3), by the temperature
        and the voltage/carbon monoxide conversion factor.

        Args: None
        
        Returns: None
        """
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = (
            CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
                sensor_voltage, self.on_board_temp_sensor.get_temperature()
            )
        )
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        '''In real life, it should read from hardware.'''        
        return 2.3

    @classmethod
    def convert_voltage_to_carbon_monoxide_level(cls, voltage, temperature):
        '''Compute and return CO, given voltage and temperate.'''
        return voltage * cls.VOLTAGE_TO_CO_FACTOR * temperature
    

class DisplayUnit:

    def __init__(self):
        '''Instantiates a new DisplayUnit.'''
        self.string = ''

    def display(self, msg):
        '''Displays the message on the unit.'''
        print(msg)


class CarbonMonoxideDevice():

    def __init__(self, co_sensor, display_unit):
        """Instantiates a new CO device.
        
        Args:
            co_sensor: a CarbonMonoxideSensor instance
            display_unit: a DisplayUnit instance

        Returns: None
        """
        self.carbon_monoxide_sensor = co_sensor 
        self.display_unit = display_unit

    def display(self):
        """Prints out the carbon monoxide level.

        We compute the CO level from the carbon_monoxide_sensor attribute,
        and print it out using the display_unit attribute.

        Args: None

        Returns: None
        """
        msg = (
            'Carbon Monoxide Level is : ' +  
            str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        )
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
    