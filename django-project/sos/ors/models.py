from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user'


class mark(models.Model):
    firstName = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)
    studentId = models.CharField(max_length=20)
    physics = models.CharField(max_length=20)
    chemistry = models.CharField(max_length=50)
    maths = models.CharField(max_length=50)

    class Meta:
      db_table = 'marksheet'
