#!python.exe
from http import cookies
import cgi, time
import podaci

form = cgi.FieldStorage()

cookie = cookies.SimpleCookie()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prva</title>
    <style>
        table, th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <form method="post">
        <br>
            <button type="Submit" value="submit" name="submit1">1st Year</button>
            <button type="Submit" value="submit" name="submit2">2nd Year</button>
            <button type="Submit" value="submit" name="submit3">3rd Year</button>
            <button type="Submit" value="upisni" name="upisni">Upisni list</button>
        <table>''')
if 'submit1' in form:
    year = 1
    print('''   
    <tr>
        <td>1st Year</td>
        <td>Ecst</td>
        <td>Status</td>
    </tr>''')
    for key, value in podaci.subjects.items():
        for k in value:
            if year == value[k]:
                print(f'''<tr>
                <td>{value['name']}</td>
                <td>{value['ects']}</td>
                <td><input type="radio" name="{value['name']}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{value['name']}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{value['name']}" value="Passed">Passed</td>
                </tr>''')
elif 'submit2' in form:
    year = 2
    print('''   
    <tr>
        <td>2nd Year</td>
        <td>Ecst</td>
        <td>Status</td>
    </tr>''')
    for key, value in podaci.subjects.items():
        for k in value:
            if year == value[k]:
                print(f'''<tr>
                <td>{value['name']}</td>
                <td>{value['ects']}</td>
                <td><input type="radio" name="{value['name']}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{value['name']}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{value['name']}" value="Passed">Passed</td>
                </tr>''')
elif 'submit3' in form:
    year = 3
    print('''   
    <tr>
        <td>2nd Year</td>
        <td>Ecst</td>
        <td>Status</td>
    </tr>''')
    for key, value in podaci.subjects.items():
        for k in value:
            if year == value[k]:
                print(f'''<tr>
                <td>{value['name']}</td>
                <td>{value['ects']}</td>
                <td><input type="radio" name="{value['name']}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{value['name']}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{value['name']}" value="Passed">Passed</td>
                </tr>''')
elif 'upisni' in form:
    print('''
    <tr><td>Upisni list</td></tr> 
    <tr>
        <td>Subjects</td>
        <td>Ecst</td>
        <td>Status</td>
    </tr>''')
    for key, value in podaci.subjects.items():
        for k in value:
            print(f'''<tr>
            <td>{value['name']}</td>
            <td>{value['ects']}</td>
            </tr>''')
            break
print('''</form>
</body>
</html> ''')