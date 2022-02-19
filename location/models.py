from django.db import models



class Province(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
    

    
class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"    

    
class Distinct(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Distinct"
        verbose_name_plural = "Distincts"
    
    

class Location(models.Model):
    """
    This model represent location of published advertisement by User
    """
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    distinct = models.ForeignKey(Distinct, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f"{self.distinct} < {self.city} < {self.province}"
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"