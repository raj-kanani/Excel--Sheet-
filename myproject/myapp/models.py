from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, help_text='enter your unique mail-id')
    age = models.IntegerField(default=18)
    roll = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'myapp_student'
