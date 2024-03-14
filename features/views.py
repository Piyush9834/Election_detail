
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import FullVoterDetailForm, AppDetailForm
from rest_framework import status
from rest_framework.decorators import action
from django.views import View
from django.shortcuts import get_object_or_404
from .models import AppDetail, FullVoterDetail
from .serializers import AppDetailSerializer, FullVoterDetailSerializer
import csv
from django.shortcuts import render, redirect
import pandas as pd
from rest_framework.exceptions import ValidationError
from .pagination import CustomLimitOffsetPagination
import openpyxl


class CheckAppEnableView(APIView):
    def get(self, request):
        app_name = request.query_params.get('app_name')
        party_name = request.query_params.get('party_name')
        
        if not app_name or not party_name:
            return Response({"error": "Please provide both 'app_name' and 'party_name' in query parameters."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            app_detail = AppDetail.objects.get(app_name=app_name, party_name=party_name)
            serializer = AppDetailSerializer(app_detail)
            return Response(serializer.data)
        except AppDetail.DoesNotExist:
            return Response({"error": "App details not found for the provided 'app_name' and 'party_name'."}, status=status.HTTP_404_NOT_FOUND)
        

class FullVoterDetailViewset(viewsets.ViewSet):
    serializer_class = FullVoterDetailSerializer
    queryset = FullVoterDetail.objects.all()
    pagination_class = CustomLimitOffsetPagination
    
    

    def list(self, request):
        if request.method == 'GET':
            ac_no = request.query_params.get('ac_no')
            if not ac_no:
                return Response({"error": "Please provide AC No."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                voters = self.queryset.filter(ac_no=ac_no).order_by('sr_no')
                if not voters:
                    raise ValidationError("No voters found for the provided AC No.")
                serializer = self.serializer_class(voters, many=True)
                return Response(serializer.data)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



    def update(self, request, pk=None):
        try:
            voter = get_object_or_404(self.queryset, epic_no=pk)
            serializer = self.serializer_class(voter, data=request.data, partial=True) 
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED) 
                #return Response({"success": "Voter details updated successfully!"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except FullVoterDetail.DoesNotExist:
            return Response({"error": "Voter details not found"}, status=status.HTTP_404_NOT_FOUND)

class SortVoterDetailViewSet(viewsets.ViewSet):
    
    serializer_class = FullVoterDetailSerializer
    queryset = FullVoterDetail.objects.all()
    
    
    @action(detail=True, methods=['get'])
    def sort_voter_1(self, request, pk=None, *args, **kwargs):
        try:
           
            objects = self.queryset.filter(ac_no=pk)
            print(objects)
 

            if objects is not None:
                response_data = []
                for instance in objects:
                    response_data.append({
                        'sr_no': instance.sr_no,
                        'AcNo': instance.ac_no,
                        'EpicNo': instance.epic_no,
                        'MobileNo': instance.mobile_no,
                        'isActivist': instance.is_activist,
                        'Profession': instance.profession,
                        'UpdatedAddress': instance.updated_address,
                        'Post': instance.post
                        })
                return Response(response_data)
            else:
                return Response({'error': 'Voter details not found'}, status=status.HTTP_404_NOT_FOUND)
        except FullVoterDetail.DoesNotExist:
            return Response({'error': 'Voter details not found'}, status=status.HTTP_404_NOT_FOUND)
class FileUploadViewSet(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if file.name.endswith('.csv'):
                data = csv.DictReader(file)
                for row in data:
                    FullVoterDetail.objects.create(**row)
            elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
                for index, row in df.iterrows():
                    FullVoterDetail.objects.create(**row.to_dict())
            else:
                raise ValueError('Unsupported file format')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'File uploaded successfully'})


def upload_file_view(request):
    return render(request, 'uploadfile.html')

class DasboardViewSet(viewsets.ViewSet):
    def get(self, request):
        search_query = request.GET.get('q') or ''
        voter_details = FullVoterDetail.objects.all()
        if search_query:
            voter_details = voter_details.filter(first_name_english__icontains=search_query)
            no_results = not voter_details.exists()
        else:
            no_results = False
            
        
        return render(request, 'dashboard.html', {'voter_details': voter_details, 'search_query': search_query, 'no_results': no_results})
    
    

    def edit_voter_detail(self, request, pk):
        print("Received primary key:", pk)
    
    
        voter_detail = get_object_or_404(FullVoterDetail, sr_no=pk)
        print("Retrieved voter detail:", voter_detail)
        if request.method == 'POST':

            form = FullVoterDetailForm(request.POST, instance=voter_detail)
            
            if form.is_valid():
            
                form.save()
            return redirect('dashboard')
        else:
        
            form = FullVoterDetailForm(instance=voter_detail)
    
    
        return render(request, 'edit_voter_detail.html', {'form': form})

    def delete_voter_detail(self, request, pk):
        voter_detail = get_object_or_404(FullVoterDetail, sr_no=pk)
        if request.method == 'POST':
            voter_detail.delete()
            return redirect('dashboard')
        return render(request, 'delete_voter_detail.html', {'voter_detail': voter_detail})
    
    def add_voter_detail(self, request):
        if request.method == 'POST':
            form = FullVoterDetailForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = FullVoterDetailForm()
        return render(request, 'add_voter_detail.html', {'form': form})

class AppDasboardViewSet(viewsets.ViewSet):
    def get(self, request):
        search_query = request.GET.get('q') or ''
        App_details = AppDetail.objects.all()
        if search_query:
            App_details = App_details.filter(app_name__icontains=search_query)
            no_results = not App_details.exists()
        else:
            no_results = True
        return render(request, 'App_detail_dashboard.html', {'App_details': App_details, 'search_query': search_query, 'no_results': no_results})
    
    
    def edit_app_detail(self, request, pk):
        print("Received primary key:", pk)
    
        app_detail = get_object_or_404(AppDetail, id=pk)
        print('Retrieved app_detail=', app_detail)
        if request.method == 'POST':
            form = AppDetailForm(request.POST, instance=app_detail)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = AppDetailForm(instance=app_detail)
        return render(request, 'edit_app_detail.html', {'form': form})

    def delete_delete_detail(request, pk):
        App_detail = get_object_or_404(AppDetail, pk=pk)
        if request.method == 'POST':
            App_detail.delete()
            return redirect('dashboard')
        return render(request, 'app_delete_detail.html', {'voter_detail': App_detail})
       
        

 


























