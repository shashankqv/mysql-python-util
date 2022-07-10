# mysql-python-util

Blog Link : https://shashankvivek.in/2022/07/11/using-python-to-execute-mysql-insert-and-update-queries/

This is a MySQL command line utility project written in Python. 

You can do below things.
Execute an insert / update query with an option to manually commit the result. Basically before commmiting any result to database it asks whether you want to proceed or not by showing number of effected rows.

Usage : 
--------
```
python insert_update.py --query "your_query"
```


Development :
--------------
This runs on python 2.7 versions.

Install Dependencies :
--------------------
```
pip install -r requirements.txt
```
