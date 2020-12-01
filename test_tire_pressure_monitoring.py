import unittest
import random

from tire_pressure_monitoring import Alarm, Sensor, TirePressureValidator,\
    PressureValidator


class AlarmTest(unittest.TestCase):
    def test_alarm_is_off_at_initialization(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_alarm_stays_off_when_pressure_is_in_authorized_range(self):
        alarm = Alarm()
        valid_pressure = self.generate_authorized_pressure_for_alarm(alarm)
        alarm.pair_with(DummySensor(valid_pressure))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_alarm_is_set_when_pressure_is_in_too_low(self):
        alarm = Alarm()
        unvalid_pressure = self.generate_too_low_pressure_for_alarm(alarm)
        alarm.pair_with(DummySensor(unvalid_pressure))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_alarm_is_set_when_pressure_is_in_too_high(self):
        alarm = Alarm()
        unvalid_pressure = self.generate_too_high_pressure_for_alarm(alarm)
        alarm.pair_with(DummySensor(unvalid_pressure))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def generate_authorized_pressure_for_alarm(self, alarm):
        return random.uniform(
            alarm.low_pressure_threshold, alarm.high_pressure_threshold)

    def generate_too_low_pressure_for_alarm(self, alarm):
        return random.uniform(
            alarm.low_pressure_threshold - alarm.low_pressure_threshold,
            alarm.low_pressure_threshold)

    def generate_too_high_pressure_for_alarm(self, alarm):
        return random.uniform(
            alarm.high_pressure_threshold,
            alarm.high_pressure_threshold + alarm.high_pressure_threshold)

    def test_pairing_with_another_sensor_is_possible(self):
        alarm = Alarm()
        test_sensor = DummySensor(0)
        self.assertFalse(alarm.is_using_sensor(test_sensor))
        alarm.pair_with(test_sensor)
        self.assertTrue(alarm.is_using_sensor(test_sensor))

    def test_using_another_pressure_validator_is_possible(self):
        alarm = Alarm()
        test_pressure_validator = DummyPressureValidator()
        self.assertFalse(
            alarm.is_using_pressure_validator(test_pressure_validator))
        alarm.set_pressure_validator(test_pressure_validator)
        self.assertTrue(
            alarm.is_using_pressure_validator(test_pressure_validator))


class DummyPressureValidator(PressureValidator):
    pass


class DummySensor(Sensor):
    def __init__(self, pressure):
        self._pressure = pressure

    def pop_next_pressure_psi_value(self):
        return self._pressure


class TirePressureValidatorTest(unittest.TestCase):
    def test_pressure_is_not_valid_when_under_17_0_included(self):
        low_pressure = random.uniform(0.0, 17.0)
        self.assertFalse(TirePressureValidator().check(low_pressure))
        self.assertFalse(TirePressureValidator().check(17.0))

    def test_pressure_is_not_valid_when_over_21_0_included(self):
        self.assertFalse(TirePressureValidator().check(float("inf")))
        self.assertFalse(TirePressureValidator().check(21.0))

    def test_pressure_is_valid_when_over_17_0_and_under_21_0(self):
        random_valid_pressure = random.uniform(17.1, 19.9)
        self.assertTrue(TirePressureValidator().check(random_valid_pressure))


if __name__ == "__main__":
    unittest.main()
