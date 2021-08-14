def register(request):
    if request.method == 'POST':
        select_type = request.POST['select_type']
        nid_number = request.POST['nid_number']
        birth_date = request.POST['birth_date']
        choose_center = request.POST['choose_center']
        varify_code = request.POST['choose_center']
        RegisterModel.user.save()
    else:
        return render(request, 'Register.html',)