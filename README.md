# EworkerDjango

# How to run project:
1. Clone repository `git clone https://github.com/e-worker/EworkerDjango.git`
2. Install anaconda for python 3.7 (or another tool that will allow you to create virtualenv, such as pipenv or virtualenv)
[Anaconda download link (choose right OS!)](https://www.anaconda.com/distribution/)
3. After installing anaconda:
 ##### on Windows:
 - open Anaconda Prompt and navigate to project directory using cd, then type: conda create --name Ework 
 this will create virtual environment for our django application
 after succesfull environment creation type conda activate Ework, and run:     
 pip install -r requirements.txt
 (make sure you are in correct directory, where requirements.txt file is located)
##### on Unix-based system:
- open bash console and navigate to project directory, then type conda create --name Ework
this will create virtual environment for our django application
after succesfull environment creation type source activate Ework, and run:     
pip install -r requirements.txt
 
###### Your environment should be set up now
when you are working with Django, always work with your environment activated (conda activate Ework)
otherwise your project won't run

4. with active Ework environment you can use django's commands in terminal, such as:
```python
python manage.py runserver # runs server on localhost:8000
python manage.py makemigrations # creates migration files (use after creating new models in models.py)
python manage.py migrate # migrate database (based on migration files)
python manage.py createsuperuser # creates admin account so you can access /admin page
```

# Project's structure explanation:
Eworker Django
|
<p>|- Ework -> contains settings.py, urls.py and __init__.py, wsgi.py files (only urls and settings intrests us)</p>
|- employer - app that will cover logic for company/employer (create read update)
|- job_offers - app that will cover logic for job offers (create read delete)
|- student - app that will cover logic for student's account (create read update)
|- templates - folder that contains html files which are treated as a templates, we will fill them using content from db 
|- users - app that will  cover generic logic for account (register login)
|- manage.py - Django's command-line utility for administrative tasks

# Request-response cycle in Django:
![request-response](https://4.bp.blogspot.com/-KowrZmen8ko/WMluNkJmN5I/AAAAAAAACCU/SePlDNoOUmkdB_mck0gKDTZB4qgROlzzgCLcB/s640/django-request-life-cycle.png)

# Models we need to create student's cv:
(let's assume that multiple means >= 1)
<p>Student (and that model is foreign key in models below)</p>
Student Info (multiple) -> student skill -> skill
Student degree course (multiple) -> degree course -> department
Student language (multiple) -> language -> language_lvl

# Models we need to create job offer: 
(again we are assuming that multiple means >=1)
Company (and that model is foreign key in Job Offer)
Job offer (and that model is foreign key in models below)
Job info (multiple) -> student skill -> skill
Offer degree course (multiple) -> degree course -> department
Job offer language (multiple) -> language -> language_lvl

