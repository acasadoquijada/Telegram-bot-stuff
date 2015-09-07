##########################
#       Activity log     #
##########################

def log(m):
    user_id = m.from_user.id
    name = m.from_user.first_name
    last_name = m.from_user.last_name
    username = m.from_user.username
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    information = "["+ str(date) + ' ' + str(hour) + ' ' +str(name)  + ' ' + 
    str(last_name) + ' ' + str(user_id) + ' @' + str(username) + "]: " + m.text 
    
    aux = open( 'log.txt', 'a')
    aux.write( str(information) + "\n")
    aux.close()

## An example of the output
## [02/09/15 11:51:34 name last_name id username]: /command text
