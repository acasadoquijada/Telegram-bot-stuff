################################################################################
# search_users function
################################################################################

def search_user(m):
    txt = m.text
    if txt.find(" ") != -1: # any message?
        pos1 = txt.find("@")
        if pos1 != -1:
            pos2 = txt.find(" ",pos1)
            if pos2 == -1:
                user_name = txt[pos1+1:] # +1 para quitar @
            else:
                user_name = txt[pos1+1:pos2] # +1 para quitar @
            return user_name
    return -1

################################################################################
# An example of use can be:
# > /say_to @user1 hola
# this function will return 
# > @user1
################################################################################
