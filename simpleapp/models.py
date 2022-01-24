from statistics import mode
from django.db import models

business_categories ={
    ('AGRICULTURE & FORESTRY/WILDLIFE','Agriculture & Forestry/Wildlife'),
    ('BUSINESS & INFORMATION','Business & Information'),
    ('COSNTRUCTION/UTILITIES/CONTRACTING','Contruction/Utilities/Contracting'),
    ('EDUCATION','Education'),
    ('FINANCE & INSURANCE','Finance & Insurance'),
    ('FOOD & HOSPITALITY','Food & Hospitality'),
    ('GAMING','Gaming'),
    ('HEALTH SERVICES','Health Services'),
    ('MOTOR VEHICLE','Motor Vehicle'),
    ('NATURAL RESOURCES/ENVIROMENT','Natural Resources/Enviroment'),
    ('OTHER','Other(Business Type Not Listed)'),
    ('PERSONAL SERVICES','Personal Services'),
    ('REAL ESTATE & HOUSING','Real Estate & Housing'),
    ('SAFETY/SECURITY & LEGAL','Safety/Security & Legal'),
    ('TRANSPORTATION','Transportation'),
    
}




# Business Modle to handle business entries
class Business(models.Model):
    nameOfBusiness = models.CharField(max_length=200)
    category= models.CharField(max_length=40,choices=business_categories)
    websiteLink=models.URLField(max_length=200)
    facebookLink=models.URLField(max_length=200)
    instagramLink=models.URLField(max_length=200)
    twitterLink=models.URLField(max_length=200)
    
## should a business offer services to more than one city
class City(models.Model):
    business = models.ForeignKey(Business,related_name='cities',on_delete=models.CASCADE)
    City = models.TextField()
    State = models.TextField()