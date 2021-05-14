from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    city = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name


# test = Student.objects.all()
# print(test)
# for i in test:
#     print(i)
