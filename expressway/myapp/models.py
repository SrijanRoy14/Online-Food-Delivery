from django.db import models
import json

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    subject=models.TextField()
    message=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Contact Table'

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='menu_images/')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    category=models.ManyToManyField('Category',related_name='item')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class ordermodel(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    items=models.ManyToManyField('MenuItem',related_name='order',blank=True,)
    name=models.CharField(max_length=50,blank=True)
    email=models.CharField(max_length=100,blank=True)
    street=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=50,blank=True)
    state=models.CharField(max_length=50,blank=True)
    zip_code=models.IntegerField(null=True,blank=True)
    num=models.CharField(max_length=200,blank=True,null=True)

    def set_num(self,lst):
        self.num=json.dumps(lst)
    
    def get_num(self):
        return json.loads(self.num)



    def __str__(self):
        return f"Order: {self.created_on.strftime('%b %d %I: %M %p')}"
    
class adminuser(models.Model):
    username=models.CharField(max_length=50,unique=True,blank=False)
    pwd=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True,blank=False)
    is_admin=models.BooleanField(default=True)
    class Meta:
        db_table="adminuser"