from django.db import models

# Create your models here.


class user(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, unique=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=6)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id


class login(models.Model):
    login_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.login_id

class feedback(models.Model):
    feed_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    ratings = models.IntegerField(max_length=5)

    def __str__(self):
        return self.feed_id

class admin(models.Model):
    admin_id = models.ForeignKey(user, primary_key=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.admin_id

class package(models.Model):
    pack_id = models.CharField(max_length=10, primary_key=True, unique=True)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    pack_name = models.CharField(max_length=50)
    featuers = models.CharField(max_length=500)
    pack_type = models.CharField(max_length=100)

    def __str__(self):
        return self.pack_id

class customer(models.Model):
    cus_id = models.ForeignKey(user, on_delete=models.CASCADE, primary_key=True)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.cus_id

class event(models.Model):
    event_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    budget = models.FloatField(max_length=5)
    email_address = models.CharField(max_length=50)
    occassion_type = models.CharField(max_length=10)
    eq_quantity = models.IntegerField(max_length=10, null=True)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    head_count = models.IntegerField(max_length=10)
    creator_phone = models.CharField(max_length=10)
    schedule_file = models.CharField(max_length=500)
    date = models.DateField(auto_now=True, auto_now_add=False)
    event_type = models.CharField(max_length=20)
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    event_creator_name = models.CharField(max_length=20)
    eq_list = models.CharField(max_length=500)

    def __str__(self):
        return self.event_id

class ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, unique=True, max_length=10)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    tkt_name = models.CharField(max_length=50)
    tkt_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    price = models.FloatField(max_length=5, default=0.00)
    expiration_date = models.DateField(auto_now=True, auto_now_add=False)
    image = models.CharField(max_length=500)
    no_of_tickets = models.IntegerField(max_length=5)

    def __str__(self):
        return self.ticket_id

class batch(models.Model):
    batch_id = models.CharField(primary_key=True, unique=True, max_length=10)
    ticket_id = models.ForeignKey(ticket, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.batch_id

class batch_ticket(models.Model):
    batch_ticket_id = models.CharField(max_length=10,primary_key=True,unique=True)
    batch_id = models.ForeignKey(batch, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=20)

    def __str__(self):
        return self.batch_ticket_id

class reservation(models.Model):
    reservation_id = models.CharField(max_length=10, primary_key=True, unique=True)
    batch_ticket_id = models.ForeignKey(batch_ticket, on_delete=models.CASCADE)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.reservation_id

class payment(models.Model):
    pay_id = models.CharField(max_length=10, primary_key=True)
    reservation_id = models.ForeignKey(reservation, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    pay_type = models.CharField(max_length=100)
    amount = models.FloatField(max_length=5, default=0.00)
    order_type = models.CharField(max_length=50)

    def __str__(self):
        return self.pay_id

class advertistment(models.Model):
    ad_id = models.CharField(max_length=10, primary_key=True, unique=True)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    pay_id = models.ForeignKey(payment, on_delete=models.CASCADE)
    pack_id = models.ForeignKey(package, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    ad_type = models.CharField(max_length=30)
    ad_title = models.CharField(max_length=50)

    def __str__(self):
        return self.ad_id


    
    
