Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','w')
type(estudiantes)
<class '_io.TextIOWrapper'>
estudiantes
<_io.TextIOWrapper name='C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt' mode='w' encoding='cp1252'>
estudiantes.write('CARLA,DANNYSA,ORLANYS')
21
estudiantes.close()
estuciantes
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    estuciantes
NameError: name 'estuciantes' is not defined. Did you mean: 'estudiantes'?
estudiantes
<_io.TextIOWrapper name='C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt' mode='w' encoding='cp1252'>
estudiantes.close()estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','w')
SyntaxError: invalid syntax
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','w')
estudiantes.write('ANA,SUSANA')
10
estudiante.close
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    estudiante.close
NameError: name 'estudiante' is not defined. Did you mean: 'estudiantes'?
estudiantes.write('ANA,SUSANA')
10
estudiantes.close
<built-in method close of _io.TextIOWrapper object at 0x000001ACE84EBCA0>
#Apertura delo archivo en modo de anadir
estudiantes = open(C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                   
SyntaxError: unterminated string literal (detected at line 1)
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')estudiantes = open(C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                                                                                                 
SyntaxError: unterminated string literal (detected at line 1)
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')estudiantes = open(C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                                                                                                 
SyntaxError: unterminated string literal (detected at line 1)
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                                                                                                 

estudiantes.write('CARLA,DANNYSA,ORLANYS')
                                                                                                 
21
estudiantes.close()
                                                                                                 
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','r')
                                                                                                 
estudiantes.read()
                                                                                                 
'ANA,SUSANAANA,SUSANACARLA,DANNYSA,ORLANYS'
estudiantes.read()
                                                                                                 
''
# Ubicarse a partir de la posicion 4
                                                                                                 
estudiantes.seek(4)
                                                                                                 
4
estudiantes.read()
                                                                                                 
'SUSANAANA,SUSANACARLA,DANNYSA,ORLANYS'
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                                                                                                 
estudiantes.close()
                                                                                                 
estudiantes = open ('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','w')
                                                                                                 
estudiantes.close()
                                                                                                 
# Con las 2 instrucciones anteriores se ha reiniciado el archivo
                                                                                                 
estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','a')
                                                                                                 
estudiantes.writelines(['DANNYSA\n','ORLANYS\n','CARLA\n'])
                                                                                                 
estudiantes.close()
                                                                                                 
>>> # Se abre el archivo en modo lectura
...                                                                                                  
>>> estudiantes = open('C:/ESP_PYTHON_20250331/NIVEL_I/CARLA/estudiantes.txt','r')
...                                                                                                  
>>> estudiantes.writelines()
...                                                                                                  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    estudiantes.writelines()
TypeError: _IOBase.writelines() takes exactly one argument (0 given)
>>> estudiantes.readlines()
...                                                                                                  
['DANNYSA\n', 'ORLANYS\n', 'CARLA\n']
>>> estudiantes.readlines()
...                                                                                                  
[]
>>> estudiantes.seek(0)
...                                                                                                  
0
>>> estudiantes.readlines()
...                                                                                                  
['DANNYSA\n', 'ORLANYS\n', 'CARLA\n']
>>> estudiantes.readline()
...                                                                                                  
''
>>> estudiantes.seek(0)
...                                                                                                  
0
>>> estudiantes.readline()
...                                                                                                  
'DANNYSA\n'
>>> estudiantes.readline()
...                                                                                                  
'ORLANYS\n'
>>> estudiantes.readline()
...                                                                                                  
'CARLA\n'
