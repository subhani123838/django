from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
#WHENEVER U LOGGINED AUTOMATICALLY SIGNALS WILL REFLECT FROM THE BELOW CODE
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("--------------------")
    print("successfully loggined in")
    print("Run Introduction")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print(f'kwargs:{kwargs}')
#user_logged_in.connect(login_success,sender=User)

#WHENEVER U LOGGOUT AUTOMATICALLY SIGNALS WILL REFLECT FROM THE BELOW CODE
@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print("--------------------")
    print("ur details are incorrect to login")
    print("logged out ntroduction")
    print("sender:",sender)
    print("request:",request)
    print("user:",user)
    print(f'kwargs:{kwargs}')
#WHENEVER UR DETAILS R WRONG THEN SIGNALS WILL REFLECT FROM THE BELOW CODE
@receiver(user_login_failed)
def login_in_failed(sender,request,credentials,**kwargs):
    print("*****************")
    print("ur details r failed to log-in")
    print("Invalid details")
    print("sender:",sender)
    print("request:",request)
    print("user:",credentials)
    print(f'kwargs:{kwargs}')
#SIGNALS TO REFLECT FOR MODEL RELated:-
#-------------------------------------------
#FOR THIS WE HAVE TO IMPORT FEW THINGS
#------------------------------------
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete,pre_init,post_init
@receiver(pre_save,sender=User)
def at_begin_save(sender,instance,**kwargs):
    print("*****************")
    print("when ur trying save some data then signals will reflect")
    print("instance:",instance)
    print("sender:",sender)
    print(f'kwargs:{kwargs}')

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("*****************")
        print("post-save signal")
        print("when ur r trying to update some data u will get")
        print("new record updated")
        print("instance:", instance)
        print("sender:", sender)
        print(f'kwargs:{kwargs}')
    else:
        print("*****************")
        print("when ur r trying to create some data u will get")
        print("pre-save signal will reflect")
        print("instance:", instance)
        print("sender:", sender)
        print(f'kwargs:{kwargs}')

@receiver(pre_delete,sender=User)
def at_begin_delete(sender,instance,**kwargs):
    print("*****************")
    print("when ur trying to delete some data then signals will reflect")
    print("instance:",instance)
    print("sender:",sender)
    print(f'kwargs:{kwargs}')

@receiver(pre_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("*****************")
    print("when ur trying to delete some data then signals will reflect")
    print("instance:",instance)
    print("sender:",sender)
    print(f'kwargs:{kwargs}')