from django.db import models

class BookInstance(models.Model):
    bins_id = models.AutoField(primary_key=True)
    rfid_sn = models.CharField(max_length=255)
    blockchain_id = models.CharField(max_length=255, blank=True, null=True)
    book_id = models.IntegerField()
    bc_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_instance'


class Bookcases(models.Model):
    bc_id = models.AutoField(primary_key=True)
    bc_no = models.CharField(max_length=10, blank=True, null=True)
    bc_sn = models.CharField(max_length=30, blank=True, null=True)
    blockchain_id = models.CharField(max_length=255, blank=True, null=True)
    address_detail = models.CharField(max_length=255, blank=True, null=True)
    address_pos = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookcases'


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    press = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.CharField(max_length=30, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    prices = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isdn = models.CharField(max_length=50, blank=True, null=True)
    brief = models.CharField(max_length=1024, blank=True, null=True)
    scores = models.CharField(max_length=10, blank=True, null=True)
    douban_url = models.CharField(max_length=512, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class OrderLog(models.Model):
    olog_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_state = models.IntegerField()
    is_renew = models.IntegerField(blank=True, null=True)
    renew_days = models.IntegerField(blank=True, null=True)
    frozen_points = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    oper_time = models.IntegerField(blank=True, null=True)
    oper_comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_log'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_sn = models.CharField(max_length=50)
    bins_id = models.IntegerField()
    user_id = models.IntegerField()
    borrow_days = models.IntegerField(blank=True, null=True)
    renew_num = models.IntegerField(blank=True, null=True)
    borrow_begintm = models.IntegerField(blank=True, null=True)
    borrow_endtm = models.IntegerField(blank=True, null=True)
    borrow_bcid = models.IntegerField(blank=True, null=True)
    return_bcid = models.IntegerField(blank=True, null=True)
    should_points = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    favour_points = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    actual_points = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    bonus_points = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    bonus_credits = models.IntegerField(blank=True, null=True)
    order_state = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField()
    user_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50)
    land_passwd = models.CharField(max_length=100)
    blockchain_id = models.CharField(max_length=255, blank=True, null=True)
    scores = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    frozen_scores = models.DecimalField(max_digits=24, decimal_places=12, blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    qq_no = models.CharField(max_length=50, blank=True, null=True)
    weixin_no = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    is_auth = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    user_degree = models.IntegerField(blank=True, null=True)
    user_desc = models.CharField(max_length=255, blank=True, null=True)
    last_login_time = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    oper_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
