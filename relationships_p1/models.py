from django.db import models

#------------------------------------
#            PART 2
#------------------------------------


class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return (self.title)

class Viewer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    films = models.ManyToManyField(Film, related_name='viewers')
    
    def __str__(self):
        return (self.name)



class Worker(models.Model):
    name = models.CharField(max_length=100)
    wage = models.IntegerField()

    def __str__(self):
        return (f'{self.name}, {self.wage}')

class Shift(models.Model):
    date = models.CharField(max_length=20)
    time = models.IntegerField()
    workers = models.ManyToManyField(Worker, related_name="shifts")

    def __str__(self):
        return (f'{self.date}, {self.time}')





# ------------------------------------
#            PART 1 
# ------------------------------------
#  Data Set 1

# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     address = models.CharField(max_length = 255)
    
# class Order(models.Model):
#     order = models.CharField(max_length = 255)
#     date = models.DateField(auto_now_add=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers')

# # Data Set 2

# class Country(models.Model):
#     name = models.CharField(max_length=255)
#     year_founded = models.IntegerField()
    
# class Province(models.Model):
#     name = models.CharField(max_length=255)
#     year_founded = models.IntegerField()
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')

# class City(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="provinces")

# class Residence(models.Model):
#     address = models.CharField(max_length=255)
#     year_built = models.IntegerField()
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name = 'cities')

# class Person(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='residence')
