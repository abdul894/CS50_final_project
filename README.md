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
 
windows:
```bash
venv\Scripts\Activate.ps1
```
MacOS:
```bash
source venv/bin/activate
```

Now you need to install the project's dependencies by just running this one command.
```bash
pip install -r requirements.txt
```
The project has it own database, but if you want to create your own you can simply run `rm fumo.db` to remove the old one. Now you need to run this command:
```bash
flask --app app.py init-db
```

This command will create a database with necessary fields.

Setup is complete let's run the app.

```bash
flask --app app.py run
```

first register your self!

