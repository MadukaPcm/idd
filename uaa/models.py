from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator
# from django.utils.translation import gettext as _
from django.conf import settings
from django.core.validators import RegexValidator
import uuid


# from uuidfield import UUIDField
class REgisterdMember(models.Model):
      id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
      regNo = models.CharField(max_length=25,blank=False,null=True)
      
      createdAt = models.DateField(auto_now_add=True)
      updatedAt = models.DateField(auto_now=True)
      
      class Meta: 
            ordering = ['-createdAt']
      
      def __str__(self):
          return str(self.regNo)
      
      
class User(AbstractUser):
      email = models.EmailField(_('email address'), unique = True)
      nida_no = models.CharField(max_length=25, null=True, blank=True, unique=True)
      phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+255-000-000-000' ")
      phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True,null=True)
      dob = models.DateField(null=True,blank=True)
      gender = models.CharField(max_length=6,blank=True,null=True)
      profileImage = models.FileField(upload_to='profileImages', validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])],null=True,blank=True)
      
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username','first_name','last_name']

      def __str__(self):
        return "{}".format(self.email)
      
      # Dealing with image.
      # def save(self, *args, **kwargs):
      #       super().save(*args, **kwargs)

      #       if self.profileImage:
      #         profileImage = Image.open(self.profileImage.path)
              
      #         if profileImage.height > 1500 or profileImage.width > 1500:
      #             output_size = (1500, 1500)
      #             profileImage.thumbnail(output_size)
      #             profileImage.save(self.profileImage.path)
      
      
class DailyTip(models.Model):
      id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
      content = models.CharField(max_length=255,blank=True,null=True)
      createdBy = models.CharField(max_length=20,blank=True,null=True)
      
      createdAt = models.DateField(auto_now_add=True)
      updatedAt = models.DateField(auto_now=True)
      
      class Meta: 
            ordering = ['-createdAt']
          
      def __str__(self):
          return str(self.createdBy)
      
  