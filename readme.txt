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

9.) AWS
9.a) go to AWS S3 and create new bucket abc123
	scroll down a bit, allow all public access
9.b) IAM
	Policies: Create new Policiy or add this json:
		{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::abc123",
                "arn:aws:s3:::abc123/*"
            ]
        }
    ]
}

	give a name: coineddohe-s3
9.c) create new user: coineddoheuser with Programmatic access and attach policy from 9.b

10.) pip install django-storages
     pip install boto3

	update requirements: pip freeze > requirements.txt 

     add in settings.py installed apps-> 'storages',


11.) move key etc to storages
     create static folder in root
     manage.py collectstatic












pip install django-storages & boto3
