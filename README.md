# IGS_employee_manager

## Before Start

Before starting the project we need to prepare a enviroment to make everything run. So after cloning this repository create a python enviroment and make sure you are using it. Then we need to install all libraries to execute, in the project we have a file named **requirements.txt**, you can use **pip** to install everything. So now we are available to start this project.

## First Steps
As every django project we need to create migrations on our local machine, so in the promp you create the migrations and execute them.
Now we can run our application using **python manage.py runserver**, if everything is right the command line will show this message to you
<div align="center">
  <img src="https://user-images.githubusercontent.com/51749951/236271801-026e1fa7-ac32-43a7-9c45-9e18daaca1bd.png">
</div>
To facility the usage you can generate some dummy register, using the endpoint **http://127.0.0.1:8000/populate/** and sendind a post request.

<img src="https://user-images.githubusercontent.com/51749951/236271796-bf9c6e1b-c96e-493b-ba74-c39996e0545b.png">

## functionalities

###### Employees and departments
We manage the data from employee(name, email and wich department he/she is from), and also we manage the department too, at the moment we only can create or change the name from department.
To avoid repeated names in departments, we save these names in lower case, without the option to use a upper case character.

<img src="https://user-images.githubusercontent.com/51749951/236271803-1c1a9474-69df-4863-ac10-5e0daa0c89e2.png">

###### Admin panel
This system manages the employee and the department of a company, as we are using django we have option to do everything on django admin panel(you need to create a admin user to access the portal).

###### API
There is another way to use this system, the rest api. So we can do all the same in admin panel in requests (get, post,patch and delete).
<div align="center">
  <img src="https://user-images.githubusercontent.com/51749951/236271793-2779468f-3de8-4c77-a4f1-0b1321fc3a62.png" width=80%>
  <img src="https://user-images.githubusercontent.com/51749951/236271788-f406b435-1706-4ddc-98e9-29e0bef4aa64.png" width=80%>
  <img src="https://user-images.githubusercontent.com/51749951/236271812-febf5958-14de-4411-a623-5237a1c6d9a9.png" width=80%>
  <img src="https://user-images.githubusercontent.com/51749951/236271799-abd35243-a8f2-4a92-8a7e-d5f98fc37f67.png" width=80%>
  <img src="https://user-images.githubusercontent.com/51749951/236271806-ea7c8325-842f-4233-a442-13ec8872241d.png" width=80%>
  <img src="https://user-images.githubusercontent.com/51749951/236271809-b797b20f-3bc3-461e-8d8c-b0939fff7eba.png" width=80%>
</div>
