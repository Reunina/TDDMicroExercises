import unittest

from tire_pressure_monitoring import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_set_when_pressure_is_too_high(self):
        alarm = Alarm()
        alarm.set_alarm_when_pressure_is_off(alarm.maximum_pressure_authorized + 1)
        self.assertTrue(alarm.is_alarm_on, "Alarm should be set when pressure is too hight")


if __name__ == "__main__":
	unittest.main()
    