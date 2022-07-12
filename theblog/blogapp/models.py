from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        
        return str(self.name)

        #After publish show published article 
    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic =models.ImageField(upload_to="images/profile",default="static/theblog/images/default_pic.png")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    insta_url = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True,upload_to="images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_post', default=None, blank=True)
    category = models.CharField(max_length=200, default=None)


    def total_likes(self):
        return self.likes.all().count()

    def __str__(self):
    	
        return self.title+' | ' + str(self.author)

        #After publish show published article 
    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    
    