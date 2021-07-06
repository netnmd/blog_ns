from django.db import models
from django.conf import settings


class Category(models.Model):
    """Post's category"""
    
    title = models.CharField(verbose_name="Post Category", max_length=50)

    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Post's tags"""

    title = models.CharField(verbose_name="Tag", max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Blog Post"""

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    TYPE_CHOICES = (
        ("forum", "Forum"),
        ("blog", "Blog")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=100)
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.SET_NULL,
        null=True
    )
    slug = models.SlugField(
        verbose_name="Post URL",
        max_length=150,
        unique=True,
        default=""
    )
    post_img = models.ImageField(
        verbose_name="Post IMG",
        upload_to="blog/%Y/%m/%d/",
        blank=True,
        # null=True ????
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=150,
        blank=True
    )
    text = models.TextField(verbose_name="Text")
    tag = models.ManyToManyField(Tag, verbose_name="Tag", blank=True)
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated time",
        auto_now=True
    )
    views_count = models.PositiveIntegerField(verbose_name="Views count", default=0)
    likes_count = models.PositiveIntegerField(verbose_name="Likes count", default=0)
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=50)
    post_type = models.CharField(choices=TYPE_CHOICES, default="forum", max_length=50)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
