import sys
from importlib import import_module

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        mod = 'settings'
    else:
        mod = sys.argv[1]
    settings = import_module(mod)

    try:
        print("HOST=%s" % settings.DATABASES['default']['HOST'])
    except:
        pass
    try:
        print("USER=%s" % settings.DATABASE_SUPERUSER)
    except:
        pass
    try:
        print('''SHELLCMD="from helios_auth.models import User; %s"''' % ' '.join("User.objects.create(**%s);" % repr(user) for user in settings.RESET_USERS))
    except:
        pass
