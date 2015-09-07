
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
    
    
## Output:

# Times exception:07/09/15 17:55:26
# Cause of the exception: /adios
# Exception: A request to the Telegram API was unsuccessful. The server returned HTTP 400 Bad Request. Response body:
# [{"ok":false,"error_code":400,"description":"Error: Bad Request: wrong chat id"}]


