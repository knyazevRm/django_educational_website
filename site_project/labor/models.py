from django.db import models
# Create your models here.


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    sex = models.CharField(max_length=6)
    expected_salary = models.IntegerField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return "ID: {}, Name: {}".format(self.id, self.first_name)

    class Meta:
        managed = False


class Post(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "ID: {}, Title: {}".format(self.id, self.title)

    class Meta:
        managed = False


class Education(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "ID: {}, Title: {}".format(self.id, self.title)

    class Meta:
        managed = False


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    employer = models.ForeignKey('Employer', on_delete=models.CASCADE)
    type_of_education = models.ForeignKey('Education', on_delete=models.CASCADE)
    salary = models.IntegerField()
    remote_work = models.BooleanField()
    creation_date = models.DateField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return "ID: {}, Title: {}".format(self.id, self.title)

    class Meta:
        managed = False


class Activity(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return "ID: {}, Title: {}".format(self.id, self.title)

    class Meta:
        managed = False


class Employer(models.Model):
    title = models.CharField(max_length=255)
    type_of_activity = models.ForeignKey('Activity', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)

    def __str__(self):
        return "ID: {}, Title: {}".format(self.id, self.title)

    class Meta:
        managed = False