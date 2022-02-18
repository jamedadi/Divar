from django.db import models



class Province(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    
class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Distinct(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Location(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    distinct = models.ForeignKey(Distinct, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f"{self.distinct} < {self.city} < {self.province}"