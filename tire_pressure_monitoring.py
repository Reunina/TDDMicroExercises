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


class Alarm(object):
    """
    Alarm that goes on when presure is not on the expected range
    needs a Sensor
    """
    def __init__(self):
        self._pressure_validator = TirePressureValidator()
        self._sensor = Sensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        self.set_alarm_if_pressure_is_not_authorized(psi_pressure_value)

    def set_alarm_if_pressure_is_not_authorized(self, psi_pressure_value):
        if (not self._pressure_validator.check(float(psi_pressure_value))):
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on

    @property
    def low_pressure_threshold(self):
        return self._pressure_validator._low_pressure_threshold

    @property
    def high_pressure_threshold(self):
        return self._pressure_validator._high_pressure_threshold
