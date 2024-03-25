#!Python.exe
import cgi
form = cgi.FieldStorage()
ime = form.getvalue("ime", "")
status = form.getvalue("status", "")
email = form.getvalue("email", "")
smjer = form.getvalue("smjer", "")
zavrsni = form.getvalue("zavrsni", "")
napomena = form.getvalue("napomena", "")
if(zavrsni):
    zavrsni = 'Da'
else:
    zavrsni = 'Ne'
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cetvrta</title>
    <style>
        table{
            border: double;
        }
    </style>
</head>
<body>
    <form method="post">
        <br>
        <table>
        <tr>
            <td>Ime:</td>
            <td>''')
print(ime)
print('''</td>
        </tr>
        <tr>
            <td>E-mail:</td>
            <td>''')
print(email)
print('''</td>
        </tr>
        <tr>
            <td>Status:</td>
            <td>''')
print(status)
print('''</td>
        </tr>
        <tr>
            <td>Smjer:</td>
            <td>''')
print(smjer)
print('''</td>
        </tr>
        <tr>
            <td>Zavrsni rad:</td>
            <td>''')
print(zavrsni)
print('''</td>
        </tr>
        <tr>
            <td>Napomene:</td>
            <td>''')
print(napomena)
print('''</td>
        </tr>
        <tr>
            <td><button type="Submit">Next</button></td>
        </tr>
        </table>
        </form>
      <br>
      <a href="forma1.py">Na pocetak</a>
</body>
</html> ''')