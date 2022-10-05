from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    categoryName = models.CharField(max_length=20,blank=True,null=True)
    createdBy = models.CharField(max_length=20,blank=True,null=True)
    
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
            ordering = ['-createdAt']
    
    def __str__(self):
        return self.categoryName
    

class Book(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    categoryId = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name="category",blank=True,null=True)
    createdBy = models.CharField(max_length=20,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    author = models.CharField(max_length=50,blank=True,null=True)
    isbn = models.CharField(max_length=50,blank=True,null=True)
    publisher = models.CharField(max_length=50,blank=True,null=True)
    placeOfPublication = models.CharField(max_length=60,blank=True,null=True)
    yearOfPublication = models.CharField(max_length=50,blank=True,null=True)
    coverPageImage = models.FileField(upload_to='coverPageImages', validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    description = models.CharField(max_length=255,blank=True,null=True)      
    
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta: 
        ordering = ['-createdAt'] 
    
    def __str__(self):
        return self.title
    
    
class RequestedBook(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    userId = models.CharField(max_length=255,null=True,blank=True)
    bookId = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="book",blank=True,null=True)
    issueDate = models.DateField()
    dueDate = models.DateField()
    status = models.BooleanField(default=True)
    isApproved = models.BooleanField(default=False)
    isPending = models.BooleanField(default=True)
    isTaken = models.BooleanField(default=False)
    isREturned = models.BooleanField(default=False)
    
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    class Meta: 
        ordering = ['-createdAt'] 
    
    def __str__(self):
        return str(self.bookId.title)
    
    
        
    