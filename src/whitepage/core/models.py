from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user                  = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user               = models.IntegerField()
  bio                   = models.TextField(blank=True, max_length=255)
  profile_img           = models.ImageField(upload_to='profile_images', default='app/blank-profile-picture.png')
  location              = models.CharField(max_length=100, blank=True)
  is_coorporate         = models.BooleanField(default=False)
  #! if is_coorporate
  coorporate_approved   = models.BooleanField(default=False)
  company_name          = models.CharField(max_length=100)
  business_field        = models.CharField(max_length=100)
  
  def __str__(self):
    return self.user.username