from .models import Category, Product


def get_categories(request):
    categorieschild = Category.objects.filter(parent__isnull=True)
    return {'categorieschild': categorieschild}


def get_products(request):
    productsall = Product.objects.all()
    return {'productsall': productsall}
