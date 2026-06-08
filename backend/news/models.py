from django.db import models


class CategoryTerritory(models.Model):
    category = models.CharField(max_length=100)
    territory = models.CharField(max_length=100)

    class Meta:
        unique_together = ("category", "territory")

    def __str__(self):
        return f"{self.category} / {self.territory}"


class NewsMaterial(models.Model):
    category_territory = models.ForeignKey(
        CategoryTerritory,
        on_delete=models.CASCADE,
        related_name="news_materials",
    )
    event_description = models.TextField()
    source = models.CharField(max_length=255)
    received_at = models.DateTimeField(null=True, blank=True)
    event_place = models.CharField(max_length=255, blank=True)
    material_author = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_description[:80]


class News(models.Model):
    news_material = models.ForeignKey(
        NewsMaterial,
        on_delete=models.CASCADE,
        related_name="news",
    )
    category_territory = models.ForeignKey(
        CategoryTerritory,
        on_delete=models.CASCADE,
        related_name="news",
    )
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=150)
    tag = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, default="prepared")
    saved_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="images",
    )
    file_name = models.CharField(max_length=255)
    format = models.CharField(max_length=10)
    file_path = models.ImageField(upload_to="news_images/")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
