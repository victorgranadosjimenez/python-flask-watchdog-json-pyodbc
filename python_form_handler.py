import cgi

form = cgi.FieldStorage()
value = form.getvalue("food")

print(value)
