#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		return self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		return self.write(self.render_str(template, **kw))

	def render_template(self, view_filename, params=None):
		if not params:
			params = {}
		template = jinja_env.get_template(view_filename)
		return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
	def get(self):
		title = "Pretvornik Temperature"
		params = {
			'title': title
		}
		self.render_template('index.html', params=params)

	def post(self):
		temperatura = self.request.get('temperatura')
		option = self.request.get('option')
		result = self.pretvornik(temperatura, option)
		params = {
			'result':result
		}
		return self.render_template('index.html', params=params)

	def pretvornik(self, temperatura, option):
		if option == "celsius":
			fahrenheit = float(((int(temperatura) * 9)/5) + 32)
			return str(fahrenheit) + " &#730;F"
		elif option == "fahrenheit":
			celsius = float(((int(temperatura) - 32) * 5) / 9)
			return str(celsius) + " &#730;C"

class DataHandler(BaseHandler):
	def post(self):
		temperatura = self.request.get('temperatura')
		option = self.request.get('option')
		result = self.pretvornik(temperatura, option)
		self.write(result)

	def pretvornik(self, temperatura, option):
		if option == "celzija":
			kelvin = float(((int(temperatura) * 9)/5) + 32)
			return kelvin
		elif option == "kelvin":
			celzij = float(((int(temperatura) - 32) * 5) / 9)
			return celzij


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/data', DataHandler)
], debug=True)