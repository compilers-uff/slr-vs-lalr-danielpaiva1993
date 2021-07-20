import ply.lex as lex
import ply.yacc as yacc

''' Gramática dada:

S -> L = R | R
L -> * R | id
R -> L

'''

tokens = ['NAME', 'EQUALS', 'TIMES']

t_ignore = r' '
t_NAME = r'id'
t_EQUALS = r'\='
t_TIMES = r'\*'

lexer = lex.lex()

def p_S(p):
    '''S : L EQUALS R 
         | R'''

def p_L(p):
    '''L : TIMES R 
         | NAME'''

def p_R(p):
    '''R : L'''

#argumento method=LALR (default) ou method=SLR para alternar entre os dois algoritmos

#yacc.yacc(method="LALR")

yacc.yacc(method="SLR")