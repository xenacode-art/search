from django.db import models

# Create your models here.
class Register(models.Model):
  created = models.DateTimeField(auto_now = True)
  company =models.CharField(max_length=250)
  career = models.TextField(max_length=250) 
  #def __str__(self):
 #  return '{}'.format(self.SematicUi)


#class Meta:
 #   vearbose_name_plural = "Registers"
