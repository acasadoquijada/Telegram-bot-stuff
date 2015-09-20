################################################################################
# new_users_saver funciton
################################################################################

def newusers(m):
    dict_updater()
    un = m.from_user.username
    if un not in DBDIC:
        uid = m.from_user.id
        DBDIC[un] = [uid,0]
    if hasattr(m, 'new_chat_participant'):
        un = m.new_chat_participant.username
        if un not in DBDIC:
            uid = m.new_chat_participant.id
            DBDIC[un] = [uid,0]
    dict_saver()

################################################################################
# "newusers" saves new users in the dictionary
# (see dict_updater_saver.py for "dict_updater()" and "dict_saver()")
################################################################################