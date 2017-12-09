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



with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
with open('intento1.csv', 'w') as csvfile:
    writer2 = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer2.writerows(estructura2)
