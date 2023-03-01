teste =list()
teste.append('arthur')
teste.append(20)
galera=list()
galera.append(teste[:])#Copia[:] devido a junçao de listas
teste[0]= 'isa'
teste[1]= 22
galera.append((teste[:]))
print (galera)
