import unittest

from unicode_to_html_converter import HtmlLineConverter


class UnicodeFileToHtmlTextConverterTest(unittest.TestCase):

    def test_all_file_is_converted(self):
        self.assertTrue(True)

    def test_line_can_be_rstriped(self):
        input_line = " test line "
        expected_line = " test line"
        self.assertEquals(
            HtmlLineConverter.strip_line(input_line),
            expected_line)


if __name__ == "__main__":
    unittest.main()
