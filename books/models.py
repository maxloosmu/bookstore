from django.db import models

# Create your models here.
class Book(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  published = models.DateField()
  pages = models.IntegerField()
  price = models.IntegerField()
  description = models.TextField()
  image = models.ImageField(upload_to='book_images/')
  
  def __str__(self):
    return str(self.id) + ' - ' + self.name
