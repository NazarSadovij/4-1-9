from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    likes_count = models.IntegerField()
    user_email = models.EmailField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        db_table = "testingsssssss_posts"
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        unique_together = (("title", "user_email"), )
        indexes = [models.Index(fields=["title", "user_email"]),]