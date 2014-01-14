import urllib
import re
import HTMLParser
from jinja2 import evalcontextfilter, Markup, escape
from app import myapp

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
parser = HTMLParser.HTMLParser()

@myapp.template_filter('nl2br')
@evalcontextfilter
def nl2br(eval_ctx, value):
	result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n','<br>\n') for p in _paragraph_re.split(escape(value)))
	if eval_ctx.autoescape:
		result = Markup(result)
	return result

@myapp.template_filter('urlencode')
def urlencode(uri, **query):
	return urllib.quote_plus(uri.encode("utf8"))

@myapp.template_filter('htmlentitydecode')
@evalcontextfilter
def htmlentitydecode(eval_ctx, value):
	return parser.unescape(value)


myapp.jinja_env.globals['urlencode'] = urlencode
myapp.jinja_env.globals['nl2br'] = nl2br
myapp.jinja_env.globals['htmlentitydecode'] = htmlentitydecode
