from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryTerritory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=100)),
                ("territory", models.CharField(max_length=100)),
            ],
            options={
                "unique_together": {("category", "territory")},
            },
        ),
        migrations.CreateModel(
            name="NewsMaterial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_description", models.TextField()),
                ("source", models.CharField(max_length=255)),
                ("received_at", models.DateTimeField(blank=True, null=True)),
                ("event_place", models.CharField(blank=True, max_length=255)),
                ("material_author", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category_territory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news_materials",
                        to="news.categoryterritory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("text", models.TextField()),
                ("author", models.CharField(max_length=150)),
                ("tag", models.CharField(blank=True, max_length=100)),
                ("status", models.CharField(default="prepared", max_length=50)),
                ("saved_at", models.DateTimeField(auto_now_add=True)),
                ("remarks", models.TextField(blank=True)),
                (
                    "category_territory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news",
                        to="news.categoryterritory",
                    ),
                ),
                (
                    "news_material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="news",
                        to="news.newsmaterial",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file_name", models.CharField(max_length=255)),
                ("format", models.CharField(max_length=10)),
                ("file_path", models.ImageField(upload_to="news_images/")),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="news.news",
                    ),
                ),
            ],
        ),
    ]
