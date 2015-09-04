#Activity log
def log(m):
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    user_last_name = m.from_user.last_name
    user_alias = m.from_user.username
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    information = "["+ str(fecha) + ' ' + str(hora) + ' ' +str(nombre_usuario)  + ' ' + str(apellido_usuario) + ' ' + str(id_usuario) + ' @' + str(alias) + "]: " + m.text 
    
    aux = open( 'log.txt', 'a')
    aux.write( str(information) + "\n")
    aux.close()
