# CS4400_Project

## Platform

Mac OS 13.0

## Environment

Python 3.11 and MySQL 8.0


## Installation

Load the sql file

```
$ /usr/local/MySQL/bin/mysql -u root -p
Enter password:
mysql> source cs4400_database_v2 schema_and_data.sql
mysql> source cs4400_phase3_stored_procedures_team#78.sql
```

Modify the app.py

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysqs://username:password@127.0.0.1:3306/database_name'
```

Please notice that the username, password and database_name is your own setting of database.

create & active virtual enviroment then install all the required packages of Python:

```
$ python3 -m venv venv
$ source venv/bin/activate 
(env) $ pip install -r requirements.txt
```

Run the program:

```
(env) $ flask run
* Running on http://127.0.0.1:5000/
```

## Explanation

Front-end is based on the bootstrap template. For the back end, we implement it by flask, which is a micro web framework written in Python. 

## Team Members' Distribution

Peizhen Zheng (pzheng46): Bootstrap templates and 6 display views with corresponding functions in flask and html file.

Junyang Tang(jtang375): stored procedures 1-8 with corresponding functions in flask and html files.

Anjin Luo (aluo64): stored procedures 9-15 with corresponding functions in flask and html files.

Yaxin Xue (yxue95): stored procedures 16-23 with corresponding functions in flask and html files.



