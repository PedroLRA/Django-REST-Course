from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    doc_rg = models.CharField(max_length=9)
    doc_cpf = models.CharField(max_length=11, unique=True)
    birth = models.DateField()
    phone_number = models.CharField(max_length=11, default='')
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    
    # Apllying common ordering
    class Meta:
        ordering = ['id']

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1,
        choices=LEVEL,
        blank=False,
        null=False,
        default='B'
    )

    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ['id']
    
class Enrollment(models.Model):
    SHIFT = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
    )

    # The tag models.CASCADE is used to delete the enrollment when the student
    # or course related with this enrollment is deleted
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    shift = models.CharField(
        max_length=1,
        choices=SHIFT,
        blank=False,
        null=False,
        default='M'
    )

    class Meta:
        ordering = ['id']