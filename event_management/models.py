from django.db import models
from django.db.models import Count
import datetime
from time import gmtime, strftime

# Create your models here.

class user(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, unique=True)
<<<<<<< HEAD
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=32, null=True)
    district = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
=======
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=32)

    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
>>>>>>> a4fc304e361eed37d54319c95ea8f98268f94572

    def __str__(self):
        return self.user_id



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
    admin_id = models.OneToOneField(
        user, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.admin_id)


class package(models.Model):
    pack_id = models.CharField(max_length=10, primary_key=True, unique=True)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    pack_name = models.CharField(max_length=50)
    featuers = models.CharField(max_length=500)
    pack_type = models.CharField(max_length=100)

    def __str__(self):
        return self.pack_id


class customer(models.Model):
    cus_id = models.ForeignKey(
        user, on_delete=models.CASCADE, primary_key=True)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.cus_id


class event(models.Model):
    event_id = models.CharField(max_length=10, primary_key=True, unique=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, null=True)
    budget = models.FloatField(max_length=5)
    email_address = models.CharField(max_length=50)
    occassion_type = models.CharField(max_length=10)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    head_count = models.IntegerField(max_length=10)
    creator_phone = models.CharField(max_length=10)
    schedule_file = models.CharField(max_length=500, null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    event_type = models.CharField(max_length=20)
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    event_creator_name = models.CharField(max_length=20)
    d = datetime.datetime.now()
    created_month = models.CharField(
        max_length=5, default=datetime.datetime.now().strftime('%B'))
    created_date = models.CharField(
        max_length=20, default=datetime.datetime.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.location


class ticket(models.Model):
    ticket_id = models.CharField(primary_key=True, unique=True, max_length=10)
    event_id = models.OneToOneField(event, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    tkt_name = models.CharField(max_length=50)
    tkt_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    price = models.FloatField(max_length=5, default=0.00)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.CharField(max_length=500)
    no_of_tickets = models.IntegerField(max_length=5)

    def __str__(self):
        return self.ticket_id


class batch(models.Model):
    batch_id = models.CharField(primary_key=True, unique=True, max_length=10)
    ticket_id = models.OneToOneField(ticket, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.batch_id


class batch_ticket(models.Model):
    batch_ticket_id = models.CharField(
        max_length=10, primary_key=True, unique=True)
    batch_id = models.ForeignKey(batch, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    availability_status = models.CharField(max_length=20)

    def __str__(self):
        return self.batch_ticket_id


class reservation(models.Model):
    reservation_id = models.CharField(
        max_length=10, primary_key=True, unique=True)
    batch_ticket_id = models.ForeignKey(batch_ticket, on_delete=models.CASCADE)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
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


class invoice(models.Model):
    invoice_id = models.CharField(max_length=10, primary_key=True)
    pay_id = models.ForeignKey(payment, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=50)
    amount = models.FloatField(default=0.00)
    inv_status = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=20)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.invoice_id


class equipment(models.Model):
    eq_id = models.CharField(max_length=10, primary_key=True)
    admin_id = models.ForeignKey(admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0.00, max_length=5)
    qty = models.IntegerField(max_length=5)

    def __str__(self):
        return self.eq_id


class equipment_event(models.Model):
    eq_ev_id = models.CharField(max_length=10, primary_key=True)
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    qty = models.IntegerField(max_length=5)

    def __str__(self):
        return self.eq_ev_id


class rented_item(models.Model):
    rented_item_id = models.ForeignKey(
        equipment, on_delete=models.CASCADE, max_length=10, primary_key=True)
    supplier = models.CharField(max_length=50)
    rented_date = models.DateField(auto_now=True, auto_now_add=False)
    rental_period = models.CharField(max_length=10)

    def __str__(self):
        return self.rented_item_id


class rent_details(models.Model):
    rent_id = models.CharField(max_length=10, primary_key=True)
    pay_id = models.ForeignKey(payment, on_delete=models.CASCADE)
    eq_id = models.ForeignKey(equipment, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now=True)
    rental_period = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    price = models.FloatField(default=0.00)
    qty = models.IntegerField()

    def __str__(self):
        return self.rent_id


class customer_equipment(models.Model):
    cus_id = models.ForeignKey(
        customer, on_delete=models.CASCADE, primary_key=True)
    equipment_id = models.ForeignKey(equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.cus_id


class inventory_items(models.Model):
    item_id = models.ForeignKey(
        equipment_event, on_delete=models.CASCADE, primary_key=True)
    image = models.CharField(max_length=500)
    model = models.CharField(max_length=20)
    condition = models.CharField(max_length=50)
    availability = models.CharField(max_length=30)

    def __str__(self):
        return self.item_id


class emp_details(models.Model):
    emp_det_id = models.CharField(max_length=6, primary_key=True, default="")
    admin_id = models.ForeignKey('admin', on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50)
    primary_phone = models.CharField(max_length=10, unique=True)
    secondary_phone = models.CharField(max_length=10, unique=True)
    p = (
        ("Manager", "Manager"), ("Supervisor",
                                 "Supervisor"), ("Employee", "Employee")
    )
    position = models.CharField(max_length=15, choices=p, default="Employee")
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=50, unique=True)
    qualification = models.CharField(max_length=500)
    trained_years = models.IntegerField(default=0)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=False)
    g = (
        ("Male", "Male"), ("Female", "Female")
    )
    gender = models.CharField(max_length=10, choices=g, default="Male")
    r = (
        ("Yes", "Yes"), ("No", "No")
    )
    permenent = models.CharField(max_length=4, choices=r, default="No")
    joined_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.emp_det_id


class department(models.Model):
    dept_id = models.CharField(max_length=6, primary_key=True, default="")
    admin_id = models.ForeignKey('admin', on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=50, unique=True)
    dept_manager_name = models.OneToOneField(
        'emp_details', on_delete=models.CASCADE, limit_choices_to={'position': 'Manager'})

    def __str__(self):
        return self.dept_id


class dept_manager(models.Model):
    emp_id = models.OneToOneField('emp_details', on_delete=models.CASCADE,
                                  primary_key=True, limit_choices_to={'position': 'Manager'})
    dept_id = models.ForeignKey('department', on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.emp_id)


class dept_supervisor(models.Model):
    emp_id = models.OneToOneField(
        'emp_details', on_delete=models.CASCADE, primary_key=True, limit_choices_to={'position': 'Supervisor'})
    dept_id = models.ForeignKey('department', on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.emp_id)


class dept_employee(models.Model):
    emp_id = models.OneToOneField(
        'emp_details',  on_delete=models.CASCADE, primary_key=True, limit_choices_to={'position': 'Employee'})
    dept_id = models.ForeignKey('department', on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.emp_id)


class emp_details_leave(models.Model):
    emp_id = models.ForeignKey('emp_details', on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_id


class salary(models.Model):
    sal_id = models.CharField(max_length=10, primary_key=True)
    emp_det_id = models.ForeignKey('emp_details', on_delete=models.CASCADE)
    dept_id = models.ForeignKey('department', on_delete=models.CASCADE)
    basic_sal = models.IntegerField(default=0)
    extra_hours = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)

    @property
    def Extra_Payment(self):
        return self.extra_hours * 300
    extra = property(Extra_Payment)


    @property
    def Total_Payment(self):
        return self.Extra_Payment + self.basic_sal + self.bonus 
    total_Payment = property(Total_Payment)

    m = (
        ("January", "January"), ("February", "February"), ("March", "March"), ("April", "April"), ("May", "May"), ("June", "June"), ("July",
                                                                                                                                     "July"), ("August", "August"), ("September", "September"), ("October", "October"), ("November", "November"), ("December", "December")
    )
    month = models.CharField(max_length=10, choices=m)
    Year = models.IntegerField(max_length=4, default="2021")
    y = (("Yes", "Yes"), ("No", "No"))
    paid = models.CharField(max_length=10, choices=y)
    Paid_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.sal_id

class userActions(models.Model):
    username = models.CharField(max_length=50)
    createdDate = models.CharField(max_length=20)

    def __str__(self):
        return self.username



