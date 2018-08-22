from pythonlsf import lsf

def queryUserInfoAll():
    """
    "Query all user info"
    """
    if lsf.lsb_init("queryUserInfoAll") > 0:
        return -1;
    
    for user_info in lsf.get_all_user_info():
        print "user: {0}, priority: {1}".format(user_info.user, user_info.priority)

    return 0;

if __name__ == '__main__':
    queryUserInfoAll();
