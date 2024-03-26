#!/usr/bin/env python3

from flask import Flask, render_template
import os
import unittest

appp = Flask(__name__)

_output = "Test 1"

class TestMethods(unittest.TestCase):
	def test_anything(self):
		self.assertEqual('1', '1')
		self.assertEqual('Test' in _output)

@app.route('/')
def index():
	return _output

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
