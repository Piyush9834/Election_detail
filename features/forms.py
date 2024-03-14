from django import forms
from .models import FullVoterDetail, AppDetail

class FullVoterDetailForm(forms.ModelForm):
    class Meta:
        model = FullVoterDetail
        fields = '__all__'
        
class AppDetailForm(forms.ModelForm):
    class Meta:
        model = AppDetail
        fields = ['app_name', 'party_name', 'is_enable', 'banner_send_date', 'password', 'error_message',
                  'promotion_message']  
        



# class FullVoterDetailViewset(viewsets.ViewSet):
#     serializer_class = FullVoterDetailSerializer
#     queryset = FullVoterDetail.objects.all()
#     http_method_names = ['get', 'patch']
    
#     def list(self, request):
#         if request.method == 'get':
#             ac_no = request.query_params.get('ac_no')
#             if not ac_no:
#                 return Response({"error": "Please provide AC No."}, status=status.HTTP_400_BAD_REQUEST)

#             try:
#                 voters = self.queryset.filter(ac_no=ac_no).order_by('sr_no')
#                 serializer = self.serializer_class(voters, many=True)
#                 return Response(serializer.data)
#             except ValueError:
#                 return Response({"error": "Invalid AC No provided"}, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         try:
#             voter = get_object_or_404(self.queryset, epic_no=pk)
#             serializer = self.serializer_class(voter, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"success": "Voter details updated successfully!"})
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except FullVoterDetail.DoesNotExist:
#             return Response({"error": "Voter details not found"}, status=status.HTTP_404_NOT_FOUND)
        
# class FullVoterDetailViewset(viewsets.ModelViewSet):
#     serializer_class = FullVoterDetailSerializer
#     queryset = FullVoterDetail.objects.all()  
#     lookup_field = 'epic_no'     

# class FullVoterDetailViewset(viewsets.ModelViewSet):
#     serializer_class = FullVoterDetailSerializer
#     queryset = FullVoterDetail.objects.all()

#     def list(self, request):
#         if request.method == 'GET':
#             ac_no = request.query_params.get('ac_no')
#             if not ac_no:
#                 return Response({"error": "Please provide AC No."}, status=status.HTTP_400_BAD_REQUEST)

#             try:
#                 voters = self.queryset.filter(ac_no=ac_no).order_by('sr_no')
#                 if not voters:
#                     raise ValidationError("No voters found for the provided AC No.")
#                 serializer = self.serializer_class(voters, many=True)
#                 return Response(serializer.data)
#             except ValidationError as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         try:
            
#             voter = get_object_or_404(self.queryset, epic_no=pk)
            
            
#             partial = request.method == 'PATCH'

            
#             serializer = self.serializer_class(voter, data=request.data, partial=partial)

            
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"success": "Voter details updated successfully!"})
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         except FullVoterDetail.DoesNotExist:
#             return Response({"error": "Voter details not found"}, status=status.HTTP_404_NOT_FOUND)#



#dashboard whole vies edit and dlt ------------------------
# class DasboardViewSet(viewsets.ViewSet):
#     def get(self, request):
#         search_query = request.GET.get('q') or ''
#         voter_details = FullVoterDetail.objects.all()
#         if search_query:
#             voter_details = voter_details.filter(first_name_english__icontains=search_query)
#             no_results = not voter_details.exists()
#         else:
#             no_results = False
            
        
#         return render(request, 'dashboard.html', {'voter_details': voter_details, 'search_query': search_query, 'no_results': no_results})

#     def edit_voter_detail(request, pk):
#         print("Received primary key:", pk)
#         voter_detail = get_object_or_404(FullVoterDetail, pk=pk)
        
#         #print(voter_detail)
#         if request.method == 'POST':
#             form = FullVoterDetailForm(request.POST, instance=voter_detail)
#             if form.is_valid():
#                 form.save()
#                 return redirect('dashboard')
#         else:
#             form = FullVoterDetailForm(instance=voter_detail)
#             #print(form)
#         return render(request, 'edit_voter_detail.html', {'form': form})

#     def delete_voter_detail(request, pk):
#         voter_detail = get_object_or_404(FullVoterDetail, pk=pk)
#         if request.method == 'POST':
#             voter_detail.delete()
#             return redirect('dashboard')
#         return render(request, 'delete_voter_detail.html', {'voter_detail': voter_detail})