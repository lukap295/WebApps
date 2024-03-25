#!Python.exe
import cgi

form = cgi.FieldStorage()

ime = form.getvalue("ime")
if(form.getvalue("lozinka") != form.getvalue("ponoviloz")):
    print("Location: forma1.py")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Druga</title>
    <style>
        table{
            border: double;
        }
    </style>
</head>
<body>
    <form action="forma3.py" method="post">
        <br>
        <table>
        <tr>
            <td>Status:</td>
            <td><input type="radio" name="status" value="Redovan">
                <label for="Redovan">Redovan</label>
                <input type="radio" name="status" value="Izvanredan">
                <label for="Izvanredan">Izvanredan</label></td>
        </tr>
        <tr>
            <td>E-mail</td>
            <td><input type="email" name="email"></td>
        </tr>
        <tr>
            <td>Smjer</td>
            <td><select name="smjer">
                <option value="Baze Podataka">Baze Podataka</option>
                <option value="Programiranje">Programiranje</option>
                <option value="Web Aplikacije">Web Aplikacije</option>
                <option value="Analiza">Analiza</option></select>
            </td>
        </tr>
        <tr>
            <td>Zavrsni</td>
            <td><input type="checkbox" name="zavrsni"></td>
        </tr>
        <tr>
            <td><button type="Submit">Next</button></td>''')
print('<input type="hidden" name="ime" value="''' + form.getvalue("ime") + '">')
('''
        </tr>
        </table>
        </form>
</body>
</html> ''')

