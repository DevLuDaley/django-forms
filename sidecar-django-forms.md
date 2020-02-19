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

- order.html =>
  - add submit button

# - order.html => add order button

- order.html =>
  - update form action to point to 'order' page with a 'get' method

before hitting "order pizza" button http://127.0.0.1:8000/order?toping1=&toping2=&size=Small
after hitting "order pizza" button http://127.0.0.1:8000/order?toping1=Cheese&toping2=Pepperoni&size=Medium

'get' method displays and passes along info from the page
when should we use a 'get' method?
--whenever not changing anything on a website or you want something to be able to be referenced later.

we'll use a POST method instead...we only set up a 'get' initially as a test to see the data being passed.

error when hitting submit with 'post' instead of 'get'
[----Reason given for failure:

    CSRF token missing or incorrect.]

- order.html =>
  - add {% csrf_token %}
  - refresh the page and renter info

# - order.html => change 'get' to 'post' + add {% csrf_token %}

- forms.py =>

  - create [forms.py] inside the Pizza folder
  - create the [PizzaForm] class and add all 3 fields for toppings and size

- views.py =>
  [from .forms import PizzaForm]
  edit order method

before =>
def order(request):
return render(request, 'pizza/order.html')

after =>

          def order(request):
            form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform':forms})

order.html =>

[remove] =>
<label for="topping1">Topping 1: </label>
<input id="topping" type="text" name="toping1">

        <label for="topping2">Topping 2: </label>
        <input id="topping" type="text" name="toping2">

        <label for="size">Size: </label>
        <select id="size" name="size">
            <option value="Small">Small</option>
            <option value="Medium">Medium</option>
            <option value="Large">Large</option>
        </select>

[leave] =>

  <h1>Order a Pizza</h1>
  <form action="{% url 'order' %}" method="post">
      {% csrf_token %}

      <input type="submit" value="Order Pizza">

  </form>
  <a href="{% url 'home' %}">return to homepage</a>

    - add {{ pizzaform }}

# - create forms.py + PizzaForm & update views.py and order.html

- create [setup_data] branch
  ▶
  git checkout setup_data

# - git checkout setup_data

add logic for POST

order.html =>

- add <h2>{{ note }}</h2>
- change [form] to [new_form] 2 instances so do this twice
- declare [new_form=""] before calling it
- declare [note=""] before calling it
- add .capitalize() to topping1 & topping2

# - views.order() => add logic to validate data as cleaned_data + {{note}} for succesful order placed

models.py =>

- create Size and Pizza classes
- use **str**(self) to display title of models in form and admin panel.

- Size uses Foreign Key and must cascade

CASCADE = if one thing is deleted we will also delete the object that has that relationship (? research this more)

admin.py
import Pizza, Size
register 2 new models (Pizza, Size)

- [admin.site.register(Pizza)]
- [admin.site.register(Size)]

# - models.py && admin.py => create 2 models && register new models - Pizza/Size

▶
cd projectnandiasgarden
▶
python manage.py makemigrations
▶
python manage.py migrate

# - migrate models to db =>

▶
python manage.py createsuperuser
Username (leave blank to use 'lhd'): admin_django_forms
Email address:
password
Superuser created successfully.

# - create superuser =>

# - refactor: from form to django ModelForm + update spacing in topping labels

current place = chapter2 video3 'working with wigets'

python now points to env_pizza via the bottom left hand corner.

# - blank.py =>

# - customize using wigets blank.py =>

# - blank.py =>

▶
