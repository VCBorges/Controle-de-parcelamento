from django.http import JsonResponse

# Create your views here.


class FormSubmissionMixin:
    
    form_class = None
    success_message = None
    error_message = None
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            response = {
                'status': 201,
                'message': self.success_message
            }
            
        else:
            response = {
                'status': 400,
                'message': self.error_message
            }

        return JsonResponse(response)
