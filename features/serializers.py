from .models import *
from rest_framework import serializers

class AppDetailSerializer(serializers.ModelSerializer):
    app_name = serializers.CharField()
    party_name = serializers.CharField()
    class Meta:
        model = AppDetail
        fields = ['app_name', 'party_name', 'is_enable', 'banner_send_date', 'password', 'error_message', 'promotion_message']
    
    
   
        
        
class FullVoterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullVoterDetail
        fields = '__all__' 
        