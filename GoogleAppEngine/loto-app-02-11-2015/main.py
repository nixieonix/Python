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
from random import sample

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		title = "Loto app"
		question = "Zelite generirati osem nakljucnih loto stevil? "
		template_var = {
			'title': title,
			'question': question
		}
		template = jinja_env.get_template('index.html')
  		self.response.out.write(template.render(template_var))

class lotoHandler(webapp2.RequestHandler):
	def get(self):
		title = "Loto app - cifre"
		lotoCombination = sorted(sample(range(1, 40), 8))

		"""def nakljucna_izbira_loto_stevil(): 
			i = 0
			lotoCombination = []
			#random.sample(range(1, 38), 8)
			#random_list = random.sample(xrange(38), 8) 
			while i < 8:
				lotoNumber = randint(1,38)
				lotoCombination.append(lotoNumber)
				i += 1 
			return lotoCombination
		
		def remove_duplicates(values):
			output = []
			seen = set()
			for value in values:
				# If value has not been encountered yet,
				# ... add it to both list and set.
				if value not in seen:
					output.append(value)
					seen.add(value)
			return output

		def stevilo_loto_stevilk(result):
			while len(result) < 8:
				lotoNumber = randint(1,38) 
				result.append(lotoNumber)
			return result

		values = nakljucna_izbira_loto_stevil()
		result = remove_duplicates(values)
		magicNumbers = sorted(stevilo_loto_stevilk(result))"""
		
		template_var = {
			'title': title,
			'magicNumbers': str(lotoCombination).strip('[]')
		}
		template = jinja_env.get_template('loto.html')
		self.response.write(template.render(template_var))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/loto.html', lotoHandler)
], debug=True)
