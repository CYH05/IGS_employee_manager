# IGS_employee_manager

## Before Start

Before starting the project we need to prepare a enviroment to make everything run. So after cloning this repository create a python enviroment and make sure you are using it. Then we need to install all libraries to execute, in the project we have a file named **requirements.txt**, you can use **pip** to install everything. So now we are available to start this project.

## First Steps
As every django project we need to create migrations on our local machine, so in the promp you create the migrations and execute them.


Now we can run our application using **python manage.py runserver**, if everything is right the command line will show this message to you

To facility the usage you can generate some dummy register, using the endpoint **http://127.0.0.1:8000/populate/** and sendind a post request.

## functionalities

###### Employees and departments
We manage the data from employee(name, email and wich department he/she is from), and also we manage the department too, at the moment we only can create or change the name from department.
To avoid repeated names in departments, we save these names in lower case, without the option to use a upper case character.

###### Admin panel
This system manages the employee and the department of a company, as we are using django we have option to do everything on django admin panel(you need to create a admin user to access the portal).

###### API
There is another way to use this system, the rest api. So we can do all the same in admin panel in requests (get, post,patch and delete).
