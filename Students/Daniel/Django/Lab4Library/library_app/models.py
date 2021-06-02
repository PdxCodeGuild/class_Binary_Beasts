from django.db import models



class Book(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateField()
    author = models.ForeignKey('Author', on_delete = models.CASCADE, null = True, blank = True)
    available = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    author = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.author

class History(models.Model):
    book = models.CharField(max_length = 200)
    user = models.CharField(max_length = 200)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return (f"{self.book} {self.user} {self.checkout} {self.timestamp}")
