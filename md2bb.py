import mistune


class BBRender(mistune.Renderer):
    def block_code(self, code, lang=None):
        return '[code]%s[/code]\n' % code

    def block_quote(self, text):
        return '[quote=Nobody]%s[/quote]\n' % text.rstrip('\n')

    def header(self, text, level, raw=None):
        return '[h%d]%s[/h%d]\n' % (level, text, level)

    def list(self, body, ordered=True):
        tag = 'list'
        if ordered:
            tag = 'olist'
        return '[%s]\n%s[/%s]\n' % (tag, body, tag)

    def list_item(self, text):
        return '[*]%s\n' % text

    def paragraph(self, text):
        return '%s\n' % text.strip(' ')

    def table(self, header, body):
        return '[table]\n%s%s[/table]\n' % (header, body)

    def table_row(self, content):
        return '[tr]\n%s[/tr]\n' % content

    def table_cell(self, content, **flags):
        if flags['header']:
            tag = 'th'
        else:
            tag = 'td'
        return '[%s]%s[/%s]\n' % (tag, content, tag)

    def double_emphasis(self, text):
        return '[b]%s[/b]' % text

    def emphasis(self, text):
        return '[i]%s[/i]' % text

    def codespan(self, text):
        text = mistune.escape(text.rstrip(), smart_amp=False)
        return '[code]%s[/code]' % text

    def strikethrough(self, text):
        return '[strike]%s[/strike]' % text

    def autolink(self, link, is_email=False):
        text = link = mistune.escape_link(link)
        if is_email:
            link = 'mailto:%s' % link
        return '[url=%s]%s[/url]' % (link, text)

    def link(self, link, title, text):
        link = mistune.escape_link(link)
        return '[url=%s]%s[/url]' % (link, text)


text = open('example.md').read()
# renderer = mistune.Renderer(escape=True, hard_wrap=True)
renderer = BBRender(escape=True, hard_wrap=True)
# use this renderer instance
markdown = mistune.Markdown(renderer=renderer)
with open('example.bb', 'w') as f:
    f.write(markdown(text))
