Inventory Management System Web Application

Follow below steps to setup this repo on your local machine

1. Open command promt on your local machine and run command 'git clone "https://github.com/RohanSingh07/InventoryManagementSystem.git"' to clone the repo.
2. Step 1 will clone the project creating a folder called "InventoryManagementSystem".
   ------- For windows --------
3. Inside the project folder create a virtual enviroment by running the command "virtualenv env", if you don't have virtualenv library installed, first install the library
    into the system by running "pip install virtualenv".
4. Activate the virtual environment
   4.1. "cd env/Scripts"
   4.2. "activate"
  ------- For Linux  -------
3. Inside the project folder create a virtual enviroment by running the command "python3 -m venv env"
4. Activate the virtual environment
   4.1. "source env/bin/activate"
   
5. To install all the dependencies run command "pip install -r requirements.txt" inside the project folder.
6. run command "python manage.py runserver" to start python development server on localhost.

------ To test the APIS ------
7. On the homepage of the web application we have two buttom "Add Product" and "Show All Product"
8. Click on "Add Product" to add new product to the inventory database. Clicking on the button will open a form for all the fields related to product.
  Fill those fields and click of "ADD LISTING" button at the end of the form to submit the values. If all the values are in correct format the page will
  be redirected to the homepage with a message on the top saying "Product added to inventory".
9. By clicking on the other button "Show ALl Product" we can see all the products uploaded to the inventory.

-------------------------------------------------------- THANKS :) ------------------------------------------------------------------------------------------------
