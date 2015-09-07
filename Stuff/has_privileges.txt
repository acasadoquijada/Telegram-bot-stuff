################################################################################
# has_privileges function
################################################################################

def has_privileges(m):
    f = open("permissionlist.txt", "r")
    ulist = f.read()
    f.close()
    pos = ulist.find("-")
    privs = ulist.find(m.from_user.username,0,pos)
    if privs != -1:
        privileges = True
    else:
        privileges = False
    return privileges

################################################################################
# This function needs a file with @usernames. Privileged people must be before
# '-' caracter.
# Permissionlist.txt could be like this:
################################################################################

@user1
@user2
-------- # after this line, people don't have permissions
@user3
@user4
@user5