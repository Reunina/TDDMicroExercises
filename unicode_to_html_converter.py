# This is for Python 2

# For Python 3 uncomment this line
import html as html_converter


class UnicodeFileToHtmlTextConverter(object):

    def __init__(self, full_filename_with_path):
        self.full_filename_with_path = full_filename_with_path
        self.converter = HtmlConverter(HtmlLineConverter())

    def convert_to_html(self):
        fileData = open(self.full_filename_with_path, "r")
        return self.converter.convert(fileData)


class HtmlConverter(object):

    def __init__(self, line_converter):
        self.line_converter = line_converter

    def convert(self, input):
        converted = ""
        for line in input:
            converted += self.line_converter.convert(line)
        return converted


class LineConverter:
    @staticmethod
    def convert(self, line: str) -> str:
        pass


class HtmlLineConverter(LineConverter):

    @staticmethod
    def convert(self, line):
        converted = ""
        converted = line.rstrip()
        converted += html_converter.escape(line, quote=True)
        converted += "<br />"
        return converted

    @staticmethod
    def strip_line(line):
        return line.rstrip()

    @staticmethod
    def escape_line(line):
        return html_converter.escape(line, quote=True)

    @staticmethod
    def convert_to_html_line(line):
        return line + "<br />"
