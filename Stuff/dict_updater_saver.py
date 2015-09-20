################################################################################
# dict_updater and dict_saver functions
################################################################################

def dict_updater():
    with open("./files/uidprivs.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            # row[0] = username
            # row[1] = user id
            # row[2] = privileges
            DBDIC[row[0]] = [row[1], row[2]]

########################################

def dict_saver():
    with open("./files/uidprivs.csv","wb") as f:
        writer = csv.writer(f)
        for key in DBDIC:
            writer.writerows([[key, DBDIC[key][0], DBDIC[key][1]]])

################################################################################
# For this two functions you need a file call uidprivs.csv and a dictionary 
# previusly declared. The file structure is below
################################################################################

# beginning of the file
"user","id","privileges"
@user1,103832,0
@user2,3829453,0
@user3,8432984,1
# end of file