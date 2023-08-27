from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    num_ratings = models.IntegerField(default=0)
    # This function calculate average rating
    def average_rating(self):
        if self.num_ratings > 0:
            total_ratings = sum([rating.points for rating in self.ratings.all()])
            return total_ratings / self.num_ratings
        else:
            return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    points = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='ratings')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # This will calculate the average rating for the associated blog post
        blog_post = self.blog_post
        blog_post_ratings = blog_post.ratings.all()
        blog_post.num_ratings = blog_post_ratings.count()

        if blog_post.num_ratings > 0:
            total_ratings = sum([rating.points for rating in blog_post_ratings])
            blog_post.average_rating = total_ratings / blog_post.num_ratings
        else:
            blog_post.average_rating = 0

        blog_post.save()

    def __str__(self):
        return f"{self.user.username}'s Rating: {self.points}"


