def status(request):
    if request.method == 'POST':
        nid_number = request.POST['nid_number']
        birth_date = request.POST['birth_date']
        user.auth.authenticate(nid_number=nid_number,birth_date=birth_date)
        if user is not None:
            if user.status== True :
                messages.info(request,'You are registered successfully')
            else:
                messages.info(request,'You are not registered yet')
        else:
            messages.info(request,'Invalid credential')
    else:
        return render(request, 'Status.html',)