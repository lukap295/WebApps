#!Python.exe
import cgi
form = cgi.FieldStorage()
ime = form.getvalue("ime", "")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treca</title>
    <style>
        table{
            border: double;
        }
    </style>
</head>
<body>
    <form action="forma4.py" method="post">
        <br>
        <table>
        <tr>
            <td>Napomene:</td>
            <td><textarea name="napomena">Prelazak na izvanredan studij...</textarea></td>
        </tr>
        <tr>
            <td><button type="Submit">Next</button></td>
        </tr>
        </table>''')
print ('<input type="hidden" name="ime" value="''' + form.getvalue("ime") + '">')
print('<input type="hidden" name="status" value="''' + form.getvalue("status") + '">')
print('<input type="hidden" name="email" value="''' + form.getvalue("email") + '">')
print('<input type="hidden" name="smjer" value="''' + form.getvalue("smjer") + '">')
print('<input type="hidden" name="zavrsni" value="''' + form.getvalue("zavrsni") + '">')
('''</form>
</body>
</html> ''')

