import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','payroll_management_sys.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import django
from payroll_manager.models import Account
django.setup()
#write script
def populate(n):
    for i in range(1,n+1):
        user = Account()
        user.user_id = i
        user.set_password("password")
        user.is_employee=True
        user.save()
    user = Account()
    user.user_id = 0
    user.set_password("password")
    user.is_employee=False
    user.is_employer=True
    user.save()
#end script
if __name__ == '__main__':
	populate(11)