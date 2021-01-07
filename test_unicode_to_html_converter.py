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

    def test_line_can_be_escaped(self):
        input_line = " test & <and>  \"line' "
        expected_line = " test &amp; &lt;and&gt;  &quot;line&#x27; "
        self.assertEquals(
            HtmlLineConverter.escape_line(input_line),
            expected_line)

    def test_line_can_be_converted_to_an_html_line(self):
        input_line = " test line "
        expected_line = " test line <br />"
        self.assertEquals(
            HtmlLineConverter.convert_to_html_line(input_line),
            expected_line)


if __name__ == "__main__":
    unittest.main()

