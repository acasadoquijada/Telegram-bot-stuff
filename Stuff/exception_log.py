def exceptions_log(e,funtion):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
    
    information = "[" + str(date) + ' ' + str(hour) + ' ' + str(funtion) + "]: " + str(e) 
    aux = open( 'exception.txt', 'a') 
    aux.write( str(information) + "\n")
    aux.close()
