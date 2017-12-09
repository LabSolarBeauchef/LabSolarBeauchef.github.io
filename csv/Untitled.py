import scipy.io as sio
import csv
a='Estaciones_UChile.mat'
archive= sio.loadmat(a)
sio.whosmat(a)
print archive

print '----------------------1'
print '----------------------1'
print '----------------------1'
print '----------------------1'

estructura1 = archive['Estaciones_UChile']
print estructura1
print '----------------------2'
print '----------------------2'
print '----------------------2'
print '----------------------2'


estructura2 = estructura1['Minutos']
print estructura2
###archive.Dias{1, 1}.Datos_diario
### Estaciones_UChile.Minutos.Estacion_UChile_2017{1, 1}.Datos

print '----------------------3'
print '----------------------3'
print '----------------------3'
print '----------------------3'
print estructura2[0][0][0][0][0][0][0][0][0][0][0]
b=estructura2[0][0][0][0][0][0][0][0][0][0]


lista=estructura2[0][0][0][0][0][0][0][0][0][0]

with open('names.csv', 'w') as csvfile:
    fieldnames = ['fechas', 'porotos negros']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista)):
        writer.writerow({'fechas': lista[i][0][0], 'porotos negros': 'BlackBeans'})

###with open('some.csv', 'wb') as f:
##    writer = csv.writer(f)
##    writer.writerows(b)
##    writer.writerows(b)


########ES UN VERDADERO EJEMPLO DE COMO HACER UN .CSV ## pajeramente xd
###with open('names.csv', 'w') as csvfile:
###    fieldnames = ['first_name', 'last_name']
###    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
###
###    writer.writeheader()
###    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
###    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
###    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
