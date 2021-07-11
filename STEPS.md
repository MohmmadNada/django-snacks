
# django-snacks
1. create a Github repo named django-snacks
2. create folder django_snacks
3. `cd django_snacks`
4. create django project named snacks_project
    1. `poetry init -n`
    2. `poetry add django`
    3. `poetry add --dev black`
    4. `poetry shell `
    5. `django-admin startproject snacks_project . ` 
       1. this command must write once
       2. . in the last very important, its means here 
    6. check the files installed 
    7. `python  manage.py runserver`
    8. after error message Run `python manage.py migrate` to apply them.
    9. run `python  manage.py runserver` then open the link on your browser 
>     note: the command now must be written in the way `python  manage.py  command ` 
>     note: project may be have more than application 
    10. create django app named snacks
    11. `python manage.py startapp snacks`
    12. add app to project

        1.  add `'django.middleware.clickjacking.XFrameOptionsMiddleware',` in (setting project)
        2.  import os in (setting project) and add path line
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        3.  add app to project
        4.  in project - urls - import include 
        5.  add urls.py in app and add to yrls priject line 21 
    14. add to app - viwes  
    13. add templates floder and html files 


   
### add new page steps:
   1. app -> urls ->  add -> `path('pageNama', AboutView.as_view(), name='addName')`
   2. app -> views -> add child class -> 
    ``` 
    class pageNamaView(TemplateView):
    template_name = 'pageNama.html'
    ``` 
### run the test py command 
1. app - test 
2. import SimpleTestCase and reverse
3. add classes add functions 
4. run in terminal `python mange.py test`