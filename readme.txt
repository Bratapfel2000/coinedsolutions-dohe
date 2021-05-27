0.) dont show sekret key

00.) pips:
	django-environ
	
	
1.) copy coinedsolutions to here
2.) create pipenv
3.) set scret key on fake number
4.) python manage.py makemigrations + python manage.py migrate
5.a) create .env file in same folder than settings.py:
	SECRET_KEY
	DEBUG
	ALLOWED_HOSTS
	
5.b.) Set in settings
	SECRET_KEY = env('SECRET_KEY')
	DEBUG = env('DEBUG')
	ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')


6.) pip install django-environ
	add to settings:
	import environ
	env = environ.Env()
	# reading .env file
	environ.Env.read_env()

7.) create settings folder in same folder like settings.py
	create __init__.py
	move settings.py and .env in settings folder
	
	in settings.py add parent so sql will be stored in root directory
	BASE_DIR = Path(__file__).resolve().parent.parent.parent

8.)  create storage.py in settings folder
9.)



pip install django-storages & boto3
