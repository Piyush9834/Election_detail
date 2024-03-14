

from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AppDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    is_enable = models.BooleanField(default=False)
    banner_send_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=100, blank=True)
    error_message = models.TextField(blank=True)
    promotion_message = models.TextField(blank=True)
    
    
    def __str__(self):
        return f"{self.app_name}"
    
    class Meta:
        
        verbose_name = 'apps'
        
        
        


class FullVoterDetail(BaseModel):
    
    sr_no = models.IntegerField(null=False, primary_key=True)
    ac_no = models.IntegerField()
    booth_no = models.IntegerField()
    epic_no = models.CharField(max_length=100)
    voter_sr_no = models.IntegerField(blank=True)
    booth_address_hindi = models.TextField(null=True,blank=True)
    house_no = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    full_name_english = models.CharField(max_length=255, blank=True)
    full_name_hindi = models.CharField(max_length=255, blank=True)
    first_name_english = models.CharField(max_length=100, blank=True)
    first_name_hindi = models.CharField(max_length=100, blank=True)
    middle_name_english = models.CharField(max_length=100, blank=True)
    middle_name_hindi = models.CharField(max_length=100, blank=True)
    last_name_english = models.CharField(max_length=100, blank=True)
    last_name_hindi = models.CharField(max_length=100, blank=True)
    gender_english = models.CharField(max_length=10, blank=True)
    gender_hindi = models.CharField(max_length=10, blank=True)
    address_english = models.TextField(null=True, blank=True)
    address_hindi = models.TextField(null=True, blank=True)
    booth_address_english = models.TextField(blank=True)
   
    mobile_no = models.CharField(max_length=15, blank=True)
    is_voted = models.BooleanField(default=False)
    colour = models.CharField(max_length=50, blank=True)
    is_activist = models.BooleanField(default=False)
    profession = models.CharField(max_length=100, blank=True)
    updated_address = models.TextField(blank=True)
    post = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
       return f"Voter: {self.full_name_english}"
    
    class Meta:
        verbose_name = 'Voter'



