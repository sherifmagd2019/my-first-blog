from django.db import models
from django.urls import reverse
from django.db.models.fields import DateTimeField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from users.models import Department

class Organiztion(models.Model):
    name = models.TextField()    
    
    def __str__(self):
        return models.Model.__str__(self)

 

 

class Post(models.Model):
    POST_IN = 'I'
    POST_OUT = 'O'
    
    POST_CHOICES = (
        (POST_IN, 'وارد'),
        (POST_OUT, 'صادر'),
     
    )
    title = models.CharField(max_length=255 ,verbose_name ='عنوان' )
   
    departments = models.ManyToManyField( 'users.Department' ,related_name='posts'  ,verbose_name ='توجيه')
    body = models.TextField( verbose_name ='الموضوع')
    in_number = models.IntegerField(  null=True,blank=True,verbose_name ='رقم وارد')
    in_date = models.DateTimeField( null=True,blank=True,verbose_name ='تاريخ وارد')
    out_number = models.IntegerField(null=True,blank=True,verbose_name ='رقم صادر')
    out_date = DateTimeField(null=True,blank=True,verbose_name ='تاريخ صادر')
    
      
    post_flag = models.CharField(
        max_length=1,
        choices=POST_CHOICES,
        default=POST_IN,null=True,blank=True,verbose_name ='نوع المخاطبة'
    )
    
    otherpost = models.ForeignKey('Post', on_delete=CASCADE ,null=True,blank=True ,verbose_name ='ربط')
    #12 dec 2010 
    files = models.FileField(null=True,blank=True,verbose_name ='ملف')
    
    # = models.ManyToManyField("self") 
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

