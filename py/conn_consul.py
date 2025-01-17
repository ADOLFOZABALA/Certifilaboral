import psycopg2

try:
    conexion=psycopg2.connect(database='db_Prueba', user='postgres', password='adolfo2022')
    cursor01=conexion.cursor()
    cursor01.execute('select version()')
    version=cursor01.fetchone()
    
except Exception as err:
    print('error al ingresar',err)
    
else:
    
    print(version)
    
cursor01.execute('select *from empleos')
consulta=cursor01.fetchone()
print(consulta)    
    
conexion.close()