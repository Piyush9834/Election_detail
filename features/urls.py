from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CheckAppEnableView, FullVoterDetailViewset, FileUploadViewSet, DasboardViewSet , AppDasboardViewSet, SortVoterDetailViewSet, upload_file_view

router = DefaultRouter()
router.register(r'get_voter_details', FullVoterDetailViewset, basename='get-voter-detail')
router.register(r'sort_voter', SortVoterDetailViewSet, basename='get-sort-detail' )
#router.register(r'dashboard_fulldetail', DasboardViewSet, basename='dashboard-fulldetail')

urlpatterns = [
    path(" ", include(router.urls)),
    path('check_app_enable/', CheckAppEnableView.as_view(), name='check_app_enable'),
    path('upload/', upload_file_view, name='upload_file_view'),
    path('process_upload/', FileUploadViewSet.as_view(), name='process_file_upload'),
   
    path('dashboard/',DasboardViewSet.as_view({'get': 'get'}), name='dashboard'),
    path('add_voter/', DasboardViewSet.add_voter_detail, name='add-voter'),
    path('edit/<int:pk>/', DasboardViewSet.as_view({'get': 'edit_voter_detail', 'post': 'edit_voter_detail'}), name='edit_voter_detail'),
   
    path('delete/<int:pk>/',DasboardViewSet.delete_voter_detail, name='delete_voter_detail'),
    
    path('app_dashboard/', AppDasboardViewSet.as_view({'get': 'get'}), name='app-dashboard'),
    path('app_edit/<int:pk>/', DasboardViewSet.as_view({'get': 'edit_app_detail', 'post': 'edit_app_detail'}), name='edit_app_detail'),
    path('app_delete/<int:pk>/', AppDasboardViewSet.delete_delete_detail, name='delete_app_detail'),
   
    
]
    
    


urlpatterns += router.urls
