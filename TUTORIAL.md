# **My Tutorial:**

---

## 1. Templates
![01_templates.png](_tutorial_img%2F01_templates.png)

---
## 2. Forms and User Input
![02_added_form.png](_tutorial_img%2F02_added_form.png)

![02_tree_project.png](_tutorial_img%2F02_tree_project.png)

##### added:
* forms.py
* 
* login.html
* register.html
* messages.html


---

## 3. Database create, SQLAlchemy

```
from web import create_app
app = create_app()
from app import db
from app.auth.models import User, Post
with app.app_context():
    db.create_all()

```

![03_db.png](_tutorial_img%2F03_db.png)


---

## 4. Login - Auth

![04_auth_account.png](_tutorial_img%2F04_auth_account.png)

---

## 5. Account Page

![05_profile_user.png](_tutorial_img%2F05_profile_user.png)


---

## 6. Post

![06_added_post.png](_tutorial_img%2F06_added_post.png)







-------------------------------
---

#### **Notes:**

* pip freeze > requirements.txt
* pip install -r requirements.txt

---
### **Links:**
##### Bootstrap icon:
-  https://getbootstrap.com/docs/3.3/components/
-  https://www.w3schools.com/bootstrap/bootstrap_ref_comp_glyphs.asp
-  
##### Bootstrap container:
- https://getbootstrap.ru/docs/v4-alpha/layout/grid/
-  
##### atabase SQLAlchemy:
- https://testdriven.io/courses/flask-celery/app-factory/
- https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#step-5-adding-flask-sqlalchemy-models-to-your-flask-application
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
- https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask
---
