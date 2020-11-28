import unittest
import random

from tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):
    def test_arlam_is_off_at_initialization(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_alarm_stays_off_when_pressure_is_in_authorized_range(self):
        alarm = Alarm()
        valid_pressure = self.generate_authorized_pressure_for_alarm(alarm)
        alarm.set_alarm_if_pressure_is_not_authorized(valid_pressure)
        self.assertFalse(alarm.is_alarm_on)

    def test_alarm_is_set_when_pressure_is_in_too_low(self):
        alarm = Alarm()
        valid_pressure = self.generate_too_low_pressure_for_alarm(alarm)
        alarm.set_alarm_if_pressure_is_not_authorized(valid_pressure)
        self.assertTrue(alarm.is_alarm_on)

    def test_alarm_is_set_when_pressure_is_in_too_high(self):
        alarm = Alarm()
        valid_pressure = self.generate_too_high_pressure_for_alarm(alarm)
        alarm.set_alarm_if_pressure_is_not_authorized(valid_pressure)
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


if __name__ == "__main__":
    unittest.main()
