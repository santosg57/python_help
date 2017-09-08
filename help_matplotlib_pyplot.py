# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot

print 'Número de parámetros: ', len(sys.argv)
print 'Lista de argumentos: ', sys.argv
ff = sys.argv[1]
print ff
var = 'matplotlib.pyplot.' + ff
print var

print help(var)




