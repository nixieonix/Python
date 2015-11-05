#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
		title = "Calculator"
		params = {
			'title': title
		}
		self.render_template('index.html', params=params)

	def post(self):
		data = self.request.get('my_data')
		self.write(data)
		stevilo1 = self.request.get('stevilo1')
		stevilo2 = self.request.get('stevilo2')
		operator = self.request.get('operator')
		result = self.calculate(stevilo1, stevilo2, operator)
		params = {
			'result': "Answer: " + result
		}
		return self.render_template('index.html', params=params)

	def calculate(self, stevilo1, stevilo2, operator):
		if operator == "+":
			sest = int(stevilo1) + int(stevilo2)
			return str(sest)
		elif operator == "-":
			odst = int(stevilo1) - int(stevilo2)
			return str(odst)
		elif operator == "*":
			mnoz = int(stevilo1) * int(stevilo2)
			return str(mnoz)
		elif operator == "/":
			delj = int(stevilo1) / int(stevilo2)
			return str(delj)

class DataHandler(BaseHandler):
	def post(self):
		data = self.request.get('my_data')
		self.write(data)
		stevilo1 = self.request.get('stevilo1')
		stevilo2 = self.request.get('stevilo2')
		operator = self.request.get('operator')
		result = self.calculate(stevilo1, stevilo2, operator)

		self.write(result)

	def calculate(self, stevilo1, stevilo2, operator):
		if operator == "+":
			sest = int(stevilo1) + int(stevilo2)
			return str(sest)
		elif operator == "-":
			odst = int(stevilo1) - int(stevilo2)
			return str(odst)
		elif operator == "*":
			mnoz = int(stevilo1) * int(stevilo2)
			return str(mnoz)
		elif operator == "/":
			delj = int(stevilo1) / int(stevilo2)
			return str(delj)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/data', DataHandler)
], debug=True)
