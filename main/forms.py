from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock"]


# model = News untuk menunjukkan model yang akan digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek News.
# fields = ["title", "content", "category", "thumbnail", "is_featured"] untuk menunjukkan field dari model News yang digunakan untuk form. Field created_at dan news_views tidak dimasukkan ke list fields karena ditambahkan secara otomatis.