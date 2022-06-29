import textwrap


class Indent():
    def __init__(self, style, msg):
        self.msg = msg
        self.type = style

    def clean(msg):
        pref_width = 70
        wrapper = textwrap.TextWrapper(
            initial_indent='             ', width=pref_width,
            subsequent_indent='             ')
        return wrapper.fill(msg)

    def item(msg):
        pref_width = 70
        wrapper = textwrap.TextWrapper(
            initial_indent='      ', width=pref_width,
            subsequent_indent='             ')
        return wrapper.fill(msg)

    def marker(msg):
        pref_width = 70
        wrapper = textwrap.TextWrapper(
            initial_indent='', width=pref_width,
            subsequent_indent='         ')
        return wrapper.fill(msg)
