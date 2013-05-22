#coding: utf8.

print 'Content-Type: text/plain'
print ''

import main, cgi

form = cgi.FieldStorage()

print main.process(form.getvalue('translation_object'), form.getvalue('make_log'))