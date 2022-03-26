from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=1024, blank=False, verbose_name = "Tên sản phẩm")
    create_at = models.DateTimeField(auto_now_add = True, verbose_name="Create at") #update time or create time

# For a Detail Product
    def to_json_fomat(self):
        return {
            'name': self.name,
        }
    # For all Products
    def to_dict(self):
        return{
            'name': self.name,
            'id': self.id
        }
# return product with amount and discount
    # def get_product(self):
    #     amount = Amount.objects.filter(product = self)
    #     discount = Discount.objects.filter(product = self)

    #     data = {
    #         'id': self.id,
    #         'name': self.name,
    #         'amount': amount
    #     }

    class Meta:
        verbose_name ="Product"
        verbose_name_plural ="Products"
        db_table = "product"

    def __str__(self):
        return self.name

class Discount(models.Model):
    product = models.ForeignKey(Product, null= False, blank= False, verbose_name="Product", related_name='child_media', on_delete=models.CASCADE)
    discount_32b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 32 tỷ")
    discount_16b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 16 tỷ")
    discount_8b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 8 tỷ")
    discount_4b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 4 tỷ")
    discount_2b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 2 tỷ")
    discount_1b = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 1 tỷ")
    discount_500m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu  500tr")
    discount_300m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 300tr")
    discount_150m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 150tr")
    discount_60m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 60tr")
    discount_30m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 30tr")
    discount_10m = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Chiết khấu 10tr")
    create_at = models.DateTimeField(auto_now_add = True, verbose_name="Create at")

    # For a Detail Product
    def to_json_fomat(self):
        return {
            'discount_32b': self.discount_32b,
            'discount_16b': self.discount_16b,
            'discount_8b': self.discount_8b,
            'discount_4b': self.discount_4b,
            'discount_2b': self.discount_2b,
            'discount_1b': self.discount_1b,
            'discount_500m': self.discount_500m,
            'discount_300m': self.discount_300m,
            'discount_150m': self.discount_150m,
            'discount_60m': self.discount_60m,
            'discount_30m': self.discount_30m,
            'discount_10m': self.discount_10m,
        }

    class Meta:
        verbose_name ="Discount"
        verbose_name_plural = "Discounts"
        db_table = "discount"

    def __str__(self):
        return "%s" % (self.product.name)
    def __unicode__(self):
        return "%s" % (self.product.name)

# Price of Amount
class Amount(models.Model):
    name = models.CharField(max_length=1024, blank=False, verbose_name = "Tên giá")
    product = models.ManyToManyField(Product,verbose_name="Sản phẩm")
    price_of = models.DecimalField(max_digits = 16, decimal_places = 2, default = 0, verbose_name="Giá ứng với số lượng")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name = "Ngày tạo")

    def to_dict(self):
        return {
            self.name: self.price_of,
        }

    def get_products(self):
        return ",".join([str(p) for p in self.product.all()])

    # def get_amount(self):
    #     return {
    #         self.name : self.price_of
    #     }

    class Meta:
        verbose_name = "Amount"
        verbose_name_plural = "Amounts"
        db_table = "amount"
    def __str__(self):
        return self.name

    def __unicode__(self):
        return 
