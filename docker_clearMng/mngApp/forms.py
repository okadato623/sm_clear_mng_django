from django import forms

class SongForm(forms.Form):
    title = forms.CharField(required=False)

    bLv = forms.CharField(required=False)
    eLv = forms.CharField(required=False)
    mLv = forms.CharField(required=False)
    hLv = forms.CharField(required=False)
    cLv = forms.CharField(required=False)

    bRes = forms.CharField(required=False)
    eRes = forms.CharField(required=False)
    mRes = forms.CharField(required=False)
    hRes = forms.CharField(required=False)
    cRes = forms.CharField(required=False)

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label='')