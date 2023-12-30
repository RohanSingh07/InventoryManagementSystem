# Inventory Management System Web Application

## Follow below steps to setup this repo on your local machine

1. Open command promt on your local machine and run command<br>
   `git clone "https://github.com/RohanSingh07/InventoryManagementSystem.git"` to clone the repo.
2. Step 1 will clone the project creating a folder called "InventoryManagementSystem".<br>
   ------- For windows --------
3. Inside the project folder create a virtual enviroment by running the command "virtualenv env",<br>
   if you don't have virtualenv library installed, first install the library<br>
    into the system by running "pip install virtualenv".<br>
4. Activate the virtual environment<br>
   4.1. "cd env/Scripts"<br>
   4.2. "activate"<br>
  ------- For Linux  -------<br>
3. Inside the project folder create a virtual enviroment by running the command "python3 -m venv env"<br>
4. Activate the virtual environment<br>
   4.1. "source env/bin/activate"<br>
   
5. To install all the dependencies run command "pip install -r requirements.txt" inside the project folder.<br>
6. run command "python manage.py runserver" to start python development server on localhost.

    ------- To test the APIS ------<br>

7. On the homepage of the web application we have two buttom "Add Product" and "Show All Product"<br>

8. Click on "Add Product" to add new product to the inventory database.<br>
  Clicking on the button will open a form for all the fields related to product.<br>
  Fill those fields and click of "ADD LISTING" button at the end of the form to submit the values.<br>
  If all the values are in correct format the page will be redirected to the homepage with a message on the top saying "Product added to inventory".<br>
  
9. By clicking on the other button "Show ALl Product" we can see all the products uploaded to the inventory.<br>

-------------------------------------------------------- THANKS :) ------------------------------------------------------------------------------
