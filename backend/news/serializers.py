from pathlib import Path

from rest_framework import serializers

from .models import CategoryTerritory, Image, News, NewsMaterial


class NewsMaterialSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True, required=True)
    territory = serializers.CharField(write_only=True, required=True)
    category_value = serializers.CharField(
        source="category_territory.category",
        read_only=True,
    )
    territory_value = serializers.CharField(
        source="category_territory.territory",
        read_only=True,
    )

    class Meta:
        model = NewsMaterial
        fields = [
            "id",
            "category",
            "territory",
            "category_value",
            "territory_value",
            "event_description",
            "source",
            "received_at",
            "event_place",
            "material_author",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "category_value", "territory_value"]

    def validate(self, attrs):
        required_fields = [
            "event_description",
            "source",
            "category",
            "territory",
            "material_author",
        ]
        for field in required_fields:
            if not attrs.get(field):
                raise serializers.ValidationError({field: "Это поле обязательно."})
        return attrs

    def create(self, validated_data):
        category = validated_data.pop("category")
        territory = validated_data.pop("territory")
        category_territory, _ = CategoryTerritory.objects.get_or_create(
            category=category,
            territory=territory,
        )
        return NewsMaterial.objects.create(
            category_territory=category_territory,
            **validated_data,
        )


class NewsSerializer(serializers.ModelSerializer):
    news_material_id = serializers.PrimaryKeyRelatedField(
        source="news_material",
        queryset=NewsMaterial.objects.all(),
        write_only=True,
        required=True,
    )
    category = serializers.CharField(write_only=True, required=True)
    territory = serializers.CharField(write_only=True, required=True)
    category_value = serializers.CharField(
        source="category_territory.category",
        read_only=True,
    )
    territory_value = serializers.CharField(
        source="category_territory.territory",
        read_only=True,
    )

    class Meta:
        model = News
        fields = [
            "id",
            "news_material_id",
            "news_material",
            "category",
            "territory",
            "category_value",
            "territory_value",
            "title",
            "text",
            "author",
            "tag",
            "status",
            "saved_at",
            "remarks",
        ]
        read_only_fields = [
            "id",
            "news_material",
            "status",
            "saved_at",
            "category_value",
            "territory_value",
        ]

    def validate(self, attrs):
        required_fields = [
            "news_material",
            "title",
            "text",
            "category",
            "territory",
            "author",
        ]
        for field in required_fields:
            if not attrs.get(field):
                raise serializers.ValidationError({field: "Это поле обязательно."})
        return attrs

    def create(self, validated_data):
        category = validated_data.pop("category")
        territory = validated_data.pop("territory")
        category_territory, _ = CategoryTerritory.objects.get_or_create(
            category=category,
            territory=territory,
        )
        return News.objects.create(
            category_territory=category_territory,
            status="prepared",
            **validated_data,
        )


class NewsImageSerializer(serializers.ModelSerializer):
    news_id = serializers.PrimaryKeyRelatedField(
        source="news",
        queryset=News.objects.all(),
        write_only=True,
        required=True,
    )
    image = serializers.ImageField(write_only=True, required=True)
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "id",
            "news_id",
            "news",
            "image",
            "file_name",
            "format",
            "file_path",
            "file_url",
            "added_at",
        ]
        read_only_fields = [
            "id",
            "news",
            "file_name",
            "format",
            "file_path",
            "file_url",
            "added_at",
        ]

    def validate_image(self, value):
        extension = Path(value.name).suffix.lower().replace(".", "")
        allowed_extensions = ["jpeg", "jpg", "png"]
        if extension not in allowed_extensions:
            raise serializers.ValidationError(
                "Формат изображения должен быть JPEG, JPG или PNG."
            )
        return value

    def create(self, validated_data):
        uploaded_image = validated_data.pop("image")
        extension = Path(uploaded_image.name).suffix.lower().replace(".", "")
        return Image.objects.create(
            file_name=uploaded_image.name,
            format=extension,
            file_path=uploaded_image,
            **validated_data,
        )

    def get_file_url(self, obj):
        request = self.context.get("request")
        if obj.file_path and request:
            return request.build_absolute_uri(obj.file_path.url)
        if obj.file_path:
            return obj.file_path.url
        return None
