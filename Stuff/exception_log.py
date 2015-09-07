
#Excepcion log

# e -> The exception
# m -> Message that caused the exception

def exception_log(e,m):
    hour = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%y")
        
    complete_date = 'Times exception':  + str(date) + ' ' + str(hour) + '\n'
    
    cause = 'Cause of the exception: ' + str(m.text) + '\n'
    
    exception = 'Exception: ' + str(e)
    
    information = complete_date + cause + exception
    
    
    aux = open( 'exception.txt', 'a') 
    aux.write( str(information) + "\n\n")
    aux.close()
    
    
## Output
#
