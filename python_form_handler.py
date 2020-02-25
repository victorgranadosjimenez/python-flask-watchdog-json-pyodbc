import cgi

form = cgi.FieldStorage()
value = form.getvalue("clothes")

print(value)
