#!Python.exe
import cgi

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prva</title>
    <style>
        table{
            border: double;
        }
    </style>
</head>
<body>
    <form action="forma2.py" method="post">
        <br>
        <table>
        <tr>
            <td>Ime:</td>
            <td><input type="text" name="ime"></td>
        </tr>
        <tr>
            <td>Lozinka</td>
            <td><input type="password" name="lozinka"></td>
        </tr>
        <tr>
            <td>Ponovi lozinku</td>
            <td><input type="password" name="ponoviloz"></td>
        </tr>
        <tr>
            <td><button type="Submit">Next</button></td>
        </tr>
        </table>
        </form>
</body>
</html> ''')
form = cgi.FieldStorage()
