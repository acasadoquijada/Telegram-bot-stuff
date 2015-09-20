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
                user_name = txt[pos1+1:] # +1 to ignore @
            else:
                user_name = txt[pos1+1:pos2] # +1 to ignore @
            return user_name
    return -1

################################################################################
# This function searches any @username in the message
################################################################################
