Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i = 0
type(i)
<class 'int'>
while i < 5:
    print(i)
    i = i+1 #es equivlente a i+1 sobrecarga de operador

    
0
1
2
3
4

i = 0
for i in range(5):
    print(i)

    
0
1
2
3
4
i = 0
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, 'x', j, '=', i+j)
        j += 1
        i += 1
        print('')

        
1 x 1 = 2

2 x 2 = 4

3 x 3 = 6

4 x 4 = 8

5 x 5 = 10

6 x 6 = 12

7 x 7 = 14

8 x 8 = 16

9 x 9 = 18

while i < 10:
    j = 1
    while j < 10:
        print(i, 'x', j, '=', i+j)
        j += 1
    i += 1
    print('')

    
i
10
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, 'x', j, '=', i+j)
        j += 1
    i += 1
    print('')

    
1 x 1 = 2
1 x 2 = 3
1 x 3 = 4
1 x 4 = 5
1 x 5 = 6
1 x 6 = 7
1 x 7 = 8
1 x 8 = 9
1 x 9 = 10

2 x 1 = 3
2 x 2 = 4
2 x 3 = 5
2 x 4 = 6
2 x 5 = 7
2 x 6 = 8
2 x 7 = 9
2 x 8 = 10
2 x 9 = 11

3 x 1 = 4
3 x 2 = 5
3 x 3 = 6
3 x 4 = 7
3 x 5 = 8
3 x 6 = 9
3 x 7 = 10
3 x 8 = 11
3 x 9 = 12

4 x 1 = 5
4 x 2 = 6
4 x 3 = 7
4 x 4 = 8
4 x 5 = 9
4 x 6 = 10
4 x 7 = 11
4 x 8 = 12
4 x 9 = 13

5 x 1 = 6
5 x 2 = 7
5 x 3 = 8
5 x 4 = 9
5 x 5 = 10
5 x 6 = 11
5 x 7 = 12
5 x 8 = 13
5 x 9 = 14

6 x 1 = 7
6 x 2 = 8
6 x 3 = 9
6 x 4 = 10
6 x 5 = 11
6 x 6 = 12
6 x 7 = 13
6 x 8 = 14
6 x 9 = 15

7 x 1 = 8
7 x 2 = 9
7 x 3 = 10
7 x 4 = 11
7 x 5 = 12
7 x 6 = 13
7 x 7 = 14
7 x 8 = 15
7 x 9 = 16

8 x 1 = 9
8 x 2 = 10
8 x 3 = 11
8 x 4 = 12
8 x 5 = 13
8 x 6 = 14
8 x 7 = 15
8 x 8 = 16
8 x 9 = 17

9 x 1 = 10
9 x 2 = 11
9 x 3 = 12
9 x 4 = 13
9 x 5 = 14
9 x 6 = 15
9 x 7 = 16
9 x 8 = 17
9 x 9 = 18

#ciclo anidado para producir la tabla de multiplicar
i = 1
for i in range (1,9)
SyntaxError: incomplete input
i = 1
for i in range (1,10):
    j = 1
    for j in range (1,10):
        print (i, ' x ', j, ' = ', i*j)

        
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
#ciclo condicionado
continuar = 'S'
while continuar == 'S':
    print('Acciones en ejecucion...')
    continuar = input('usted desea continuar (S/N):')
    continuar.upper()
    print("usted eligio continuar...")

    
Acciones en ejecucion...
usted desea continuar (S/N):s
'S'
usted eligio continuar...
while continuar == 'S':
    print('Acciones en ejecucion...')
    continuar = input('usted desea continuar (S/N):')
    continuar = continuar.upper()
    print("usted eligio continuar...")

    
continuar = 'S'

while continuar == 'S':
    print('Acciones en ejecucion...')
    continuar = input('usted desea continuar (S/N):')
    continuar = continuar.upper()
    print("usted eligio continuar...")

    
Acciones en ejecucion...
usted desea continuar (S/N):S
usted eligio continuar...
Acciones en ejecucion...
usted desea continuar (S/N):S
usted eligio continuar...
Acciones en ejecucion...
usted desea continuar (S/N):N
usted eligio continuar...

while True:
    print('acciones en ejecucion')
    continuar = input('continuar S/N:')
    if continuar.upper() == 'S':
        print('continuan las acciones en ejecucion')
        continue
    else:
        print('se detienen las acciones. fin de ciclo')
        break

    
acciones en ejecucion
continuar S/N:S
continuan las acciones en ejecucion
acciones en ejecucion
continuar S/N:N
se detienen las acciones. fin de ciclo
# SOLUCION A LA ECUACION RESOLVENTE
2+2
4
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
PyInstaller         audioop             inflect             runscript
__future__          autocommand         inspect             sched
__hello__           autocomplete        io                  scrolledlist
__main__            autocomplete_w      iomenu              search
__phello__          autoexpand          ipaddress           searchbase
_abc                backports           itertools           searchengine
_aix_support        base64              json                secrets
_ast                bdb                 keras               select
_asyncio            binascii            keyword             selectors
_bisect             bisect              lib2to3             setuptools
_blake2             browser             linecache           shelve
_bz2                builtins            locale              shlex
_codecs             bz2                 logging             shutil
_codecs_cn          cProfile            lzma                sidebar
_codecs_hk          calendar            macosx              signal
_codecs_iso2022     calltip             mailbox             site
_codecs_jp          calltip_w           mailcap             six
_codecs_kr          certifi             mainmenu            smtplib
_codecs_tw          cgi                 markdown            sndhdr
_collections        cgitb               markdown_it         socket
_collections_abc    charset_normalizer  markupsafe          socketserver
_compat_pickle      chunk               marshal             sqlite3
_compression        clang               math                sqlparse
_contextvars        cmath               mdurl               squeezer
_csv                cmd                 mimetypes           sre_compile
_ctypes             code                ml_dtypes           sre_constants
_ctypes_test        codecontext         mmap                sre_parse
_datetime           codecs              modulefinder        ssl
_decimal            codeop              more_itertools      stackviewer
_distutils_hack     collections         mouseinfo           stat
_elementtree        colorizer           msilib              statistics
_functools          colorsys            msvcrt              statusbar
_hashlib            compileall          multicall           string
_heapq              concurrent          multiprocessing     stringprep
_imp                config              mysql               struct
_io                 config_key          mysqlx              subprocess
_json               configdialog        namex               sunau
_locale             configparser        netrc               symtable
_lsprof             contextlib          nntplib             sys
_lzma               contextvars         nt                  sysconfig
_markupbase         copy                ntpath              tabnanny
_md5                copyreg             nturl2path          tarfile
_msi                corsheaders         numbers             telnetlib
_multibytecodec     crypt               numpy               tempfile
_multiprocessing    csv                 opcode              tensorboard
_mysql_connector    ctypes              operator            tensorboard_data_server
_opcode             curses              opt_einsum          tensorflow
_operator           dataclasses         optparse            termcolor
_osx_support        datetime            optree              test
_overlapped         dateutil            ordlookup           textview
_pickle             dbm                 os                  textwrap
_py_abc             debugger            outwin              this
_pydatetime         debugger_r          packaging           threading
_pydecimal          debugobj            pandas              time
_pyinstaller_hooks_contrib debugobj_r          parenmatch          timeit
_pyio               decimal             pasta               tkinter
_pylong             delegator           pathbrowser         token
_queue              difflib             pathlib             tokenize
_random             dis                 pdb                 tomli
_sha1               distlib             pefile              tomllib
_sha2               django              percolator          tooltip
_sha3               doctest             peutils             trace
_signal             dynoption           pickle              traceback
_sitebuiltins       editor              pickletools         tracemalloc
_socket             email               pip                 tree
_sqlite3            encodings           pipes               tty
_sre                ensurepip           pkg_resources       turtle
_ssl                enum                pkgutil             turtledemo
_stat               errno               platform            typeguard
_statistics         faulthandler        platformdirs        types
_string             filecmp             plistlib            typing
_strptime           fileinput           poplib              typing_extensions
_struct             filelist            posixpath           tzdata
_symtable           filelock            pprint              undo
_testbuffer         flatbuffers         profile             unicodedata
_testcapi           fnmatch             pstats              unittest
_testclinic         format              pty                 urllib
_testconsole        fractions           py_compile          urllib3
_testimportmultiple ftplib              pyautogui           util
_testinternalcapi   functools           pyclbr              uu
_testmultiphase     gast                pydoc               uuid
_testsinglephase    gc                  pydoc_data          vboxapi
_thread             genericpath         pyexpat             vboxapisetup
_threading_local    getopt              pygetwindow         venv
_tkinter            getpass             pygments            virtualenv
_tokenize           gettext             pymsgbox            warnings
_tracemalloc        glob                pymysql             wave
_typing             graphlib            pynput              weakref
_uuid               grep                pyparse             webbrowser
_warnings           grpc                pyperclip           werkzeug
_weakref            gzip                pyrect              wheel
_weakrefset         h5py                pyscreeze           win32ctypes
_winapi             hashlib             pyshell             window
_wmi                heapq               pytweening          winreg
_xxinterpchannels   help                pytz                winsound
_xxsubinterpreters  help_about          query               wrapt
_zoneinfo           history             queue               wsgiref
abc                 hmac                quopri              xdrlib
absl                html                random              xml
aifc                http                re                  xmlrpc
altgraph            hyperparser         redirector          xxsubtype
antigravity         idle                replace             zipapp
argparse            idle_test           reprlib             zipfile
array               idlelib             requests            zipimport
asgiref             idna                rich                zipp
ast                 imaplib             rlcompleter         zlib
astunparse          imghdr              rpc                 zoneinfo
asyncio             importlib           run                 zoomheight
atexit              importlib_metadata  runpy               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
import math
math.sqrt(4)
2.0
# todo programa tendra las siguientes secciones
# 1 importacion de modulos o librerias
# declaracion de funciones y procedimientos
# declaracion de variables
# declaracion de variables
#estructura de datos
# cuerpo principal de programas


========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
valor de a:
========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
----------solucion a ecuacion resolvente----------
valor de a:1
valor de b:1
valor de c:1
error: expresion subradical no puede ser negativa
usted desea obtener la resolvente para otros valores (S/N):s
----------solucion a ecuacion resolvente----------
valor de a:1
valor de b:4
valor de c:1
x1: -0.2679491924311228
usted desea obtener la resolvente para otros valores (S/N):n
Fin del programa

========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
----------solucion a ecuacion resolvente----------
valor de a:3
valor de b:4
valor de c:5
error: expresion subradical no puede ser negativa
usted desea obtener la resolvente para otros valores (S/N):s
----------solucion a ecuacion resolvente----------
valor de a:1
valor de b:3
valor de c:2
x1: -1.0
x2: -2.0
usted desea obtener la resolvente para otros valores (S/N):s
----------solucion a ecuacion resolvente----------
valor de a:6
valor de b:7
valor de c:1
x1: -6.0
x2: -36.0
usted desea obtener la resolvente para otros valores (S/N):
========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
----------solucion a ecuacion resolvente----------
valor de a:a
Traceback (most recent call last):
  File "C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py", line 22, in <module>
    a = float(input('valor de a:'))
ValueError: could not convert string to float: 'a'
>>> 
========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
----------solucion a ecuacion resolvente----------
valor de a:d
error:debe ingresar un valor numerico
valor de a:7
valor de a:
Traceback (most recent call last):
  File "C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py", line 24, in <module>
    a = float(input('valor de a:'))
KeyboardInterrupt

========================= RESTART: C:/ESP_PYTHON_20250331/NIVEL_I/DANNYSA/ej1_resolvente.py =========================
----------solucion a ecuacion resolvente----------
valor de a:7
valor de b:e
error:debe ingresar un valor numerico
valor de b:9
valor de c:e
error:debe ingresar un valor numerico
valor de c:3
error: expresion subradical no puede ser negativa
usted desea obtener la resolvente para otros valores (S/N):s
----------solucion a ecuacion resolvente----------
valor de a:3
valor de b:15
valor de c:3
x1: -1.8784093726987194
x2: -43.12159062730128
usted desea obtener la resolvente para otros valores (S/N):n
Fin del programa
