from django.db import models


class Todo(models.Model):
    title= models.CharField(max_length= 1000, unique= True)
    completed= models.BooleanField(default= False)
    date_created= models.DateTimeField(auto_now_add= True)


    class Meta:
        verbose_name= 'Todo'
        verbose_name_plural= 'Todos'
        ordering= ['-id']


    def __str__(self):
        return self.title



