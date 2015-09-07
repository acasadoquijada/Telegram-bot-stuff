################################################################################
# search_users function
################################################################################
def search_user(m):
    text = m.text
    pos1 = text.find("@")
    if pos1 != -1:
        pos2 = text.find(" ",pos1)
        user_name = text[pos1:pos2]
        return user_name
    return -1

################################################################################
# An example of use can be:
# > /say_to @user1 hola
# this function will return 
# > @user1
################################################################################
