from mcp_server import ModelQueryToolset
from catalog.models import Category, Product

class CategoryQueryTool(ModelQueryToolset):
  model = Category
  extra_instructions = (
  "Category means ชนิดของสินค้า"
  )

class ProductQueryTool(ModelQueryToolset):
  model = Product