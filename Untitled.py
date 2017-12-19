import scipy.io as sio
import csv
import time

tiempo1=time.time()
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
lista3=estructura2[0][0][0][0][1][0][0][0][0]
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
print '-------- Imprimir por minutos-----------'
nombres=['Fechas','RECORS','BattV_min','PTemp_C_Avg','Pres_mbar_Avg','Temp_C_Avg','Temp_C_Max','Temp_C_Min','RH','Slr_Wm2_Avg','Total_flu','Rain_mm_Tot','WS_ms_S_WVT','WindDir_d1_WVT','WindDir_SD1_WVT']
#### BattV_min  
for j in range(2,len(nombres)):
    nombre=  nombres[j] #str(lista2[2][j]).replace(" ", "")
    with open('./csv/minutos/'+nombre +'_minutos'+'.csv', 'w') as csvfile:
        fieldnames = ['Fechas', nombre ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(lista[0])): ## LEN de todos los datos de fechas
            writer.writerow({'Fechas': lista[0][i][0][0],  nombres[j] : str(lista[j][i][0]).replace("[u'NAN']", "0")})
            
nombre='Datos_temperatura'
with open('./csv/minutos/' + nombre +'_minutos'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', nombres[5],nombres[6],nombres[7] ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
           writer.writerow({'Fechas': lista[0][i][0][0],  nombres[5]: lista[5][i][0] ,nombres[6]: lista[6][i][0],nombres[7]: lista[7][i][0] })

print lista3
for j in range(2,len(lista3[1])):
    nombre= ((str(lista3[1][j]).replace(" ", "")).replace("u'", "")).replace("'", "") #str(lista2[2][j]).replace(" ", "")
    with open('./csv/minutos/'+nombre +'_minutos'+'.csv', 'w') as csvfile:
        fieldnames = ['Fechas', nombre ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(lista[0])): ## LEN de todos los datos de fechas
            writer.writerow({'Fechas': lista3[0][1][0][0],  nombre : str(lista3[2][i][j]).replace("[u'NAN']", "0")})
 
nombre= 'Datos_radiacion'
with open('./csv/minutos/'+nombre +'_minutos'+'.csv', 'w') as csvfile:
    fieldnames = ['Fechas', ((str(lista3[1][2]).replace(" ", "")).replace("u'", "")).replace("'", ""), ((str(lista3[1][3]).replace(" ", "")).replace("u'", "")).replace("'", ""),((str(lista3[1][4]).replace(" ", "")).replace("u'", "")).replace("'", "")  ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(lista[0])): ## LEN de todos los datos de fechas
        writer.writerow({'Fechas': lista3[0][1][0][0],  ((str(lista3[1][2]).replace(" ", "")).replace("u'", "")).replace("'", "")  : str(lista3[2][i][2]).replace("[u'NAN']", "0"), ((str(lista3[1][3]).replace(" ", "")).replace("u'", "")).replace("'", "")  : str(lista3[2][i][3]).replace("[u'NAN']", "0"),   ((str(lista3[1][4]).replace(" ", "")).replace("u'", "")).replace("'", "")  : str(lista3[2][i][4]).replace("[u'NAN']", "0"), })
 
tiempo2=time.time()
print 'Me demoro ' + str(tiempo2-tiempo1) + 'segundos'
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

tiempo3=time.time()
print 'Me demoro ' + str(tiempo3-tiempo2) + 'segundos'
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
        
tiempo4=time.time()
print 'Me demoro ' + str(tiempo4-tiempo3) + 'segundos'
