from django.shortcuts import redirect
class PatientAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_request(self, request):
        
        if 'userid' in request.session:
            return None
        return redirect('index')


class PatientLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_request(self, request):
        
        if 'userid' in request.session:
            return redirect('home')
        return None


class AdminAuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_request(self, request):    
        if 'admin' in request.session:
            return None
        return redirect('adminLogin')
    
    
class AdminLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_request(self, request):    
        if 'admin' in request.session:
            return redirect('dashboard')
        return None