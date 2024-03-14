from django.contrib import admin
from dj_rest_kit.admin import BaseAdmin
from .models import AppDetail, FullVoterDetail

admin.site.register(AppDetail)
admin.site.register(FullVoterDetail)

# @admin.register(models.AppDetail)
# class ResourcesAdmin(admin.ModelAdmin):
#     list_display = ['app_name', 'party_name', 'is_enable', 'banner_send_date', 'password', 'error_message', ' promotion_message']
#     search_fields = ['app_name']
    
# @admin.register(models.FullVoterDetail)
# class FullVoterAdmin(admin.ModelAdmin):
#     list_display = [
#             'sr_no',
#             'ac_no',
#             'booth_no',
#             'epic_no',
#             'voter_sr_no',
#             'house_no',
#             'age',
#             'full_name_english',
#             'full_name_hindi',
#             'first_name_english',
#             'first_name_hindi',
#             'middle_name_english',
#             'middle_name_hindi',
#             'last_name_english',
#             'last_name_hindi',
#             'gender_english',
#             'gender_hindi',
#             'address_english',
#             'address_hindi',
#             'booth_address_english',
#             'booth_address_hindi',
#             'mobile_no',
#             'is_voted',
#             'colour',
#             'is_activist',
#             'profession',
#             'updated_address',
#             'post',
#         ]