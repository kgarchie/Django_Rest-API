# ELU
## A Django App with REST API

This app includes Google OAuth to ease signup and signin. This will coerce users to create accounts. Emails from these accounts can be used to push notifications and events about the organisation.
I made an REST API to enable bootstrapping of the project to other Applications on Andoid and IOS.

Required:

```
python
django
djangorestframework
django-allauth

```

Optional
```
django_crispy_forms
```
## Getting Started
You need python as the base interprater. Download and install it from [Here](https://www.python.org/downloads/)

To install on Windows machines with python already installed correctly

* open powershell/terminal as administrator(this will help us deal with some issues that may arise)
* change directory to your preferred directory (unnecessary, just note the current directory so that you don't lose your files) Use  ```cd``` to change directory eg ```cd desktop``` will change the working directory to the desktop which I can recommend as it is easy to find the files later.
* type ```mkdir Project``` We are making a directory named 'Project', but you can call it whatever you want.
* then cd into it using the command ```Project``` (this makes it the current working directory)
* create a virtual environment ```python -m venv myvenv```(this creates a virtual environment for python)
* activate the environment using ```myvenv/Scripts/activate``` (Note the S is capital). You may receive an error because running scripts is disabled. At this point restart powershell this time as administrator and type in this command 'set-executionpolicy remotesigned'. It will allow local scripts to run.

to be continued...



