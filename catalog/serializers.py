from rest_framework import serializers
from catalog.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField()
  item_count = serializers.SerializerMethodField()
  def get_item_count(self, obj):
    return obj.products.all().count()

  def create(self, validated_data):
    return Category.objects.create(**validated_data)

  class Meta:
    model = Category
    # fields = ['id', 'name', 'description', 'item_count']
    fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  class Meta:
    model = Product
    fields = '__all__'