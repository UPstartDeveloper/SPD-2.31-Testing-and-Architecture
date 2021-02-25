class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def register_observer(observer):
        pass

    def remove_observer(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notify_observers():
        pass


# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# weather_data now implements the subject interface.
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def remove_observer(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notify_observers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()

    # other weather_data methods here.


class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer
        # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(
            "Current conditions:",
            self.temerature,
            "F degrees and",
            self.humidity,
            "[%] humidity",
            "and pressure",
            self.pressure,
        )


class StatisticsDisplay(Observer):
    """The StatisticsDisplay class should keep track of the min/average/max
    measurements and display them."""

    def __init__(self, weather_data):
        self.temps = []  # all recorded temperatures
        self.humidities = []  # all recorded humidity measurements
        self.pressures = []  # all recorded pressures

        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer

    def update(self, temperature, humidity, pressure):
        # add the new measurements to our records
        self.temps.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)
        # display the changes
        self.display()

    def get_stats(self, units):
        """return min, max, and avg of a list"""
        # decide the list we want stats from
        if units == "F degrees":
            values = self.temps
            measurement = "temp"
        elif units == "[%]":
            values = self.humidities
            measurement = "humidity"
        else:  # get the pressure, no units
            values = self.pressures
            measurement = "pressure"
        # form the message
        message = (
            f"Min {measurement}: {min(values)} {units}"
            + f"Avg {measurement}: {max(values)} {units}"
            + f"Max {measurement}: {sum(values) / len(values)} {units}"
        )
        # return the message
        return message

    def display(self):
        # display stats for all 3 measures
        if len(self.temps) > 0:
            temp_message = self.get_stats("F degrees")
        else:
            temp_message = "No temperature stats"
        print(temp_message)

        if len(self.humidities) > 0:
            h_message = self.get_stats("[%]")
        else:
            h_message = "No humidity stats"
        print(h_message)

        if len(self.pressures) > 0:
            pressure_message = self.get_stats("")
        else:
            pressure_message = "No pressure stats"
        print(pressure_message)


class ForecastDisplay(Observer):
    """The ForecastDisplay class shows the weather forcast based on the current
    temperature, humidity and pressure."""

    def __init__(self, weather_data):
        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer
        # init the forecast metrics
        self.forecast_temp = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humidity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print(
            "Forecast conditions:",
            self.forecast_temp,
            "F degrees and",
            self.forecast_humidity,
            "[%] humidity",
            "and pressure",
            self.forecast_pressure,
        )


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        # Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        stats_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)

        # un-register the observer
        weather_data.remove_observer(current_display)
        weather_data.set_measurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
