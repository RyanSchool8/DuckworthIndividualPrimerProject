#!/usr/bin/python

import os

print("Content-type:text/html\n\n")

print("<html>")
print("<head>")
print("<title>CGI Test</title>")
print("</head>")
print("<body>")
for entry in os.environ.keys():
	print("<b>%20s</b>: %s <br><br>" %  (entry, os.environ[entry]))
print("<h2>Simple CGI test</h2>")
print("</body>")
print("</html>")
