from django.http.response import HttpResponse
from django.shortcuts import redirect
class myMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization in class")

    def __call__(self, request):
        print("Before view in class ")
        path = request.path
        if path in ['/app/', '/app','apps', '/apps/', '/apps']:
            return redirect('myview')  
        response = self.get_response(request)
        print("After view in class")
        return response

    def process_exception(self, request, exception):
        """If there is any exception in view then it will run"""
        print("I am under process_exception")
        return HttpResponse(f"I am from process_exception {exception} middleware")

    def process_view(self, request, view_func, view_args, view_kargs):
        """This is called whne django calls the actual view.Django should return either None or 
        an HttpResponse object. If it returns None, Django will continue processing this request,
        executing any other process_view() middleware and, then, the appropriate view. 
        If it returns an HttpResponse object, Django won’t bother calling the appropriate view; 
        it’ll apply response middleware to that HttpResponse and return the result.
        """
        print("I am in process_view")
        #return HttpResponse("I am coming from process_view")

    def process_template_response(self, request, response):
        response.context_data['name'] = 'Payal'
        return response
