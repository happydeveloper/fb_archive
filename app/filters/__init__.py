import urllib
import re
import HTMLParser
from jinja2 import evalcontextfilter, Markup, escape
from app import engfordev

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
parser = HTMLParser.HTMLParser()

@engfordev.template_filter('nl2br')
@evalcontextfilter
def nl2br(eval_ctx, value):
	result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n','<br>\n') for p in _paragraph_re.split(escape(value)))
	if eval_ctx.autoescape:
		result = Markup(result)
	return result

@engfordev.template_filter('urlencode')
def urlencode(uri, **query):
	return urllib.quote_plus(uri.encode("utf8"))

@engfordev.template_filter('htmlentitydecode')
@evalcontextfilter
def htmlentitydecode(eval_ctx, value):
	return parser.unescape(value)


engfordev.jinja_env.globals['urlencode'] = urlencode
engfordev.jinja_env.globals['nl2br'] = nl2br
engfordev.jinja_env.globals['htmlentitydecode'] = htmlentitydecode
