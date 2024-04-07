#!python.exe
from http import cookies
import cgi, time, os
import podaci

form = cgi.FieldStorage()

cookie = cookies.SimpleCookie()

cookie_string = os.environ.get('HTTP_COOKIE')

cookie_object = cookies.SimpleCookie(cookie_string)

for data in form:
    cookie[data] = form.getvalue(data)
print(cookie)

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">''')
print('''
    <title>Prva</title>
    <style>
        table, th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <form method="post">''')
print(''' <br>
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
                <td><input type="radio" name="{key}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{key}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{key}" value="Passed">Passed</td>
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
                <td><input type="radio" name="{key}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{key}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{key}" value="Passed">Passed</td>
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
                <td><input type="radio" name="{key}" value="Not selected">Not selected</td>
                <td><input type="radio" name="{key}" value="Enrolled">Enrolled</td>
                <td><input type="radio" name="{key}" value="Passed">Passed</td>
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
            print(f'''
                <tr>
                    <td>{value['name']}</td>
                    <td>{value['ects']}</td>''')
            if key in form:
                status = form.getvalue(key)
            else:
                status = cookie_object.get(key).value if key in cookie_object else None
            print(f'''
                    <td>{status}</td>
                </tr>''')
            break


print('''</form>
</body>
</html> ''')

