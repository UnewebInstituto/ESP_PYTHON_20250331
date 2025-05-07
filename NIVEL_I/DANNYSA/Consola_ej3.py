Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
type(estudiantes)
<class '_io.TextIOWrapper'>
estudiantes
<_io.TextIOWrapper name='C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt' mode='w' encoding='cp1252'>
estudiantes.write('CARLA','ORLANYS','DANNYSA')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    estudiantes.write('CARLA','ORLANYS','DANNYSA')
TypeError: TextIOWrapper.write() takes exactly one argument (3 given)
estudiantes.close()
estudiantes.write('CARLA,ORLANYS,DANNYSA')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    estudiantes.write('CARLA,ORLANYS,DANNYSA')
ValueError: I/O operation on closed file.
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
estudiantes.write('CARLA','ORLANYS','DANNYSA')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    estudiantes.write('CARLA','ORLANYS','DANNYSA')
TypeError: TextIOWrapper.write() takes exactly one argument (3 given)
estudiantes.write('CARLA,ORLANYS,DANNYSA')
21
estudiantes.close()
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
estudiantes.write('ana, susana')estudiantes.close()
SyntaxError: invalid syntax
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
estudiantes.write('ana, susana')
11
estudiantes.close()
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'a')
estudiantes.write('CARLA,ORLANYS,DANNYSA')
21
estudiantes.close()
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'r')
estudiantes.read()
'ana, susanaCARLA,ORLANYS,DANNYSA'
estudiantes.read()
''
estudiantes.seek(0)
0
estudiantes.read()
'ana, susanaCARLA,ORLANYS,DANNYSA'
estudiants.seek(4)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    estudiants.seek(4)
NameError: name 'estudiants' is not defined. Did you mean: 'estudiantes'?
estudiantes.read()
''
estudiantes.seek(4)
4

estudiantes.read()
' susanaCARLA,ORLANYS,DANNYSA'
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'a')estudiantes.close()
SyntaxError: invalid syntax
estudiantes.close()
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
estudiantes.close()
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'a')
>>> estudiantes.writelines(['dannysa','orlanys','carla'])
>>> estudiantes.close()
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')estudiantes.close()
SyntaxError: invalid syntax
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'w')
>>> estudiantes.close()
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'a')
>>> estudiantes.writelines(['dannysa\n','orlanys\n','carla\n'])
>>> estudiantes.close()
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/estudiantes.txt', 'r')
>>> estudiantes.readlines()
['dannysa\n', 'orlanys\n', 'carla\n']
>>> estudiantes.readlines()
[]
>>> estudiantes.seek(0)
0
>>> ()
... []estudiantes.readlines()
SyntaxError: multiple statements found while compiling a single statement
>>> estudiantes.readline()
'dannysa\n'
>>> estudiantes.readline()
'orlanys\n'
>>> estudiantes.readline()
'carla\n'
>>> estudiantes.readline()
''
>>> ()estudiantes.close()
SyntaxError: invalid syntax
>>> estudiantes.close()
