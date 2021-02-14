
# My Wall / Django

# Live demo

This is a example implementation of the Django Rest Framework. Also it is included some Model y View tests.


# 1. ¿How to reproduce?

## 1. (Optional) Set a VirtualEnviroment
*There are many ways to set a virtual enviroment, it depends of your host OS. In this case we are using python3 directly.

1. Go to project folder

2. Create a virtual enviroment folder with python 3 `python3 -m venv venv`

3. Activate the virtual enviroment 
  a. (Unix) `source venv/bin/activate`
  b. (Windows) `.\venv\Scripts\activate`

## 3. Create and configure a Database
*In my case a prefer the Docker way

1. create a postgres docker `docker run --name some-postgres -p5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

## 3. Dependencies Installation and start api

5. Install python 3 dependencies listed on requirements.txt `pip install -r requirements.txt`

6. Go to core folder: `cd ./mywall`

6. Apply configurations and schema to configured database: `python manage.py makemigrations` or `python manage.py migrate`

7. Start django rest api  `python manage.py runserver`

## 4. Django Testing

8. Open new tab Terminal inside the core folder `cd ./mywall`

9. Run the following command: `python manage.py test`

## 5. Enjoy!

10. Dont forget to start the React project for the complete experience: https://github.com/nistalhelmuth/mywall-react

11. Feel free to try
