import os
import subprocess
import webbrowser


# to do 
'''
1-venv
2-activate venv
3-install django
4-create project
5-create app[option]
6-migrate
7-create super user
8-runserver
9-website
'''
venv_name = str(input('Enter the name of venv : '))
os.system(f'python -m venv {venv_name}')
path = os.path.abspath(f'{venv_name}/Scripts')
#venv_name/Script
os.chdir(path)
os.system('activate')
os.system('pip install django')
os.chdir(os.path.abspath('../..'))
project_name = str(input('Enter the name of project : '))
subprocess.run(f'django-admin startproject {project_name}')
projectPath = os.path.abspath(f'{project_name}')
os.chdir(projectPath)
query = str(input('Would you like to create new app ? Y/n '))
#yes / y / ye /e /s 
if query.lower() in 'yes':
    app_name = str(input('Enter the name of app : '))
    os.system(f'python manage.py startapp {app_name}')
else:
    pass
os.system('python manage.py migrate')
def createSuperUser():
    username = 'admin'
    email = 'admin'
    os.system(f'python manage.py createsuperuser --username={username} --email={email}')
# option create superuser with name admin 
createSuperUser()
os.system('exit')
webbrowser.open('http://127.0.0.1:8000/')
os.system('python manage.py runserver')
