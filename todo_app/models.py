from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    todo_text = models.CharField( max_length=100,null=False)
    todo_status = models.CharField(max_length=10,default='Not Done')

    def __str__(self) -> str:
        return self.todo_text