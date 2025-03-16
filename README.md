# For a LIVE DEMO of this Django website, goto:
## https://maxloo.pythonanywhere.com/
### From Bash CLI:
- pip3 install django==5.0 pillow
- python3 manage.py runserver
### From PythonAnywhere Bash:
- rm -rf bookstore
- git clone https://github.com/maxloosmu/bookstore.git
- mkvirtualenv -p python3.10 virtualenv
- pip install django==5.0 pillow
- workon virtualenv
- cd bookstore/
- python manage.py collectstatic