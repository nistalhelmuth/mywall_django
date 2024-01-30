
# My Wall / Django

# Live demo

This is a example implementation of the Django Rest Framework. Also it is included some Model y View tests.


# ¿How to reproduce?

## 1. (Optional) Set a VirtualEnviroment
*There are many ways to set a virtual enviroment, it depends of your host OS. In this case we are using python3 directly.

1. Go to project folder

2. Create a virtual enviroment folder with python 3 `python3 -m venv venv`

3. Activate the virtual enviroment 
  a. (Unix) `source venv/bin/activate`
  b. (Windows) `.\venv\Scripts\activate`

## 2. Create and configure a Database
*In my case a prefer the Docker way

4. create a postgres docker `docker run --name some-postgres -p5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

## 3. Dependencies Installation and start api

5. Install python 3 dependencies listed on requirements.txt `pip install -r requirements.txt`

TODO: psycopg2-binary dependency have issues from requirements. check how to solve it, manual instalation works. [More Info](https://stackoverflow.com/a/49812755)

### IMPORTANT NOTE

TODO: Update how to configure database credentials as env variables. .env file works but needs to be configured properly.

1. Check and change(if needed) the database configurations in settings.py in mywall(Main folder):

![Database Settings](https://github.com/nistalhelmuth/mywall_django/blob/main/Photo2.png "Database Settings")

7. Add email server configurations at the bottom of settings.py in mywall(Main folder):

![Mail Settings](https://github.com/nistalhelmuth/mywall_django/blob/main/Photo.png "Mail Settings")


8. Apply configurations and schema to configured database: `python manage.py makemigrations` and `python manage.py migrate`

9. Start django rest api  `python manage.py runserver`

## 4. Django Testing

10. Open new tab Terminal inside the core folder `cd ./mywall`

11. Run the following command: `python manage.py test`

## 5. Enjoy!

12. Dont forget to start the React project for the complete experience: https://github.com/nistalhelmuth/mywall-react

13. Feel free to try
