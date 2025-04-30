Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, ' x ', j, ' = ', i*j)
        j += 1
    i += 1
    print ('')

    
1  x  1  =  1
1  x  2  =  2
1  x  3  =  3
1  x  4  =  4
1  x  5  =  5
1  x  6  =  6
1  x  7  =  7
1  x  8  =  8
1  x  9  =  9

2  x  1  =  2
2  x  2  =  4
2  x  3  =  6
2  x  4  =  8
2  x  5  =  10
2  x  6  =  12
2  x  7  =  14
2  x  8  =  16
2  x  9  =  18

3  x  1  =  3
3  x  2  =  6
3  x  3  =  9
3  x  4  =  12
3  x  5  =  15
3  x  6  =  18
3  x  7  =  21
3  x  8  =  24
3  x  9  =  27

4  x  1  =  4
4  x  2  =  8
4  x  3  =  12
4  x  4  =  16
4  x  5  =  20
4  x  6  =  24
4  x  7  =  28
4  x  8  =  32
4  x  9  =  36

5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45

6  x  1  =  6
6  x  2  =  12
6  x  3  =  18
6  x  4  =  24
6  x  5  =  30
6  x  6  =  36
6  x  7  =  42
6  x  8  =  48
6  x  9  =  54

7  x  1  =  7
7  x  2  =  14
7  x  3  =  21
7  x  4  =  28
7  x  5  =  35
7  x  6  =  42
7  x  7  =  49
7  x  8  =  56
7  x  9  =  63

8  x  1  =  8
8  x  2  =  16
8  x  3  =  24
8  x  4  =  32
8  x  5  =  40
8  x  6  =  48
8  x  7  =  56
8  x  8  =  64
8  x  9  =  72

9  x  1  =  9
9  x  2  =  18
9  x  3  =  27
9  x  4  =  36
9  x  5  =  45
9  x  6  =  54
9  x  7  =  63
9  x  8  =  72
9  x  9  =  81

Ciclo anidado para producir la tabla de multiplicar
SyntaxError: invalid syntax

i = 1
for i in range (1,10):
    j = 1
    for j in range (1,10):
        print(i, ' x ', j, ' = ', i*j)

        
1  x  1  =  1
1  x  2  =  2
1  x  3  =  3
1  x  4  =  4
1  x  5  =  5
1  x  6  =  6
1  x  7  =  7
1  x  8  =  8
1  x  9  =  9
2  x  1  =  2
2  x  2  =  4
2  x  3  =  6
2  x  4  =  8
2  x  5  =  10
2  x  6  =  12
2  x  7  =  14
2  x  8  =  16
2  x  9  =  18
3  x  1  =  3
3  x  2  =  6
3  x  3  =  9
3  x  4  =  12
3  x  5  =  15
3  x  6  =  18
3  x  7  =  21
3  x  8  =  24
3  x  9  =  27
4  x  1  =  4
4  x  2  =  8
4  x  3  =  12
4  x  4  =  16
4  x  5  =  20
4  x  6  =  24
4  x  7  =  28
4  x  8  =  32
4  x  9  =  36
5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45
6  x  1  =  6
6  x  2  =  12
6  x  3  =  18
6  x  4  =  24
6  x  5  =  30
6  x  6  =  36
6  x  7  =  42
6  x  8  =  48
6  x  9  =  54
7  x  1  =  7
7  x  2  =  14
7  x  3  =  21
7  x  4  =  28
7  x  5  =  35
7  x  6  =  42
7  x  7  =  49
7  x  8  =  56
7  x  9  =  63
8  x  1  =  8
8  x  2  =  16
8  x  3  =  24
8  x  4  =  32
8  x  5  =  40
8  x  6  =  48
8  x  7  =  56
8  x  8  =  64
8  x  9  =  72
9  x  1  =  9
9  x  2  =  18
9  x  3  =  27
9  x  4  =  36
9  x  5  =  45
9  x  6  =  54
9  x  7  =  63
9  x  8  =  72
9  x  9  =  81


Ciclos condicionados
SyntaxError: incomplete input

continuar = 'S'
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar.upper()
    print ("Usted eligiò continuar...")
print("Usted eligiò salir...")
SyntaxError: invalid syntax
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar.upper()
    print ("Usted eligiò continuar...")
print("Usted eligiò salir...")
SyntaxError: invalid syntax

while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar.upper()
    print ("Usted eligiò continuar...")

    
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?S
'S'
Usted eligiò continuar...
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?s
'S'
Usted eligiò continuar...
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar = continuar.upper()
    print ("Usted eligiò continuar...")

    
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar.upper()
    print ("Usted eligiò continuar...")
print("Usted eligiò salir...")
SyntaxError: invalid syntax

continuar = 'S'
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar.upper()
    print ("Usted eligiò continuar...")

    
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?s
'S'
Usted eligiò continuar...
s
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s
NameError: name 's' is not defined
NameError: name 's' is not defined
SyntaxError: invalid syntax

continuar = 'S'
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar = continuar.upper()
    print ("Usted eligiò continuar...")
    
SyntaxError: multiple statements found while compiling a single statement


continuar = 'S':
    
SyntaxError: incomplete input
continuar = 'S':
    
SyntaxError: incomplete input


continuar = 'S'
while continuar == 'S':
    print ('Acciones en ejecuciòn...')
    continuar = input ('¿Usted desea continuar (S/N):?')
    continuar = continuar.upper()
    print ("Usted eligiò continuar...")

    
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?S
Usted eligiò continuar...
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?S
Usted eligiò continuar...
Acciones en ejecuciòn...
¿Usted desea continuar (S/N):?N
Usted eligiò continuar...
while True:
    print('Acciones en ejecuciòn')
    continuar = input('¿Continuar (S/N):?')
    if continuar.upper() == 'S':
        print('Continuan las acciones en ejecuciòn')
        continue
    else:
        print('Se detienen las acciones. Fin del ciclo')
        break

    
Acciones en ejecuciòn
¿Continuar (S/N):?s
Continuan las acciones en ejecuciòn
Acciones en ejecuciòn
¿Continuar (S/N):?n
Se detienen las acciones. Fin del ciclo
2+2
4
2/2
1.0
2*2
4
2-2
0
sqrt(4)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    sqrt(4)
NameError: name 'sqrt' is not defined
help()

Welcome to Python 3.12's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

test_sqlite3: testing with SQLite version 3.42.0

Warning (from warnings module):
  File "C:\Python\Lib\site-packages\vboxapi-1.0-py3.12.egg\vboxapi\__init__.py", line 73
SyntaxWarning: invalid escape sequence '\P'

Warning (from warnings module):
  File "C:\Python\Lib\site-packages\vboxapi-1.0-py3.12.egg\vboxapi\__init__.py", line 73
SyntaxWarning: invalid escape sequence '\P'
PyInstaller         audioop             io                  scrolledlist
__future__          autocommand         iomenu              search
__hello__           autocomplete        ipaddress           searchbase
__main__            autocomplete_w      itertools           searchengine
__phello__          autoexpand          json                secrets
_abc                backports           keras               select
_aix_support        base64              keyword             selectors
_ast                bdb                 lib2to3             setuptools
_asyncio            binascii            linecache           shelve
_bisect             bisect              locale              shlex
_blake2             browser             logging             shutil
_bz2                builtins            lzma                sidebar
_codecs             bz2                 macosx              signal
_codecs_cn          cProfile            mailbox             site
_codecs_hk          calendar            mailcap             six
_codecs_iso2022     calltip             mainmenu            smtplib
_codecs_jp          calltip_w           markdown            sndhdr
_codecs_kr          certifi             markdown_it         socket
_codecs_tw          cgi                 markupsafe          socketserver
_collections        cgitb               marshal             sqlite3
_collections_abc    charset_normalizer  math                sqlparse
_compat_pickle      chunk               mdurl               squeezer
_compression        clang               mimetypes           sre_compile
_contextvars        cmath               ml_dtypes           sre_constants
_csv                cmd                 mmap                sre_parse
_ctypes             code                modulefinder        ssl
_ctypes_test        codecontext         more_itertools      stackviewer
_datetime           codecs              mouseinfo           stat
_decimal            codeop              msilib              statistics
_distutils_hack     collections         msvcrt              statusbar
_elementtree        colorizer           multicall           string
_functools          colorsys            multiprocessing     stringprep
_hashlib            compileall          mysql               struct
_heapq              concurrent          mysqlx              subprocess
_imp                config              namex               sunau
_io                 config_key          netrc               symtable
_json               configdialog        nntplib             sys
_locale             configparser        nt                  sysconfig
_lsprof             contextlib          ntpath              tabnanny
_lzma               contextvars         nturl2path          tarfile
_markupbase         copy                numbers             telnetlib
_md5                copyreg             numpy               tempfile
_msi                corsheaders         opcode              tensorboard
_multibytecodec     crypt               operator            tensorboard_data_server
_multiprocessing    csv                 opt_einsum          tensorflow
_mysql_connector    ctypes              optparse            termcolor
_opcode             curses              optree              test
_operator           dataclasses         ordlookup           textview
_osx_support        datetime            os                  textwrap
_overlapped         dateutil            outwin              this
_pickle             dbm                 packaging           threading
_py_abc             debugger            pandas              time
_pydatetime         debugger_r          parenmatch          timeit
_pydecimal          debugobj            pasta               tkinter
_pyinstaller_hooks_contrib debugobj_r          pathbrowser         token
_pyio               decimal             pathlib             tokenize
_pylong             delegator           pdb                 tomli
_queue              difflib             pefile              tomllib
_random             dis                 percolator          tooltip
_sha1               django              peutils             trace
_sha2               doctest             pickle              traceback
_sha3               dynoption           pickletools         tracemalloc
_signal             editor              pip                 tree
_sitebuiltins       email               pipes               tty
_socket             encodings           pkg_resources       turtle
_sqlite3            ensurepip           pkgutil             turtledemo
_sre                enum                platform            typeguard
_ssl                errno               platformdirs        types
_stat               faulthandler        plistlib            typing
_statistics         filecmp             poplib              typing_extensions
_string             fileinput           posixpath           tzdata
_strptime           filelist            pprint              undo
_struct             flatbuffers         profile             unicodedata
_symtable           fnmatch             pstats              unittest
_testbuffer         format              pty                 urllib
_testcapi           fractions           py_compile          urllib3
_testclinic         ftplib              pyautogui           util
_testconsole        functools           pyclbr              uu
_testimportmultiple gast                pydoc               uuid
_testinternalcapi   gc                  pydoc_data          vboxapi
_testmultiphase     genericpath         pyexpat             vboxapisetup
_testsinglephase    getopt              pygetwindow         venv
_thread             getpass             pygments            warnings
_threading_local    gettext             pymsgbox            wave
_tkinter            glob                pymysql             weakref
_tokenize           graphlib            pynput              webbrowser
_tracemalloc        grep                pyparse             werkzeug
_typing             grpc                pyperclip           wheel
_uuid               gzip                pyrect              win32ctypes
_warnings           h5py                pyscreeze           window
_weakref            hashlib             pyshell             winreg
_weakrefset         heapq               pytweening          winsound
_winapi             help                pytz                wrapt
_wmi                help_about          query               wsgiref
_xxinterpchannels   history             queue               xdrlib
_xxsubinterpreters  hmac                quopri              xml
_zoneinfo           html                random              xmlrpc
abc                 http                re                  xxsubtype
absl                hyperparser         redirector          zipapp
aifc                idle                replace             zipfile
altgraph            idle_test           reprlib             zipimport
antigravity         idlelib             requests            zipp
argparse            idna                rich                zlib
array               imaplib             rlcompleter         zoneinfo
asgiref             imghdr              rpc                 zoomheight
ast                 importlib           run                 zzdummy
astunparse          importlib_metadata  runpy               
asyncio             inflect             runscript           
atexit              inspect             sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
import math
math.sqrt(4)
2.0
# Todo programa tendrà las siguientes secciones:
# 1) Importaciòn de mòdulos o librerìas
# 2) Declaraciòn de funciones y procedimientos
# 3) Declaraciòn de variables y estructuras de datos

======= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS/ej1_resolvente.py ======
¿Valor de a:?
======= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS/ej1_resolvente.py ======
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?0
ERROR: El valor de 'a' debe ser diferente de 0
¿Uste desea obtener la resolvente para otros valores(S/N):?s
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?1
¿Valor de b:?1
¿Valor de c:?1
ERROR: Expresiòn subradical no puede ser negativa
¿Uste desea obtener la resolvente para otros valores(S/N):?s
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?1
¿Valor de b:?4
¿Valor de c:?1
x1: -0.2679491924311228
x2:-3.732050807568877
¿Uste desea obtener la resolvente para otros valores(S/N):?n
Fin del programa
>>> 
>>> 
>>> a
1.0
>>> 
>>> 
======= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS/ej1_resolvente.py ======
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?dbfsjdfjksgv
ERROR: Debe ingresar un valor nùmerico
¿Valor de a:?7
¿Valor de a:?
Traceback (most recent call last):
  File "C:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS/ej1_resolvente.py", line 23, in <module>
    a = float(input('¿Valor de a:?'))
KeyboardInterrupt
>>> 
======= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/ORLANYS/ej1_resolvente.py ======
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?d
ERROR: Debe ingresar un valor nùmerico
¿Valor de a:?7
¿Valor de b:?f
ERROR: Debe ingresar un valor nùmerico
¿Valor de b:?5
¿Valor de c:?f
x1: 0.0
x2:-35.0
¿Usted desea obtener la resolvente para otros valores(S/N):?s
----------Soluciòn a ecuaciòn resolvente----------
¿Valor de a:?3
¿Valor de b:?15
¿Valor de c:?3
¿Valor de c:?n
x1: -1.8784093726987194
x2:-43.12159062730128
¿Usted desea obtener la resolvente para otros valores(S/N):?n
Fin del programa
