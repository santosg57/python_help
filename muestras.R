pob = c('A', 'C', 'G', 'T')
nmuestras = 1000

muestra = sample(pob, nmuestras, replace=TRUE)

print(muestra)

x=paste(muestra, collapse="")

print(x)

