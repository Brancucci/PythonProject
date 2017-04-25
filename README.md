## PythonProject
Group project assigned in advanced python course at USF

Login - a login window upon success takes user to selection

Selection - a main window where the user chooses from three options below

Quizzer- The Quizzer generates equations for which the user supplies the answer

Solver - The Solver provides the answer to a fractions equation supplied by the user

Results - The Results Viewer presents a bar chart showing the user's average score for each operator and for all operators combined

## How to install dependencies
CD into the folder with the requirements.txt file and use => pip install -r requirements.txt

## Instructions to run server

CD into the folder with the manage.py file

In the terminal type: python manage.py runserver

open app at: localhost:8000/math

## How to Login
localhost:8000/math/login

## active students registered for Login and Testing
user: student01     password: password01

user: student02     password: password02

user: student03     password: password03

user: student04     password: password04

user: student05     password: password05

## Create an admin user
python manage.py createsuperuser

Enter a username, email, and password

While app is running open app at: localhost:8000/admin for admin priviledges.

## To invoke Python shell
python manage.py shell

## To get user ID
{{ user.get_username }}

## DB Note: There is a hidden 'id' column that is auto imcremented and is the primary key
To find row by id: Results.objects.filter(id=1)


