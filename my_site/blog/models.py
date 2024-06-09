from django.db import models

# Create your models here.


class Tag(models.Model):
    captions = models.CharField(max_length=20)

    def __str__(self):
        return self.captions


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=254)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False,
                            blank=True,
                            unique=True)

    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True,
                               related_name="posts")
    tags = models.ManyToManyField(Tag)

    content = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(null=True)
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")

    def __str__(self):
        user_name = self.user_name
        return user_name.capitalize()
