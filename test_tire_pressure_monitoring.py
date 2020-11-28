import unittest

from tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):
    def test_arlam_is_off_at_initialization(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)


if __name__ == "__main__":
    unittest.main()
