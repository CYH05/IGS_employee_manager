import requests
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = dict()
        employee_response = requests.get("http://127.0.0.1:8000/employee/")
        department_response = requests.get("http://127.0.0.1:8000/department/")
        context['object']= {
            'employees': employee_response.json(),
            'departments': department_response.json()
        }
        
        return context