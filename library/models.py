from django.db import models


class Books(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('not_available', 'Not Available'),
    ]

    title = models.CharField(max_length=225)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_stock'
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-year']

