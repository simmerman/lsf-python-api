from pythonlsf import lsf

def queryUserInfo():
    """
    "Query user info by username(s)"
    """
    if lsf.lsb_init("queryUserInfo") > 0:
        return -1;
    
    usernames = ["validusr1", "validusr2"]
    
    for idx, user_info in enumerate(lsf.get_user_info(usernames)):
        if user_info != None:
            print "\nuser: {0}, maxJobs: {1}".format(user_info.user, user_info.maxJobs)
        else:
            print "\nNo information found for user {0}".format(usernames[idx]) 

    return 0;

if __name__ == '__main__':
    queryUserInfo();
