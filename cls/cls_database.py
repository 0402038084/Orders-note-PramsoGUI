import sqlite3

class comunication_pramso_database():
    def __init__(self):
        self.conexion = sqlite3.connect('dbpramso.db')


    ####################### NOTA DE PEDIDOS #######################
    #<------------Metodo para cargar tabla de nota de pedidos------------>
    def mostrar_order_note(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  ORDER_NOTE'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #<------------Metodo para cargar tabla de nota de pedidos con busqueda------------>
    def search_ol(self, CLIENTE, TRACTOR, COSECHADORA, PLATAFORMA_S, PLATAFORMA_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, ESTADO): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM ORDER_NOTE WHERE CLIENTE LIKE "%{}%" AND TRACTOR LIKE "%{}%" AND COSECHADORA LIKE "%{}%" AND PLATAFORMA_SOJERA LIKE "%{}%" AND PLATAFORMA_MAICERA LIKE "%{}%" AND CHASISEMBOCADOR LIKE "%{}%" AND RODADO LIKE "%{}%" AND OBSERVACIONES LIKE "%{}%" AND LOCALIDAD LIKE "%{}%" AND PROVINCIA LIKE "%{}%" AND ESTADO LIKE "%{}%"'.format(CLIENTE, TRACTOR, COSECHADORA, PLATAFORMA_S, PLATAFORMA_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, ESTADO)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

   #<------------Metodo para cargar tabla de nota de pedidos------------>
    def search_id(self, ID_P):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  ORDER_NOTE WHERE ID_PEDIDO = {}'.format(ID_P)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro


    #Guardar nueva fila de la order list
    def guardar_nueva_fila_ol(self, list_save):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO ORDER_NOTE(CLIENTE, FECHA, TRACTOR, ID_T, COSECHADORA, ID_C, PLATAFORMA_SOJERA, ID_PL_S, PLATAFORMA_MAICERA, ID_PL_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, FECHADEENTREGA, ESTADO) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save [12],list_save[13], list_save[14], list_save[15], list_save[16])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #Editar fila de la order list
    def editar_fila_ol(self, list_save):
        cursor = self.conexion.cursor()
        bd = 'UPDATE ORDER_NOTE SET CLIENTE="{}", TRACTOR="{}", ID_T="{}", COSECHADORA="{}", ID_C="{}", PLATAFORMA_SOJERA="{}", ID_PL_S="{}", PLATAFORMA_MAICERA="{}", ID_PL_M="{}", CHASISEMBOCADOR="{}", OBSERVACIONES="{}", RODADO="{}", LOCALIDAD="{}", PROVINCIA="{}", FECHADEENTREGA="{}", ESTADO="{}" WHERE ID_PEDIDO = {}'.format(list_save[0], list_save[1], list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save [12], list_save[13], list_save[14], list_save[15], list_save[16])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
        
    #Eliminar fila de la order list
    def eliminar_fila_ol(self, id):
        cursor = self.conexion.cursor()
        bd = 'DELETE FROM ORDER_NOTE WHERE ID_PEDIDO = {}'.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    ####################### IMPRESION DE CONTROL DE ENTREGA #######################
    def control_entrega_tractor(self, id):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  TRACTOR_MODELS JOIN TRACTOR_EQUIPMENTS ON TRACTOR_MODELS.ID_T = TRACTOR_EQUIPMENTS.ID_T WHERE TRACTOR_EQUIPMENTS.ID_T = "{}"'.format(id)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro


    def control_entrega_cosechadora(self, id):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  COMBINEHARVESTER_MODELS JOIN COMBINEHARVESTER_EQUIPMENTS ON COMBINEHARVESTER_MODELS.ID_C = COMBINEHARVESTER_EQUIPMENTS.ID_C WHERE COMBINEHARVESTER_EQUIPMENTS.ID_C = "{}"'.format(id)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro        

    def control_entrega_sojero(self, id):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE PLATFORM_EQUIPMENTS.ID_PL = "{}"'.format(id)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    def control_entrega_maicero(self, id):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE PLATFORM_EQUIPMENTS.ID_PL = "{}"'.format(id)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro                



    ####################### REGISTRO DE EQUIPOS #######################

    #<------------Metodo para cargar tabla de registro de equipos------------>

    #Mostrar la tabla de tractores 
    def mostrar_tractor_register(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  TRACTOR_MODELS JOIN TRACTOR_EQUIPMENTS ON TRACTOR_MODELS.ID_T = TRACTOR_EQUIPMENTS.ID_T'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #Mostrar la tabla de las cosechadoras
    def mostrar_cosechadora_register(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  COMBINEHARVESTER_MODELS JOIN COMBINEHARVESTER_EQUIPMENTS ON COMBINEHARVESTER_MODELS.ID_C = COMBINEHARVESTER_EQUIPMENTS.ID_C'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro        

    
    #Mostrar la tabla de plataforma
    def mostrar_plataforma_register(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro    


    #Mostrar la tabla de plataforma sojera
    def mostrar_plataforma_sojera(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE TIPODEPLATAFORMA = "SOJERO"'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro    


    #Mostrar la tabla de plataforma maicera
    def mostrar_plataforma_maicera(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE TIPODEPLATAFORMA = "MAICERO"'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro    



    #<------------Metodo para cargar tabla de registro con busqueda------------>

    #Mostrar la tabla de tractores con la busqueda
    def buscar_tractor_register(self, modelo_tractor):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  TRACTOR_MODELS JOIN TRACTOR_EQUIPMENTS ON TRACTOR_MODELS .ID_T = TRACTOR_EQUIPMENTS.ID_T WHERE MODELO LIKE "%{}%"'.format(modelo_tractor)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #Mostrar la tabla de cosechadora con la busqueda
    def buscar_cosechadora_register(self, modelo_cosechadora):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  COMBINEHARVESTER_MODELS JOIN COMBINEHARVESTER_EQUIPMENTS ON COMBINEHARVESTER_MODELS.ID_C = COMBINEHARVESTER_EQUIPMENTS.ID_C WHERE MODELO LIKE "%{}%"'.format(modelo_cosechadora)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #Mostrar la tabla de plataforma con la busqueda
    def buscar_plataforma_register(self, modelo_plataforma):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE MODELO LIKE "%{}%"'.format(modelo_plataforma)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro



    #<------------Metodos para new register------------>

    def comprobar_ID(self, ID, machinary):
        cursor = self.conexion.cursor()
        if machinary == "tractor":
            bd = 'SELECT ID_T FROM TRACTOR_MODELS WHERE ID_T = "{}"'.format(ID)
        elif machinary == "cosechadora":
            bd = 'SELECT ID_C FROM COMBINEHARVESTER_MODELS WHERE ID_C = "{}"'.format(ID)
        elif machinary == "plataforma":
            bd = 'SELECT ID_PL FROM PLATFORM_MODELS WHERE ID_PL = "{}"'.format(ID)


        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #Ingresar nuevo Tractor
    def new_tractor (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO TRACTOR_MODELS(ID_T, MARCA, MODELO) VALUES("{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'INSERT INTO TRACTOR_EQUIPMENTS(ID_T, BASES, ADAPTADORES, COGOTE, FRENTE, BRAZOS, PLACAPORTABRAZOS, PORTAROLO, ROLO, CILINDROS, TOPES, MANGUERAS, BANDERAS, RIENDAS, BULONES58, BULONES78, BULONES20mm, BULONES916, GRAMPAS, RESORTES, CALCOS, KITHIDRAULICO, KITDETRANSFERENCIA, TEFLON, PRECINTOS) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[15], list_save[16], list_save[17], list_save[18], list_save[19], list_save[20], list_save[21], list_save[22], list_save[23], list_save[24], list_save[25], list_save[26])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #Ingresar nueva cosechadora
    def new_cosechadora (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO COMBINEHARVESTER_MODELS(ID_C, MARCA, MODELO) VALUES("{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'INSERT INTO COMBINEHARVESTER_EQUIPMENTS(ID_C, BASES, PLACAPORTACADENA, GRAMPASCADENA, FRENTE, BRAZOS, PLACAPORTABRAZOS, PORTAROLO, ROLO, BULONES58, BULONES78, BULONES20mm, BULONES916, BULONES12, GRAMPAS, RESORTES, CALCOS) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[15], list_save[16], list_save[17], list_save[18])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #Ingresar nueva plataforma
    def new_plataforma (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO PLATFORM_MODELS(ID_PL, MARCA, MODELO, TIPODEPLATAFORMA) VALUES("{}", "{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2], list_save[3])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'INSERT INTO PLATFORM_EQUIPMENTS(ID_PL, BASES, BRAZOS, PORTAROLO, ROLO, BULONES58, BULONES12, BULONES20mm, BULONES916,  GRAMPAS, RESORTES, CALCOS, ADAPTADORES) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[15])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #Editar Tractor
    def edit_tractor (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'UPDATE TRACTOR_MODELS SET MODELO="{}" WHERE ID_T="{}"'.format(list_save[0], list_save[1])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'UPDATE TRACTOR_EQUIPMENTS SET BASES="{}", ADAPTADORES="{}", COGOTE="{}",  FRENTE="{}",  BRAZOS="{}",  PLACAPORTABRAZOS="{}",  PORTAROLO="{}",  ROLO="{}",  CILINDROS="{}",  TOPES="{}",  MANGUERAS="{}",  BANDERAS="{}",  RIENDAS="{}",  BULONES58="{}",  BULONES78="{}",  BULONES20mm="{}",  BULONES916="{}",  GRAMPAS="{}",  RESORTES="{}",  CALCOS="{}",  KITHIDRAULICO="{}",  KITDETRANSFERENCIA="{}",  TEFLON="{}",  PRECINTOS="{}" WHERE ID_T="{}"'.format(list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[15], list_save[16], list_save[17], list_save[18], list_save[19], list_save[20], list_save[21], list_save[22], list_save[23], list_save[24], list_save[25], list_save[0])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
    
    
    #Editar cosechadora
    def edit_cosechadora (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'UPDATE COMBINEHARVESTER_MODELS SET MODELO="{}" WHERE ID_C="{}"'.format(list_save[0], list_save[1])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'UPDATE COMBINEHARVESTER_EQUIPMENTS SET BASES="{}", PLACAPORTACADENA="{}", GRAMPASCADENA="{}", FRENTE="{}",  BRAZOS="{}",  PLACAPORTABRAZOS="{}",  PORTAROLO="{}",  ROLO="{}", BULONES58="{}",  BULONES78="{}",  BULONES20mm="{}",  BULONES916="{}", BULONES12="{}",  GRAMPAS="{}",  RESORTES="{}",  CALCOS="{}" WHERE ID_C="{}"'.format(list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[15], list_save[16], list_save[17], list_save[0])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
    #Editar plataforma
    def edit_plataforma (self, list_save):
        cursor = self.conexion.cursor()
        bd = 'UPDATE PLATFORM_MODELS SET MODELO="{}" WHERE ID_PL="{}"'.format(list_save[0], list_save[1])
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'UPDATE PLATFORM_EQUIPMENTS SET BASES="{}", BRAZOS="{}",  PORTAROLO="{}",  ROLO="{}", BULONES58="{}",  BULONES12="{}",  BULONES20mm="{}",  BULONES916="{}",  GRAMPAS="{}",  RESORTES="{}",  CALCOS="{}", ADAPTADORES="{}" WHERE ID_PL="{}"'.format(list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save[12], list_save[13], list_save[14], list_save[0])
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #eliminar tractor
    def eliminar_fila_tractor(self, id):
        cursor = self.conexion.cursor()
        bd = 'DELETE FROM TRACTOR_EQUIPMENTS WHERE ID_T = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'DELETE FROM TRACTOR_MODELS WHERE ID_T = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
    #eliminar cosechadora
    def eliminar_fila_cosechadora(self, id):
        cursor = self.conexion.cursor()
        bd = 'DELETE FROM COMBINEHARVESTER_EQUIPMENTS WHERE ID_C = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'DELETE FROM COMBINEHARVESTER_MODELS WHERE ID_C = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    #eliminar plataforma
    def eliminar_fila_plataforma(self, id):
        cursor = self.conexion.cursor()
        bd = 'DELETE FROM PLATFORM_EQUIPMENTS WHERE ID_PL = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        bd = 'DELETE FROM PLATFORM_MODELS WHERE ID_PL = "{}" '.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()




    #<------------Metodos para edit register------------>

    #carga la tabla de tractor para seleccionar modelo
    def load_tabletractor_upgrade(self, ID, Marca, Modelo): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  TRACTOR_MODELS JOIN TRACTOR_EQUIPMENTS ON TRACTOR_MODELS.ID_T = TRACTOR_EQUIPMENTS.ID_T WHERE TRACTOR_MODELS.ID_T LIKE "%{}%" AND MARCA LIKE "%{}%" AND MODELO LIKE "%{}%"'.format(ID, Marca, Modelo)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #carga la tabla de cosechadora para seleccionar modelo
    def load_tablecosechadora_upgrade(self, ID, Marca, Modelo): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  COMBINEHARVESTER_MODELS JOIN COMBINEHARVESTER_EQUIPMENTS ON COMBINEHARVESTER_MODELS.ID_C = COMBINEHARVESTER_EQUIPMENTS.ID_C WHERE COMBINEHARVESTER_MODELS.ID_C LIKE "%{}%" AND MARCA LIKE "%{}%" AND MODELO LIKE "%{}%"'.format(ID, Marca, Modelo)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro


    #carga la tabla de plataforma para seleccionar modelo
    def load_tableplataforma_upgrade(self, ID, Marca, Modelo): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE PLATFORM_MODELS.ID_PL LIKE "%{}%" AND MARCA LIKE "%{}%" AND MODELO LIKE "%{}%"'.format(ID, Marca, Modelo)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro
    
        #carga la tabla de plataforma para seleccionar modelo
    def load_tableplataforma(self, ID, Marca, Modelo, tipoplataforma): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  PLATFORM_MODELS JOIN PLATFORM_EQUIPMENTS ON PLATFORM_MODELS.ID_PL = PLATFORM_EQUIPMENTS.ID_PL WHERE PLATFORM_MODELS.ID_PL LIKE "%{}%" AND MARCA LIKE "%{}%" AND MODELO LIKE "%{}%" AND TIPOPLATAFORMA LIKE "%{}%"'.format(ID, Marca, Modelo, tipoplataforma)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro




    #<------------Metodos para delete register------------>
    
    #Mostrar la tabla en la ventana dialog-delete
    def mostrar_table_delete(self, machinary):
        cursor = self.conexion.cursor()
        if machinary == "Tractor":
            bd = 'SELECT * FROM TRACTOR_MODELS' 
        elif machinary == "Cosechadora":
            bd = 'SELECT * FROM COMBINEHARVESTER_MODELS' 
        elif machinary == "Plataforma":
            bd = 'SELECT * FROM PLATFORM_MODELS' 
            
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro


    ####################### Backup de nota de pedidos #######################

    #Guardar nueva fila en Equipos entregados
    def guardar_equipo_entregado(self, list_save, fechaentrega):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO ORDER_NOTE_BACKUP(ID_PEDIDO, CLIENTE, FECHA, TRACTOR, ID_T, COSECHADORA, ID_C, PLATAFORMA_SOJERA, ID_PL_S, PLATAFORMA_MAICERA, ID_PL_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, FECHADEENTREGA, ESTADO) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save [12],list_save[13], list_save[14], list_save[15], fechaentrega, "ENTREGADO")
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
    #Restaurar fila de Equipos entregados a nota de pedidos
    def Restaurar_equipo_entregado(self, list_save):
        cursor = self.conexion.cursor()
        bd = 'INSERT INTO ORDER_NOTE(ID_PEDIDO, CLIENTE, FECHA, TRACTOR, ID_T, COSECHADORA, ID_C, PLATAFORMA_SOJERA, ID_PL_S, PLATAFORMA_MAICERA, ID_PL_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, FECHADEENTREGA, ESTADO) VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(list_save[0], list_save[1], list_save[2], list_save[3], list_save[4], list_save[5], list_save[6], list_save[7], list_save[8], list_save[9], list_save[10], list_save[11], list_save [12],list_save[13], list_save[14], list_save[15], "-" , "NORMAL")
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()
        
        
    def eliminar_fila_ee(self, id):
        cursor = self.conexion.cursor()
        bd = 'DELETE FROM ORDER_NOTE_BACKUP WHERE ID_PEDIDO = {}'.format(id)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    
    def search_id_backup(self, ID):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  ORDER_NOTE_BACKUP WHERE ID_PEDIDO = {}'.format(ID)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro



    
    def mostrar_ee(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM  ORDER_NOTE_BACKUP'
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro
    
    
    #<------------Metodo para cargar tabla de equipos entregados con busqueda------------>
    def search_ol_ee(self, CLIENTE, TRACTOR, COSECHADORA, PLATAFORMA_S, PLATAFORMA_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, ESTADO): 
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM ORDER_NOTE_BACKUP WHERE CLIENTE LIKE "%{}%" AND TRACTOR LIKE "%{}%" AND COSECHADORA LIKE "%{}%" AND PLATAFORMA_SOJERA LIKE "%{}%" AND PLATAFORMA_MAICERA LIKE "%{}%" AND CHASISEMBOCADOR LIKE "%{}%" AND RODADO LIKE "%{}%" AND OBSERVACIONES LIKE "%{}%" AND LOCALIDAD LIKE "%{}%" AND PROVINCIA LIKE "%{}%" AND ESTADO LIKE "%{}%"'.format(CLIENTE, TRACTOR, COSECHADORA, PLATAFORMA_S, PLATAFORMA_M, CHASISEMBOCADOR, OBSERVACIONES, RODADO, LOCALIDAD, PROVINCIA, ESTADO)
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()

        return registro

    #<------------Metodo para pedidos a proveedores------------>

    def id_pp(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT ID_PP FROM PEDIDOS_PROVEEDOR'
        cursor.execute(bd)
        ID = cursor.fetchall()
        cursor.close()

        return ID
    
    def proveedores(self):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM PROVEEDOR_P'
        cursor.execute(bd)
        data = cursor.fetchall()
        cursor.close()

        return data

    def busqueda_proveedores(self, proveedor):
        cursor = self.conexion.cursor()
        bd = 'SELECT * FROM PROVEEDOR_P WHERE PROVEEDOR LIKE "%{}%"'.format(proveedor)
        cursor.execute(bd)
        data = cursor.fetchall()
        cursor.close()

        return data
