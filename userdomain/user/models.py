from django.db import models

class User(models.Model):
    username = models.CharField(max_length= 50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
    def __str__(self):
        return self.username

