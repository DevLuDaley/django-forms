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
\$ - do this so that local git knows about the new branch ('django-setup') created in remote git/GitHub
▶
git checkout setup_django
▶
pip install django

\$

# - install django

▶ django-admin startproject nandiasgarden

# - create project + folder

▶ mv nandiasgarden/ projectnandiasgarden
(tutorial says nandiasgarden-project but "name-project" is an invalid proj name in py 3.8)
rename project folder. add project to start of the name i.e folder => projectfolder or projectnandiasgarden for this project

this helps differentiate between the project folder and the autogenerate folder (with the identaical project name) that lives in the project folder

# - rename project folder
