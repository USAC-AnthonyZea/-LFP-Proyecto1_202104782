from numero import Numero # Clase numero, para obtener un objeto Numero
from aritmeticas import Aritmeticas # Clase aritmeticas, para obtener un objeto Aritmeticas
from operador import Operador # Clase para operadores como: Mas, Menos, mayor, igual, etc...
from errores import Errores

# Nombre de los tokens
tokens = (
    'RTIPO',
    'ROPERACION',
    'RNUMERO',
    'RSUMA',
    'RRESTA',
    'RMULTIPLICACION',
    'RDIVISION',
    'RRAIZ',
    'RPOTENCIA',
    'RMOD',
    'RINVERSO',
    'LLAA',
    'LLAC',
    'IGUAL',
    'DIV',
    'ENTERO',
    'DECIMAL',
)

# Aqui se dan los valores de cada token
# En este caso decimos el valor que va a contener cada token osea, el lexema

t_RTIPO       = r'Tipo'
t_ROPERACION  = r'Operacion'
t_RSUMA       = r'SUMA'
t_RRESTA       = r'RESTA'
t_RMULTIPLICACION = r'MULTIPLICACION'
t_RDIVISION = r'DIVISION'
t_RRAIZ = r'RAIZ'
t_RPOTENCIA = r'POTENCIA'
t_RMOD = r'MOD'
t_RINVERSO = r'INVERSO'
t_RNUMERO     = r'Numero'
t_LLAA        = r'<'
t_LLAC        = r'>'
t_IGUAL       = r'='
t_DIV         = r'/'

# Gramática para números con punto decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

# Gramática para números enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Esta esa para poder aceptar cadenas de texto, lo vamos a usar más adelante
# def t_CADENA(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     return t

# Esta función cuando lee un salto de línea lo agrega al analizador para 
# Saber en qué linea se encuentra
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Caracteres ignorados en este caso los espacios y las tabulaciones
t_ignore = " \t"

# Este es un error léxico, pueden irlos almacenando en un array para obtenerlos después
def t_error(t):

    error = Errores(t.value[0],'Error Lexico', t.lineno, find_column(input,t))
    errores_.append(error)
    t.lexer.skip(1)

# Contruccion del analizador lexico
import ply.lex as lex
lexer = lex.lex()

# ------ DE AQUI EN ADELANTE EMPIEZA EL ANALIZADOR SINTACTICO ------
# Pueden guiarse con esto que les dejé, ya solo es de 
# agregar las demás operaciones que hagan falta y agregarlas en el archivo aritmeticas.py

# ANALIZADOR SINTACTICO
# Definicion de la gramatica

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        |   instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    'instruccion  : LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC'
    t[0] = t[4]

def p_instrucciones_2_lista(t):
    'instrucciones_2 : instrucciones_2 instruccion_2'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2_instruccion(t):
    'instrucciones_2 :  instruccion_2'
    t[0] = [t[1]]

def p_instruccion_2(t):
    'instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC'
    t[0] = Aritmeticas(t[6][0], t[6][1], t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_decimal(t):
    'instruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC '
    t[0] = Numero(float(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_entero(t):
    'instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC '
    t[0] = Numero(int(t[4]), t.lineno(1), find_column(input,t.slice[1]))

# def p_var(t):
#     '''var  : RTIPO
#             | RTEXTO
#     '''
#     print('Entramos en p_var() con: ', t[1])
#     t[0] = t[1]

def p_tipo(t):
    '''tipo :   RSUMA
            |   RRESTA
            |   RMULTIPLICACION
            |   RDIVISION
            |   RRAIZ
            |   RPOTENCIA
            |   RMOD
            |   RINVERSO
    '''

    if t[1] == 'SUMA':
        t[0] = Operador.SUMA

    elif t[1] == 'RESTA':
        t[0] = Operador.RESTA

    elif t[1] == 'MULTIPLICACION':
        t[0] = Operador.MULTIPLICACION

    elif t[1] == 'DIVISION':
        t[0] = Operador.DIVISION

    elif t[1] == 'RAIZ':
        t[0] = Operador.RAIZ

    elif t[1] == 'POTENCIA':
        t[0] = Operador.POTENCIA

    elif t[1] == 'MOD':
        t[0] = Operador.MOD

    elif t[1] == 'INVERSO':
        t[0] = Operador.INVERSO
    
# Aqui reconoce un error de sintaxis, pueden crear un array e irlos agregando
# para obtenerlos después
def p_error(t):
    print("Error de sintaxis en '%s'" % t.value)

# Esta función busca la columna en la que se encuentra el token o lexema
def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    lexer.lineno = 1
    return parser.parse(input)

f = open('analizador.txt', 'r')

errores_ = []

input = f.read()
f.close()
variable = parse(input)

getERFalse = False #Para obtener el resultado
getERTrue = True # Para obtener la expresion regular
n = 1

print()
for var in variable:
    for var_ in var:
        print(f"Operacion {n}:")
        print(str(var_.ejecutar(getERTrue))+" = " + str(var_.ejecutar(getERFalse)))
        print()
        n+=1

#Errores
print("Errores\n")
for var in errores_:
    print(var.toString())
    print()