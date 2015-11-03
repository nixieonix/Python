#!/usr/bin/env python
import os
import jinja2
import webapp2
import time

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

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Home | Nika Grabnar"
    	template_var = {
    		'title': title
    	}
    	template = jinja_env.get_template('index.html')
        self.response.out.write(template.render(template_var))

class blogHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Blog | Nika Grabnar"
    	template_var = {
    		'title': title
    	}
    	template = jinja_env.get_template('blog.html')
        self.response.out.write(template.render(template_var))

class projectsHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Projects | Nika Grabnar"
    	template_var = {
    		'title': title
    	}
    	template = jinja_env.get_template('projects.html')
        self.response.out.write(template.render(template_var))

class contactsHandler(webapp2.RequestHandler):
    def get(self):
    	title = "Contacts | Nika Grabnar"
    	template_var = {
    		'title': title
    	}
    	template = jinja_env.get_template('contacts.html')
        self.response.out.write(template.render(template_var))
       

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog.html', blogHandler),
    webapp2.Route('/projects.html', projectsHandler),
    webapp2.Route('/contacts.html', contactsHandler)
], debug=True)
