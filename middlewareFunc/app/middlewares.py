from django.shortcuts import redirect

def my_middleware(get_response):
    print("One time intialization")

    def my_functi(request):
        print("Before going to the view")
        path = request.path
        if path in ['/app/','app/', 'apps/', '/apps/', '/app']:
            return redirect('myview')
        response = get_response(request)
        print("after view function")
        return response
    return my_functi
