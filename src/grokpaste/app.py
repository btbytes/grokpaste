import grok
from zope.interface import Interface
from datetime import datetime
from random import randint
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from grokpaste.utils import slugify
from persistent.dict import PersistentDict

class GrokPaste(grok.Application, grok.Container):
    pass

class Layout(grok.View):
    grok.context(Interface)
    
class Entry(grok.Model):
    def __init__(self, text, title=None, syntax=None, name=None, hold=False):
        self.text = text
        self.syntax = syntax
        self.hold = hold
        self.title = title
        self.name = name
        self.created = datetime.now()
        self.lastview = None
                
        if len(name) < 1:
            self.name = 'Anonymous'
        
        if self.syntax:
            try:
                self.lexer = get_lexer_by_name(self.syntax, stripall=True)
            except:
                self.lexer = get_lexer_by_name("text", stripall=True)
            
    def render_text(self):        
        formatter = HtmlFormatter(linenos=True, cssclass="highlight")
        return highlight(self.text, self.lexer, formatter)
    
    def render_html(self):
        formatter = HtmlFormatter(linenos=False, cssclass="highlight")
        return highlight(self.text, self.lexer, formatter)
            
    def after(self):
        self.lastview = datetime.now()
        
    
class EntryIndex(grok.View):
    grok.context(Entry)
    grok.name('index')
    
class EntryPlain(grok.View):
    grok.context(Entry)
    grok.name('plain')

class EntryHtml(grok.View):
    grok.context(Entry)
    grok.name('html')
        
class GrokPasteIndex(grok.View):
    grok.context(GrokPaste)
    grok.name('index')
    languages = ['text', 'python', 'html', 'ruby', 'c']
    userinfo = PersistentDict(dict(name='', syntax='text'))
    def update(self, title=None, text=None, syntax=None, name=None, hold=False):
        if text is None:
            return
        self.userinfo = PersistentDict(dict(name=name, syntax=syntax))
        if len(title) < 1:
            now = datetime.now()
            title = str(now.strftime('%s-')+str(randint(1,10000)))
            
        url = slugify(title)    
        self.context[url] = Entry(text, title, syntax, name, hold)

class About(grok.View):
    """The About Page"""
    grok.context(GrokPaste)
    grok.name('about')
    def foo(self):
        c = Cookie('name', 'value', max_age=3, comment='no!', version=1)
        c.value = "I've changed my mind"
        c.raw_value = "...again"
        request.response.addCookie(c)
        return self.request.cookies.get('name', 'default value for name')
    