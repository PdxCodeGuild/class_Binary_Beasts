This guide covers the content in the folder **Model**

## What is a model?

A model is a representation of your object in the database. Django uses by default a relational database such as SQL lite. A relational database is organized into tables where data is stored in [key-value pairs](https://content.codecademy.com/courses/sql-intensive/table.jpg)


There are different ways to define a relationship between elements in the database:

- `OneToOneField` represents a [one-to-one relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/one_to_one/)
- `ForeignKey` represents a [many-to-one relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/)
- `ManyToManyField` represents a [many-to-many relationship](https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/)



1) `Many-to-one relationships`. This can be the relationship between a car manufacturer and a car. A manufacturer can build different cars. But all the cars have one manufacturer in common.

```python

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

```

2) `Many-to-many relationships`. For example, a Pizza has multiple Topping objects. A Topping can be on multiple pizzas and each Pizza has multiple toppings – here’s how you’d represent that:

```python

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```

3) `One-to-one relationships`  A OneToOneField would be like an Engine, where a Car object can have one and only one engine.`

```python
class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine)

    def __unicode__(self):
        return self.name

```

Check [this video](https://www.youtube.com/watch?v=wIPHER2UBB4&t=61s) for a more visual explanation of the models.


## Create your model

Go to the your app folder and inside the models.py file add a model. The following is an example of a **many to one** relationship model:

```python
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        pub_date = models.DateField()
        user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

        def __str__(self):
            return self.title
```

- Stage your migrations: `python manage.py makemigrations <appname>`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

2. Create superuser

- run `python manage.py createsuperuser`

3. The shell

 Learn more about making queries [here](https://docs.djangoproject.com/en/3.1/topics/db/queries/) and [here](https://docs.djangoproject.com/en/3.1/topics/db/queries/)

- In the terminal run `python manage.py shell`
- run `from my_app.models import Blog`
- run `Blog`, you should be returned a class
- run `Blog.objects.all()`, to see the content of your database. You should see `<QuerySet []>` if empty

Create a few entries:

- run `Blog.objects.create(title='I made my kittens bark', text='lorem ipsum', pub_date='2009-11-12')`
- run `Blog.objects.create(title='The economy of the 20th century', text='another lorem ipsum', pub_date='2020-01-12')`

Filtering:

- run `Blog.objects.filter(title = 'I made my kittens bark')`
- run `Blog.objects.filter(id = 1)`
- run `Blog.objects.filter(title__startswith='I made')`

- run `a = Blog.objects.all()` to assign all posts to a variable
- run `a` to see all blog posts
- run `a[0]` to access the first element
- run `a[0].delete()` to delete the first element


## Part 4. Superuser

Exit the shell typing `exit()`. Let's discover the Admin panel and see all the blog posts that we have created. In my_app > admin.py page add the following:

```python
from django.contrib import admin

from . import models

admin.site.register(models.Blog)

```
- In the terminal, start the server and run `python manage.py runserver`
- run `python manage.py createsuperuser`
- Go to` http://localhost:8000/admin/` to explore the page and add more blog posts.