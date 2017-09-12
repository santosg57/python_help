# -*- coding: utf-8 -*-

import sys
import scipy 
print 'Número de parámetros: ', len(sys.argv)
print 'Lista de argumentos: ', sys.argv
ff = sys.argv[1]
print ff
var = 'scipy.' + ff
print var

print help(var)




