from django.db import models

#   Create your models here.


class TStat14(models.Model):
    province = models.CharField(max_length=200)
    all = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    ii = models.IntegerField(default=0)
    iii = models.IntegerField(default=0)
    iv = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    vi = models.IntegerField(default=0)
    vii = models.IntegerField(default=0)
    viii = models.IntegerField(default=0)
    ix = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    xi = models.IntegerField(default=0)
    xii = models.IntegerField(default=0)
#   pub_date = models.DateTimeField('date published')

    def __str__(self):
       return "Województwo: " + self.province + " Ilość:" + str(self.all)


class TStat15(models.Model):
    province = models.CharField(max_length=200)
    all = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    ii = models.IntegerField(default=0)
    iii = models.IntegerField(default=0)
    iv = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    vi = models.IntegerField(default=0)
    vii = models.IntegerField(default=0)
    viii = models.IntegerField(default=0)
    ix = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    xi = models.IntegerField(default=0)
    xii = models.IntegerField(default=0)

    def __str__(self):
        return self.province + " " + str(self.all)


class TStat16(models.Model):
    province = models.CharField(max_length=200)
    all = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    ii = models.IntegerField(default=0)
    iii = models.IntegerField(default=0)
    iv = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    vi = models.IntegerField(default=0)
    vii = models.IntegerField(default=0)
    viii = models.IntegerField(default=0)
    ix = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    xi = models.IntegerField(default=0)
    xii = models.IntegerField(default=0)

    def __str__(self):
        return self.province + " " + str(self.all)


class TStat17(models.Model):
    province = models.CharField(max_length=200)
    all = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    ii = models.IntegerField(default=0)
    iii = models.IntegerField(default=0)
    iv = models.IntegerField(default=0)
    v = models.IntegerField(default=0)
    vi = models.IntegerField(default=0)
    vii = models.IntegerField(default=0)
    viii = models.IntegerField(default=0)
    ix = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    xi = models.IntegerField(default=0)
    xii = models.IntegerField(default=0)

    def __str__(self):
        return self.province + " " + str(self.all)
