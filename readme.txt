Instructions to Deploy Django App via Docker on Heroku

0.) dont show sekret key

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


12.) Dockerization
12.a) pip install gunicorn + safe in requirements.txt
12.b) create in same folder loke manage.py the Dockerfile. Using Py3.6 because issues with greater versions and psycopg2
	docker login
	docker build -t coinedsolutionsdohe:v3 .

	docker run -p 8000:8000 coinedsolutionsdohe:v3
	http://127.0.0.1:8000/

13.) Push to Dockerhub
	docker tag coinedsolutionsdohe:v1 paufourdm/coinedsolutionsdohe:latest
	docker push paufourdm/coinedsolutionsdohe:latest

	https://hub.docker.com/r/paufourdm/coinedsolutionsdohe

14.) update dockerfile for heroku deployment
	comment out EXPOSE 8000
	comment out CMD[....]

	comment in
        CMD gunicorn coinedsolutions.wsgi:application --bind 0.0.0.0:$PORT

15.) get heroku ready via cli
	 heroku container:login

16.) Delete env variables

	settings.py 
	#import environ
	
	take out in settings.py 
	>env = environ.Env()
	># reading .env file
	>environ.Env.read_env()

	
	SECRET_KEY=os.environ.get('SECRET_KEY')
	DEBUG='False'
	ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

17.) heroku create
	heroku container:push web --app <herokuappname>
	
	add variables here or directly on Heroku:
	heroku config:add ALLOWED_HOSTS=* -a <herokuappname>
	heroku config:get ALLOWED_HOSTS -a <herokuappname>
	
	heroku container:release -a <herokuappname> web
	heroku open -a=<herokuappname> 
	
	if problem, look on logs
	heroku logs --tail -a <herokuappname> 


