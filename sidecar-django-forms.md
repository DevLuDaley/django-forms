Syntax Key:

commit messages =

# - commit_message

terminal input =
▶
input

---

create github repo titled => django-forms
▶
git clone git@github.com:DevLuDaley/django-forms.git
▶
cd django-forms
▶
python3 -m venv env_pizza
▶
source env_pizza/bin/activate

# - create and activate (env_pizza)

- clone master branch to create 'django-setup' branch

▶
git pull

- do this so that local git knows about the new branch ('django-setup') created in remote git/GitHub
  ▶
  git checkout setup_django
  ▶
  pip install django

# - install django

▶ django-admin startproject nandiasgarden

# - create nandiasgarden project + folder

▶ mv nandiasgarden/ projectnandiasgarden
(tutorial says nandiasgarden-project but "name-project" is an invalid proj name in py 3.8)
rename project folder. add project to start of the name i.e folder => projectfolder or projectnandiasgarden for this project

this helps differentiate between the project folder and the autogenerate folder (with the identaical project name) that lives in the project folder

# - rename project folder to projectnandiasgarden

▶
django-admin startapp pizza

# - create app pizza

- on Github, create new remote branch => setup_frontend

▶
git checkout setup_frontend

# - git checkout setup_frontend

- urls.py =>

  - ['from pizza import views']

    add paths for home & order
    [path('', views.home, name='home')
    path('order', views.order, name='order'),]

- next we need to let settings know that this app exists and add paths for home & order to views.py

- settings.py =>

  - add ['pizza'] to [installed_apps]
  - update timezone variable to ['est']

- inside of pizza folder create paths and files
  [/templates/pizza/home.html][/templates/pizza/order.html]

# - update urls & settings & views.py

- home.html
  - add title and href to order page
- order.html
  - add title and href to home page

* debugged 2 errors
  - 1st - views.py =>
    - forgot to wrap url in ''
  - 2nd - urls.py =>
    - forgot to add order to path instead of just "" aka empty string

- order.html =>
  - add 2 topping fields
  - 1 option field (3 options small, medium, large)

# - order.html => add fields for toppings and size choices
