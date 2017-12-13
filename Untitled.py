import scipy.io as sio
import csv

a='Estaciones_UChile.mat'
archive= sio.loadmat(a)
sio.whosmat(a)
#### ACA SE NOS METEMOS EN ESTRUCTURAS 
estructura1 = archive['Estaciones_UChile']
estructura2 = estructura1['Minutos']
###archive.Dias{1, 1}.Datos_diario
### Estaciones_UChile.Minutos.Estacion_UChile_2017{1, 1}.Datos

## ACA ME METO EN LISTAS  y esas cosas
lista=estructura2[0][0][0][0][0][0][0][0][0]

lista3=estructura2[0][0][0][0][0][0][0][0]
print lista3
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

'''
nombre='BattV_Min'
with open(nombre + 'minutos'+ '.csv', 'w') as csvfile:
    fieldnames = ['Fechas', nombre ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista[0][i][0][0], nombre : lista[2][i][0]})
'''
####
#### PTemp_C_Avg 
'''
nombre='PTemp_C_Avg'
with open(nombre + 'minutos'+ '.csv', 'w') as csvfile:
    fieldnames = ['Fechas', nombre ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista[0][i][0][0], nombre : lista[3][i][0]})
'''
############################ #### #### #### 
'''
print '-------- Imprimir por hora-----------'
estructura3 = estructura1['Horas']
lista2 =estructura3[0][0][0][0][0][0]

for j in range(18):
    nombre= str(lista2[2][j]).replace(" ", "")
    with open('./csv/hora/'+nombre +'_hora'+'.csv', 'w') as csvfile:
        fieldnames = ['Fechas', nombre ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
            writer.writerow({'Fechas': lista2[0][i][0][0], nombre : lista2[1][i][j]})

nombre='Datos_radiacion'
with open('./csv/hora/' + nombre +'_hora'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][0]).replace(" ", ""), str(lista2[2][1]).replace(" ", ""),str(lista2[2][2]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
           writer.writerow({'Fechas': lista2[0][i][0][0], str(lista2[2][0]).replace(" ", ""):  lista2[1][i][0] , str(lista2[2][1]).replace(" ", ""):  lista2[1][i][1] ,str(lista2[2][2]).replace(" ", ""):  lista2[1][i][0]})

nombre='Datos_temperatura'
with open('./csv/hora/' + nombre +'_hora'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][4]).replace(" ", ""), str(lista2[2][5]).replace(" ", ""),str(lista2[2][6]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
           writer.writerow({'Fechas': lista2[0][i][0][0], str(lista2[2][4]).replace(" ", ""):  lista2[1][i][4] , str(lista2[2][5]).replace(" ", ""): lista2[1][i][5] ,str(lista2[2][6]).replace(" ", ""): lista2[1][i][6]})

nombre= 'Todos'
with open('./csv/hora/' + nombre +'_hora'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][0]).replace(" ", ""), str(lista2[2][1]).replace(" ", ""),str(lista2[2][2]).replace(" ", ""),str(lista2[2][3]).replace(" ", ""),str(lista2[2][4]).replace(" ", ""),str(lista2[2][5]).replace(" ", ""),str(lista2[2][6]).replace(" ", ""),str(lista2[2][7]).replace(" ", ""),str(lista2[2][8]).replace(" ", ""),str(lista2[2][9]).replace(" ", ""),str(lista2[2][10]).replace(" ", ""),str(lista2[2][11]).replace(" ", ""),str(lista2[2][12]).replace(" ", ""),str(lista2[2][13]).replace(" ", ""),str(lista2[2][14]).replace(" ", ""),str(lista2[2][15]).replace(" ", ""),str(lista2[2][16]).replace(" ", ""),str(lista2[2][17]).replace(" ", ""),str(lista2[2][18]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista2[0][i][0][0],str(lista2[2][0]).replace(" ", "") : lista2[1][i][0] ,str(lista2[2][1]).replace(" ", "") : lista2[1][i][1] ,str(lista2[2][2]).replace(" ", "") : lista2[1][i][2] ,str(lista2[2][3]).replace(" ", "") : lista2[1][i][3] ,str(lista2[2][4]).replace(" ", "") : lista2[1][i][4] ,str(lista2[2][5]).replace(" ", "") : lista2[1][i][5] ,str(lista2[2][6]).replace(" ", "") : lista2[1][i][6] ,str(lista2[2][7]).replace(" ", "") : lista2[1][i][7] ,str(lista2[2][8]).replace(" ", "") : lista2[1][i][8] ,str(lista2[2][9]).replace(" ", "") : lista2[1][i][9] ,str(lista2[2][10]).replace(" ", "") : lista2[1][i][10] ,str(lista2[2][11]).replace(" ", "") : lista2[1][i][11] ,str(lista2[2][12]).replace(" ", "") : lista2[1][i][12] ,str(lista2[2][13]).replace(" ", "") : lista2[1][i][13] ,str(lista2[2][14]).replace(" ", "") : lista2[1][i][14] ,str(lista2[2][15]).replace(" ", "") : lista2[1][i][15] ,str(lista2[2][16]).replace(" ", "") : lista2[1][i][16] ,str(lista2[2][17]).replace(" ", "") : lista2[1][i][17] ,str(lista2[2][18]).replace(" ", "")  : lista2[1][i][18]})

################ DIAS
print '-------- Imprimir por dias-----------'
estructura3 = estructura1['Dias']
lista2 =estructura3[0][0][0][0][0][0]
for j in range(18):
    nombre= str(lista2[2][j]).replace(" ", "")
    with open('./csv/dias/'+nombre +'_dias'+'.csv', 'w') as csvfile:
        fieldnames = ['Fechas', nombre ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
            writer.writerow({'Fechas': lista2[0][i][0][0], nombre : lista2[1][i][j]})

nombre='Datos_radiacion'
with open('./csv/dias/' + nombre +'_dias'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][0]).replace(" ", ""), str(lista2[2][1]).replace(" ", ""),str(lista2[2][2]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
           writer.writerow({'Fechas': lista2[0][i][0][0], str(lista2[2][0]).replace(" ", ""):  lista2[1][i][0] , str(lista2[2][1]).replace(" ", ""):  lista2[1][i][1] ,str(lista2[2][2]).replace(" ", ""):  lista2[1][i][0]})

nombre='Datos_temperatura'
with open('./csv/dias/' + nombre +'_dias'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][4]).replace(" ", ""), str(lista2[2][5]).replace(" ", ""),str(lista2[2][6]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
           writer.writerow({'Fechas': lista2[0][i][0][0], str(lista2[2][4]).replace(" ", ""):  lista2[1][i][4] , str(lista2[2][5]).replace(" ", ""): lista2[1][i][5] ,str(lista2[2][6]).replace(" ", ""): lista2[1][i][6]})

nombre= 'Todos'
with open('./csv/dias/' + nombre +'_dias'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', str(lista2[2][0]).replace(" ", ""), str(lista2[2][1]).replace(" ", ""),str(lista2[2][2]).replace(" ", ""),str(lista2[2][3]).replace(" ", ""),str(lista2[2][4]).replace(" ", ""),str(lista2[2][5]).replace(" ", ""),str(lista2[2][6]).replace(" ", ""),str(lista2[2][7]).replace(" ", ""),str(lista2[2][8]).replace(" ", ""),str(lista2[2][9]).replace(" ", ""),str(lista2[2][10]).replace(" ", ""),str(lista2[2][11]).replace(" ", ""),str(lista2[2][12]).replace(" ", ""),str(lista2[2][13]).replace(" ", ""),str(lista2[2][14]).replace(" ", ""),str(lista2[2][15]).replace(" ", ""),str(lista2[2][16]).replace(" ", ""),str(lista2[2][17]).replace(" ", ""),str(lista2[2][18]).replace(" ", "")]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista2[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista2[0][i][0][0],str(lista2[2][0]).replace(" ", "") : lista2[1][i][0] ,str(lista2[2][1]).replace(" ", "") : lista2[1][i][1] ,str(lista2[2][2]).replace(" ", "") : lista2[1][i][2] ,str(lista2[2][3]).replace(" ", "") : lista2[1][i][3] ,str(lista2[2][4]).replace(" ", "") : lista2[1][i][4] ,str(lista2[2][5]).replace(" ", "") : lista2[1][i][5] ,str(lista2[2][6]).replace(" ", "") : lista2[1][i][6] ,str(lista2[2][7]).replace(" ", "") : lista2[1][i][7] ,str(lista2[2][8]).replace(" ", "") : lista2[1][i][8] ,str(lista2[2][9]).replace(" ", "") : lista2[1][i][9] ,str(lista2[2][10]).replace(" ", "") : lista2[1][i][10] ,str(lista2[2][11]).replace(" ", "") : lista2[1][i][11] ,str(lista2[2][12]).replace(" ", "") : lista2[1][i][12] ,str(lista2[2][13]).replace(" ", "") : lista2[1][i][13] ,str(lista2[2][14]).replace(" ", "") : lista2[1][i][14] ,str(lista2[2][15]).replace(" ", "") : lista2[1][i][15] ,str(lista2[2][16]).replace(" ", "") : lista2[1][i][16] ,str(lista2[2][17]).replace(" ", "") : lista2[1][i][17] ,str(lista2[2][18]).replace(" ", "")  : lista2[1][i][18]})


'''
