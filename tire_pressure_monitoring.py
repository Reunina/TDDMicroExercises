import random


class Sensor(object):

    # The reading of the pressure value from the sensor
    # is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET = 16

    def pop_next_pressure_psi_value(self):
        pressure_telemetry_value = self.sample_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value


class PressureValidator:
    def check(self, psi_pressure_value: float) -> bool:
        pass


class TirePressureValidator(PressureValidator):
    """
    A Pressure validator for Tires
    """
    def __init__(self):
        self._low_pressure_threshold = 17.0
        self._high_pressure_threshold = 21.0

    def check(self, psi_pressure_value):
        return self._low_pressure_threshold < psi_pressure_value and\
               psi_pressure_value < self._high_pressure_threshold


class SimpleAlarm(object):
    """
    Alarm that goes on when presure is not valid
    """
    def __init__(self, pressureValidator, sensor):
        self._pressure_validator = pressureValidator
        self._sensor = sensor
        self._is_alarm_on = False

    def check(self):
        pressure = self._sensor.pop_next_pressure_psi_value()
        self._is_alarm_on = not self._pressure_validator.check(pressure)

    @property
    def is_alarm_on(self):
        return self._is_alarm_on

    @property
    def low_pressure_threshold(self):
        return self._pressure_validator._low_pressure_threshold

    @property
    def high_pressure_threshold(self):
        return self._pressure_validator._high_pressure_threshold


class Alarm(SimpleAlarm):
    """
    Alarm that goes on when presure is not on the expected range
    needs a Sensor
    """
    def __init__(self):
        SimpleAlarm.__init__(self, TirePressureValidator(), Sensor())

    def pair_with(self, new_sensor):
        self._sensor = new_sensor

    def is_using_sensor(self, sensor):
        return self._sensor == sensor

    def set_pressure_validator(self, validator):
        self._pressure_validator = validator

    def is_using_pressure_validator(self, validator):
        return self._pressure_validator == validator
