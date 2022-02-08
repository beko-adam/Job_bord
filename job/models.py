from django.db import models
from django.utils.text import slugify

# Create your models here.

TYPE_JOB = (
            ('full time', 'Full Time'),
            ('Part time', 'Part Time'),
            )
class Job(models.Model):
    
    title = models.CharField(max_length=100)
    Type_job = models.CharField(max_length=15, choices=TYPE_JOB )
    descrption = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience =  models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField( upload_to='jobs')
    slug = models.SlugField(null=True, blank=True)

    #for chane urls name to str
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):

        return self.name



# modle for get data from Apply form

class Apply(models.Model):

    job_link= models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webside = models.URLField()
    cv = models.FileField(upload_to='Apply/')
    cover_letter = models.TextField(max_length=500)
    create_at = models.DateField(auto_now=True)

    def __str__(self):

        return self.name
        

    