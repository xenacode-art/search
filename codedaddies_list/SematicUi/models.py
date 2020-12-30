from django.db import models

# Create your models here.
class Active_item(models.Model):
  home= models.CharField(max_length = 500)
  created = models.DateTimeField(auto_now = True)
  company =models.TextField(max_length=500)
  career = models.TextField(max_length=500)
  login = models.CharField(max_length=500),
  list_display={'name','password'}
  sign_up = models.CharField(max_length=500),
  list_display = {'name','password'}
  def __str__(self):
   return '{}'.format(self.home-page)


   class Meta:
    vearbose_name_plural = "Searches"