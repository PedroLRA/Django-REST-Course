# Introduction

This project was developed during Alura's "Django REST APIs: create REST applications with Python" training.

# Course goals

During the course and the development of the application, the following topics were covered:

- How to create an API using Django REST Framework
- Use Django Admin with the API
- Serialization and validation of fields
- User permissions and throttling
- API versioning
- API internationalization
- Automated testing
- API documentation with Swagger
- Integration with Postman for testing

# Running the API

### 1. clone the repository from Github.

To clone using `ssh`, you can use the following command:

```sh
$ git clone git@github.com:PedroLRA/Django-REST-Course.git
```

Or, if you prefer to use `HTTPS`:

```sh
$ git clone https://github.com/PedroLRA/Django-REST-Course.git
```    

### 2. Change to the new directory where the project was cloned:

```sh
$ cd Django-REST-Course
```

### 3. Install project dependencies:

```sh
$ pip install -r requirements.txt
```

### 4. Configure the `.env` file.

In this step, you will need to change the value `<YOUR_SECRET_KEY>` to yours and remove the `.example` from the file name.

To obtain a django secret key, you can run the following code using python:

```py
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

### 5. Apply the migrations:

```sh
$ python manage.py migrate
```    

### 6. Compile the messages:

```sh
$ python manage.py compliemessages
```

### 7. Create a superuser

```sh
python manage.py createsuperuser
```

### 8. Finally, run the API:

```sh
$ python manage.py runserver
```

Now the API is already running in your localhost and you can access it on http://localhost:8000/.

---
---

<div style="text-align: right;">
  This project was developed for learning purposes.
  
  If you have any tips to improve the code, feel free to submit them as issues. I would ❤️ to see it.
</div>
