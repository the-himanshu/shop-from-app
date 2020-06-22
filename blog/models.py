from django.db import models

# Create your models here.
class Blogpost(models.Model):
    blogpost_id = models.AutoField
    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    head3 = models.CharField(max_length=500, default="")
    chead3 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.title
