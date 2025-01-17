import psycopg2

try:
    conexion=psycopg2.connect(database='db_Prueba', user='postgres', password='adolfo2022')
    cursor01=conexion.cursor()
    cursor01.execute('select version()')
    version=cursor01.fetchone()
except Exception as err:
    print('error al ingresar',err)
    
try:
    cursor01.execute("insert into Empleos values (2044 Grado 9,'Profesional Universitario','Promover')")
except Exception as err:
    print('error al ingresar datos',err)
    
else:
    print('Datos insertados correctamente')
conexion.commit()

    
else:
    
    print(version)
    
conexion.close()