from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete
from django.core.signals import request_started, request_finished, got_request_exception

@receiver(user_logged_in, sender=User)
def receiver_func(sender, request, user, **kwargs): # Receiver function that receive the signal from sender
    print("User logged in signal")
    print('sender:', sender)
    print('request:', request)
    print('user:',user)
    print(f'kwargs {kwargs}')


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs): #To receive the signal when user logout 
    print("User logged out signal", user_logged_out)
    print('sender:', sender)
    print('request:', request)
    print('user:',user)
    print(f'kwargs {kwargs}')

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("___Login failed____")
    print("sender :", sender)
    print("request :", request)
    print("credentials :", credentials)
    print(f'kwargs {kwargs}')

    
# connection signal with receiver - signal.connect(rece_func, sender)
# user_logged_in.connect(receiver_func, sender=User)

# Model Signals
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("Pre save signal....")
    print("sender :", sender)
    print("instance :", instance)
    print(f'kwargs {kwargs}')



@receiver(post_save, sender=User)
def at_beginning_save(sender, created, instance, **kwargs):
    print("___________________")
    if created:
        print("New Records")
        print("Post save signal....")
        print("sender :", sender)
        print("created", created)
        print("instance :", instance)
        print(f'kwargs {kwargs}')
    else:
        print("Records Updated")
        print("Post save signal....")
        print("sender :", sender)
        print("created", created)
        print("instance :", instance)
        print(f'kwargs {kwargs}')



@receiver(pre_delete, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("Pre delete signal....")
    print("sender :", sender)
    print("instance :", instance)
    print(f'kwargs {kwargs}')


@receiver(post_delete, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("____________")
    print("Post delete signal....")
    print("sender :", sender)
    print("instance :", instance)
    print(f'kwargs {kwargs}')



@receiver(pre_init, sender=User)
def at_beginning_save(sender, *args, **kwargs):
    print("____________")
    print("Pre init signal....")
    print("sender :", sender)
    print(f'args {args}')
    print(f'kwargs {kwargs}')

@receiver(post_init, sender=User)
def at_beginning_save(sender, *args, **kwargs):
    print("____________")
    print("Post init signal....")
    print("sender :", sender)
    print(f'args {args}')
    print(f'kwargs {kwargs}')


#Request/Response Signals
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("request started..........")
    print("environ :", environ)


@receiver(request_finished)
def at_ending_request(sender,  **kwargs):
    pass


@receiver(got_request_exception)
def exception_at_requst(sender, **kwargs):
    pass