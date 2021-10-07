# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addons(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    unique_identifier = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    activated = models.IntegerField()
    image = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addons'


class Addresses(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    alternate_phone = models.CharField(max_length=255, blank=True, null=True)
    set_default = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'addresses'


class AppSettings(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    currency_format = models.CharField(max_length=10, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    google_plus = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_settings'


class AttributeTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attribute_translations'


class Attributes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'attributes'


class Banners(models.Model):
    photo = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    position = models.IntegerField()
    published = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'banners'


class BlogCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_categories'


class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.IntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    banner = models.IntegerField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_img = models.IntegerField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'


class BrandTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brand_translations'


class Brands(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=100, blank=True, null=True)
    top = models.IntegerField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brands'


class BusinessSettings(models.Model):
    id = models.AutoField()
    type = models.CharField(max_length=30)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_settings'


class BusinessSettingsOldest(models.Model):
    id = models.IntegerField()
    type = models.CharField(max_length=30)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_settings_oldest'


class Carts(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    temp_user_id = models.CharField(max_length=255, blank=True, null=True)
    address_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    variation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    shipping_type = models.CharField(max_length=30)
    pickup_point = models.IntegerField(blank=True, null=True)
    discount = models.FloatField()
    coupon_code = models.CharField(max_length=255)
    coupon_applied = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carts'


class Categories(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    order_level = models.IntegerField()
    commision_rate = models.FloatField()
    banner = models.CharField(max_length=100, blank=True, null=True)
    thumbnail_banner = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    featured = models.IntegerField()
    top = models.IntegerField()
    digital = models.IntegerField()
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category_translations'


class Cities(models.Model):
    country_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField()
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities'


class CitiesFull(models.Model):
    name = models.CharField(max_length=191)
    state_id = models.IntegerField()
    mapped = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities_full'


class CityTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    city_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city_translations'


class ClubPointDetails(models.Model):
    club_point_id = models.IntegerField()
    product_id = models.IntegerField()
    product_qty = models.IntegerField()
    point = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'club_point_details'


class ClubPoints(models.Model):
    user_id = models.IntegerField()
    points = models.FloatField()
    order_id = models.IntegerField()
    convert_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'club_points'


class Colors(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colors'


class CommissionHistories(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    order_detail_id = models.IntegerField()
    seller_id = models.IntegerField()
    admin_commission = models.FloatField()
    seller_earning = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commission_histories'


class Conversations(models.Model):
    id = models.IntegerField(primary_key=True)
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    title = models.CharField(max_length=1000, blank=True, null=True)
    sender_viewed = models.IntegerField()
    receiver_viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conversations'


class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class CouponUsages(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon_usages'


class Coupons(models.Model):
    couponcode = models.CharField(db_column='couponCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discountamount = models.IntegerField(db_column='discountAmount', blank=True, null=True)  # Field name made lowercase.
    rulename = models.CharField(db_column='ruleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    validfrom = models.CharField(db_column='validFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    validto = models.CharField(db_column='validTo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    couponstatus = models.PositiveIntegerField(db_column='couponStatus', blank=True, null=True)  # Field name made lowercase.
    allowedpercustomer = models.IntegerField(db_column='allowedPerCustomer', blank=True, null=True)  # Field name made lowercase.
    usedpercustomer = models.IntegerField(db_column='usedPerCustomer', blank=True, null=True)  # Field name made lowercase.
    couponaddedon = models.CharField(db_column='couponAddedon', max_length=25, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupons'


class Currencies(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    countrycode = models.CharField(db_column='countryCode', max_length=255)  # Field name made lowercase.
    exchange_rate = models.FloatField()
    status = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerBulkOrder(models.Model):
    sendername = models.CharField(db_column='senderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sendermobile = models.CharField(db_column='senderMobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    senderemail = models.CharField(db_column='senderEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendermessage = models.TextField(db_column='senderMessage', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_bulk_order'


class CustomerPackagePayments(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    customer_package_id = models.IntegerField()
    payment_method = models.CharField(max_length=255)
    payment_details = models.TextField()
    approval = models.IntegerField()
    offline_payment = models.IntegerField()
    reciept = models.CharField(max_length=150)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_package_payments'


class CustomerPackageTranslations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_package_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_package_translations'


class CustomerPackages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    product_upload = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_packages'


class CustomerProductTranslations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_product_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_product_translations'


class CustomerProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    published = models.IntegerField()
    status = models.IntegerField()
    added_by = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    subsubcategory_id = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    photos = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_img = models.CharField(max_length=150, blank=True, null=True)
    conditon = models.CharField(max_length=50, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    video_provider = models.CharField(max_length=100, blank=True, null=True)
    video_link = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_img = models.CharField(max_length=150, blank=True, null=True)
    pdf = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_products'


class CustomerReview(models.Model):
    customername = models.CharField(db_column='customerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerphone = models.CharField(db_column='customerPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='customerEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    review_content = models.TextField(blank=True, null=True)
    customerrating = models.TextField(db_column='customerRating', blank=True, null=True)  # Field name made lowercase.
    celebrety_image = models.CharField(max_length=50, blank=True, null=True)
    review_status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_review'


class CustomerSupport(models.Model):
    sendername = models.CharField(db_column='senderName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendermobile = models.CharField(db_column='senderMobile', max_length=25, blank=True, null=True)  # Field name made lowercase.
    senderemail = models.CharField(db_column='senderEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sendermessage = models.TextField(db_column='senderMessage', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_support'


class CustomerTestimonials(models.Model):
    customername = models.CharField(db_column='customerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeremail = models.CharField(db_column='customerEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customermobile = models.CharField(db_column='customerMobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customertestimonial = models.TextField(db_column='customerTestimonial', blank=True, null=True)  # Field name made lowercase.
    profilepicture = models.CharField(db_column='profilePicture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customerrating = models.IntegerField(db_column='customerRating', blank=True, null=True)  # Field name made lowercase.
    testimonialstatus = models.CharField(db_column='testimonialStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_testimonials'


class Customers(models.Model):
    user_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers'
        unique_together = (('id', 'user_id'),)


class Datas(models.Model):
    id = models.BigAutoField(primary_key=True)
    customername = models.CharField(db_column='customerName', max_length=191)  # Field name made lowercase.
    customerphone = models.CharField(db_column='customerPhone', max_length=191)  # Field name made lowercase.
    customeremail = models.CharField(db_column='customerEmail', max_length=191)  # Field name made lowercase.
    review_content = models.CharField(max_length=191)
    customerrating = models.CharField(db_column='customerRating', max_length=191)  # Field name made lowercase.
    celebrety_image = models.CharField(max_length=191)
    reviewcreated = models.CharField(db_column='reviewCreated', max_length=191)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datas'


class FlashDealProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    flash_deal_id = models.IntegerField()
    product_id = models.IntegerField()
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deal_products'


class FlashDealTranslations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    flash_deal_id = models.BigIntegerField()
    title = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deal_translations'


class FlashDeals(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    featured = models.IntegerField()
    background_color = models.CharField(max_length=255, blank=True, null=True)
    text_color = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flash_deals'


class GeneralSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    frontend_color = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    footer_logo = models.CharField(max_length=255, blank=True, null=True)
    admin_logo = models.CharField(max_length=255, blank=True, null=True)
    admin_login_background = models.CharField(max_length=255, blank=True, null=True)
    admin_login_sidebar = models.CharField(max_length=255, blank=True, null=True)
    favicon = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField()
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    twitter = models.CharField(max_length=1000, blank=True, null=True)
    youtube = models.CharField(max_length=1000, blank=True, null=True)
    google_plus = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'general_settings'


class HomeCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    subsubcategories = models.CharField(max_length=1000, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'home_categories'


class HsnCode(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    gst_till = models.CharField(db_column='GST_till', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gst_above = models.CharField(db_column='GST_above', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hsn_code'


class Languages(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    rtl = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'languages'


class Links(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'links'


class Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    conversation_id = models.IntegerField()
    user_id = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField()
    client_id = models.PositiveIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class OrderDetails(models.Model):
    order_id = models.IntegerField()
    seller_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField()
    variation = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tax = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=10)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    shipping_type = models.CharField(max_length=255, blank=True, null=True)
    pickup_point_id = models.IntegerField(blank=True, null=True)
    product_referral_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    guest_id = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    purchase_order_number = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    shipping_charge = models.CharField(max_length=200, blank=True, null=True)
    coupon_code = models.CharField(max_length=200, blank=True, null=True)
    coupon_discount = models.FloatField()
    code = models.TextField(blank=True, null=True)
    date = models.IntegerField()
    viewed = models.IntegerField()
    gift_wrap = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    delivery_viewed = models.IntegerField()
    payment_status_viewed = models.IntegerField(blank=True, null=True)
    commission_calculated = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_log'


class OrderStatus(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    short = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    order_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_status'


class OrderStatusHistory(models.Model):
    order_id = models.CharField(max_length=100)
    courier_partner = models.CharField(max_length=255, blank=True, null=True)
    trackingnumber = models.CharField(db_column='trackingNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pickupperson = models.CharField(db_column='pickupPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    canceledreason = models.CharField(db_column='canceledReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='orderStatus', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_status_history'


class Orders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    guest_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    updated_by = models.IntegerField(blank=True, null=True)
    seller_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    uniware_request = models.TextField(blank=True, null=True)
    uniware_response = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    purchase_order_number = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    shipping_charge = models.CharField(max_length=200, blank=True, null=True)
    coupon_code = models.CharField(max_length=200, blank=True, null=True)
    coupon_discount = models.FloatField()
    code = models.TextField(blank=True, null=True)
    date = models.IntegerField()
    viewed = models.IntegerField()
    gift_wrap = models.IntegerField()
    delivery_viewed = models.IntegerField()
    payment_status_viewed = models.IntegerField(blank=True, null=True)
    commission_calculated = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


class OtpConfigurations(models.Model):
    type = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'otp_configurations'


class PageHeadings(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=200)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'page_headings'


class PageTranslations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    page_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'page_translations'


class Pages(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.CharField(max_length=1000, blank=True, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    meta_image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_device = models.TextField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=225)
    ip = models.CharField(max_length=225)
    method = models.CharField(max_length=225)
    agent = models.CharField(max_length=225)
    payment_method = models.CharField(max_length=30)
    request = models.TextField()
    response = models.TextField()
    payment_phase = models.CharField(max_length=40)
    letzpay_hash = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=40)
    is_status_final = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_logs'


class Payments(models.Model):
    id = models.IntegerField(primary_key=True)
    seller_id = models.IntegerField()
    amount = models.FloatField()
    payment_details = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    txn_code = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments'


class PickupPointTranslations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pickup_point_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    address = models.TextField()
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pickup_point_translations'


class PickupPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    pick_up_status = models.IntegerField(blank=True, null=True)
    cash_on_pickup_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pickup_points'


class Policies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'policies'


class ProductRecent(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    temp_user_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_recent'


class ProductStocks(models.Model):
    product_id = models.IntegerField()
    variant = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    product_sku = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    image = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    updated_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stocks'


class ProductTaxes(models.Model):
    product_id = models.IntegerField()
    tax_id = models.IntegerField()
    tax = models.FloatField()
    tax_type = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_taxes'


class ProductTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_translations'


class Products(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, blank=True, null=True)
    added_by = models.CharField(max_length=6)
    user_id = models.IntegerField()
    category_id = models.IntegerField()
    subcategoryid = models.CharField(db_column='subCategoryId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brand_id = models.IntegerField(blank=True, null=True)
    photos = models.CharField(max_length=2000, blank=True, null=True)
    thumbnail_img = models.CharField(max_length=100, blank=True, null=True)
    imagetype = models.CharField(db_column='imageType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    video_provider = models.CharField(max_length=20, blank=True, null=True)
    video_link = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField()
    added_hsn_price = models.FloatField()
    purchase_price = models.FloatField(blank=True, null=True)
    variant_product = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    choice_options = models.TextField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)
    variations = models.TextField(blank=True, null=True)
    todays_deal = models.IntegerField()
    published = models.IntegerField()
    stock_visibility_state = models.CharField(max_length=10, blank=True, null=True)
    cash_on_delivery = models.IntegerField()
    featured = models.IntegerField()
    seller_featured = models.IntegerField()
    current_stock = models.IntegerField()
    unit = models.CharField(max_length=20, blank=True, null=True)
    min_qty = models.IntegerField()
    low_stock_quantity = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.CharField(max_length=10, blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    tax_type = models.CharField(max_length=10, blank=True, null=True)
    shipping_type = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    shipping_cost = models.TextField(blank=True, null=True)
    is_quantity_multiplied = models.IntegerField()
    est_shipping_days = models.IntegerField(blank=True, null=True)
    num_of_sale = models.IntegerField()
    meta_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_img = models.CharField(max_length=255, blank=True, null=True)
    pdf = models.CharField(max_length=255, blank=True, null=True)
    slug = models.TextField()
    refundable = models.IntegerField()
    earn_point = models.FloatField()
    rating = models.FloatField()
    barcode = models.CharField(max_length=255, blank=True, null=True)
    hsncode = models.CharField(db_column='HSNCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    digital = models.IntegerField()
    is_deleted = models.IntegerField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    isshikoh = models.CharField(max_length=200, blank=True, null=True)
    shikohpriority = models.CharField(db_column='ShikohPriority', max_length=200, blank=True, null=True)  # Field name made lowercase.
    trendingpriority = models.IntegerField(db_column='TrendingPriority', blank=True, null=True)  # Field name made lowercase.
    istrending = models.CharField(max_length=200, blank=True, null=True)
    isfestivewear = models.CharField(db_column='isFestiveWear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    festivepriority = models.IntegerField(db_column='FestivePriority', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class RefundRequests(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    order_detail_id = models.IntegerField()
    seller_id = models.IntegerField()
    seller_approval = models.IntegerField()
    admin_approval = models.IntegerField()
    refund_amount = models.FloatField()
    reason = models.TextField(blank=True, null=True)
    admin_seen = models.IntegerField()
    refund_status = models.IntegerField()
    reject_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'refund_requests'


class Reviews(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'


class RoleTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role_translations'


class Roles(models.Model):
    name = models.CharField(max_length=30)
    permissions = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles'


class Searches(models.Model):
    query = models.CharField(max_length=1000)
    count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'searches'


class SellerWithdrawRequests(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    message = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    viewed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seller_withdraw_requests'


class Sellers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    verification_status = models.IntegerField()
    verification_info = models.TextField(blank=True, null=True)
    cash_on_delivery_status = models.IntegerField()
    admin_to_pay = models.FloatField()
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_acc_name = models.CharField(max_length=200, blank=True, null=True)
    bank_acc_no = models.CharField(max_length=50, blank=True, null=True)
    bank_routing_no = models.IntegerField(blank=True, null=True)
    bank_payment_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sellers'


class SeoSettings(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    revisit = models.IntegerField()
    sitemap_link = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'seo_settings'


class Shops(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    sliders = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    google = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    pick_up_point_id = models.TextField(blank=True, null=True)
    shipping_cost = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class Sliders(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    published = models.IntegerField()
    view = models.IntegerField()
    carousel_id = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sliders'


class SmsTemplates(models.Model):
    identifier = models.CharField(max_length=100)
    sms_body = models.TextField()
    template_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_templates'


class Staff(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'


class States(models.Model):
    name = models.CharField(max_length=40)
    country_id = models.IntegerField()
    region_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class SubcategoryTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_category_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    lang = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subCategory_translations'


class Subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    maincatid = models.CharField(db_column='mainCatID', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subcategoryname = models.CharField(db_column='subCategoryName', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subcategoryurl = models.CharField(db_column='subCategoryURL', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subcategoryisactive = models.CharField(db_column='subCategoryIsActive', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subcategoryincludenav = models.CharField(db_column='subCategoryIncludeNav', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subpagetitle = models.CharField(db_column='subPageTitle', max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    submetakeyword = models.CharField(db_column='subMetaKeyword', max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    submetadescription = models.CharField(db_column='subMetaDescription', max_length=191, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    sizechart = models.CharField(db_column='sizeChart', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    chartimage = models.CharField(db_column='chartImage', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    chartimageinternational = models.CharField(db_column='chartImageInternational', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    subcatpriority = models.IntegerField(db_column='subCatPriority')  # Field name made lowercase.
    subcataddedon = models.CharField(db_column='subCatAddedOn', max_length=191, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategory'


class SubcategoryOld(models.Model):
    subcatid = models.BigAutoField(db_column='subcatID', primary_key=True)  # Field name made lowercase.
    maincatid = models.CharField(db_column='mainCatID', max_length=191)  # Field name made lowercase.
    subcategoryname = models.CharField(db_column='subCategoryName', max_length=191)  # Field name made lowercase.
    subcategoryurl = models.CharField(db_column='subCategoryURL', max_length=191)  # Field name made lowercase.
    subcategoryisactive = models.CharField(db_column='subCategoryIsActive', max_length=191)  # Field name made lowercase.
    subcategoryincludenav = models.CharField(db_column='subCategoryIncludeNav', max_length=191)  # Field name made lowercase.
    subpagetitle = models.CharField(db_column='subPageTitle', max_length=191)  # Field name made lowercase.
    submetakeyword = models.CharField(db_column='subMetaKeyword', max_length=191)  # Field name made lowercase.
    submetadescription = models.CharField(db_column='subMetaDescription', max_length=191)  # Field name made lowercase.
    sizechart = models.CharField(db_column='sizeChart', max_length=191)  # Field name made lowercase.
    chartimage = models.CharField(db_column='chartImage', max_length=191)  # Field name made lowercase.
    chartimageinternational = models.CharField(db_column='chartImageInternational', max_length=191)  # Field name made lowercase.
    subcatpriority = models.CharField(db_column='subCatPriority', max_length=191)  # Field name made lowercase.
    subcataddedon = models.CharField(db_column='subCatAddedOn', max_length=191)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategory_old'


class Subscribers(models.Model):
    email = models.CharField(unique=True, max_length=200)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscribers'


class Taxes(models.Model):
    name = models.CharField(max_length=255)
    tax_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'taxes'


class TicketReplies(models.Model):
    id = models.IntegerField(primary_key=True)
    ticket_id = models.IntegerField()
    user_id = models.IntegerField()
    reply = models.TextField()
    files = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_replies'


class Tickets(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    user_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    files = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    status = models.CharField(max_length=10)
    viewed = models.IntegerField()
    client_viewed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tickets'


class Translations(models.Model):
    id = models.IntegerField()
    lang = models.CharField(max_length=10, blank=True, null=True)
    lang_key = models.TextField(blank=True, null=True)
    lang_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'translations'


class Uploads(models.Model):
    file_original_name = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'


class Usertext(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    normal_password = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userText'


class Users(models.Model):
    referred_by = models.IntegerField(blank=True, null=True)
    provider_id = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.CharField(max_length=10)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=191, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    normal_password = models.CharField(max_length=50, blank=True, null=True)
    verification_code = models.TextField(blank=True, null=True)
    new_email_verificiation_code = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    avatar_original = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    balance = models.FloatField()
    banned = models.IntegerField()
    referral_code = models.CharField(max_length=255, blank=True, null=True)
    customer_package_id = models.IntegerField(blank=True, null=True)
    remaining_uploads = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wallets(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wallets'


class Wishlists(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wishlists'
