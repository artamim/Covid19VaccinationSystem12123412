def certification(request):
    if request.method == 'POST':
        nid_number = request.POST['nid_number']
        birth_date = request.POST['birth_date']
        user=auth.authenticate(nid_number=nid_number,birth_date=birth_date)
        if user is not None:
            if user.certification== True :
                return redirect('CertificateImage',{{user.certificate}})
            else:
                messages.info(request,'Your certificate is not ready yet')
        else:
            messages.info(request,'Invalid credential')
    else:
        return render(request, 'certification')