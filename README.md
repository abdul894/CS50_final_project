# FUMO
#### Video Demo:  <https://youtu.be/mPYcsCb7uz8>
#### Description:

FUMO is an e-commerce website created using Python Flask. Users can easily register, browse products, add items to their carts, and view their selections. For administrators, the platform provides the ability to add new products, manage existing ones, view user lists, and perform actions like editing or deleting products.

To clone the repo to your local machine, first you need follow these instructions:

- [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

> **_Note:_** To run this project locally you must have Python 3.11.4 or above and sqlite3 3.44.0 or above in your local machine.

After following above instructions create virtual enviroment in your project directory.

```bash
python -m venv venv
```
this command will create a virtual enviroment in your project directory. Now you need to activate the virtual enviroment
 
### windows:
```bash
venv\Scripts\Activate.ps1
```
### MacOS:
```bash
source venv/bin/activate
```

Now you need to install the project's dependencies by just running this one command.
```bash
pip install -r requirements.txt
```
The project has it own database, but if you want to create your own you can simply run `rm fumo.db` to remove the old one (with caution). Now you need to run this command:
```bash
flask --app app.py init-db
```

This command will create a database with necessary fields.

Setup is complete let's run the app.

```bash
flask --app app.py run
```

first register your self!

Click on the login icon.
 
 ![homepage](/assets/Homepage.png)


 Now go to **Create an Account**.


 ![loginpage](/assets/loginpage.png)



 Fill up the form!


 ![registerpage](/assets/Register%20page.jpg)

 Once you've registered to need to change the **type** to **admin** to access the admin dashboard. In order to do that you need to run this sqlite command.

```bash
UPDATE users SET type = 'admin' WHERE email = '**your_registered_email**';
``` 

Now you can access admin dashboard and do the generic admin stuff.

To list new porducts go the product listing tab.

![admin dashboard](/assets/admin%20dashboard.png)

fill up the necessary information and click on **Add product**. your product is now visible to users.

If you need to change some information later on in your product click on edit icon you're good to go.

![editprodut](/assets/edit%20product.png)

you can also delete listed products by just clicking on delete icon.

If you want to see how many users are currently registered to your site visit **Users** tab in the Nav bar.

Finally register some your user's and try adding some prducts to your cart.

![addtocart](/assets/addtocart.png)

Cart!

![cart](/assets/cart.jpg)

user's can empty their cart by clicking on **delete** icon.

that's it for this one.

## This was CS50!
