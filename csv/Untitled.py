import scipy.io as sio
import csv
a='Estaciones_UChile.mat'
archive= sio.loadmat(a)
sio.whosmat(a)
print archive
#### ACA SE NOS METEMOS EN ESTRUCTURAS 
estructura1 = archive['Estaciones_UChile']
estructura2 = estructura1['Minutos']
###archive.Dias{1, 1}.Datos_diario
### Estaciones_UChile.Minutos.Estacion_UChile_2017{1, 1}.Datos

## ACA ME METO EN LISTAS  y esas cosas
lista=estructura2[0][0][0][0][0][0][0][0][0]

##lista[0] = TIMESTAMP (Son las fechas) 
##lista[1] = RECORS    (es el numero de caption tomados)
##lista[2] = BattV_min
##lista[3] = PTemp_C_Avg
##lista[4] = Pres_mbar_Avg
##lista[5] = Temp_C_Avg
##lista[6] = Temp_C_Max
##lista[7] = Temp_C_Min
##lista[8] = RH
##lista[9] = Slr_Wm2_Avg (Esta lleno de NAN eso)
##lista[10] = total_flu_langl... (Esta lleno de NAN eso)
##lista[11] = Rain_mm_Tot
##lista[12] = WS_ms_S_WVT
##lista[13] = WindDir_d1_WVT
##lista[14] = WindDir_SD1_WVT

#### BattV_min  
nombre='BattV_Min'
with open(nombre + '.csv', 'w') as csvfile:
    fieldnames = ['Fechas', nombre ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista[0][i][0][0], nombre : lista[2][i][0]})
####
#### PTemp_C_Avg 
nombre='PTemp_C_Avg'
with open(nombre + '.csv', 'w') as csvfile:
    fieldnames = ['Fechas', nombre ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista[0][i][0][0], nombre : lista[3][i][0]})
####


########ES UN VERDADERO EJEMPLO DE COMO HACER UN .CSV ## pajeramente xd
###with open('names.csv', 'w') as csvfile:
###    fieldnames = ['first_name', 'last_name']
###    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
###
###    writer.writeheader()
###    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
###    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
###    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
