from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminFileWidget

from guide.models import NaturalProblem,ArtificialProblem,ProblemVideo,Comment,Sector,ProblemImage,ProblemFlag


class ProblemByMemberForm(forms.Form):
    status = forms.ChoiceField(choices=(
        (0,'still working on it'),
        (1,'done it'),
        ),
        )
    pass


class ProblemVideoForm(ModelForm):
    class Meta:
        model = ProblemVideo
        fields = ['embed_code']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class AddArtificialProblemForm(ModelForm):
    def __init__(self,*args,**kwargs):
        q = Sector.objects.all()
        if 'area_id' in kwargs:
            q = q.filter(area__id=kwargs['area_id'])
            kwargs.pop('area_id')
        super(AddArtificialProblemForm,self).__init__(*args,**kwargs)
        self.fields['sector'].queryset=q

    class Meta:
        model = ArtificialProblem
        exclude = ['exists','setter','owner','approved','done_by']
        widgets = {
                'description':forms.Textarea(attrs={
                    'placeholder':'A brief description of the problem. e.g. Dark blue with yellow tape, sit start, no arete, match on the last hold'}),
                'date':forms.TextInput(attrs={
                    'type':'date'
                    }),
                }


    def clean(self):
        cleaned_data = super(AddArtificialProblemForm,self).clean()
        holds = cleaned_data.get('holds')
        description = cleaned_data.get('description')
        print((holds,description))
        if holds==None and description=='':
            self._errors['']="You must either submit a description or pick a hold colour"
        print(self._errors)
        return cleaned_data



class AddNaturalProblemForm(ModelForm):
    def __init__(self,*args,**kwargs):
        q = Sector.objects.all()
        if 'area_id' in kwargs:
            q = q.filter(area__id=kwargs['area_id'])
            kwargs.pop('area_id')
        super(AddNaturalProblemForm,self).__init__(*args,**kwargs)
        self.fields['sector'].queryset=q

    class Meta:
        model = NaturalProblem
        exclude = ['exists','owner','approved','done_by']


    def clean(self):
        cleaned_data = super(AddArtificialProblemForm,self).clean()
        description = cleaned_data.get('description')
        print((holds,description))
        if description=='':
            self._errors['']="You must submit a description"
        print(self._errors)
        return cleaned_data



class ProblemImageInlineForm(forms.ModelForm):
    image_file = forms.FileField()

    class Meta:
        model = ProblemImage
        fields = ('image_file',)


class ProblemFlagForm(forms.ModelForm):
    class Meta:
        model = ProblemFlag
        exclude = ('problem','member','resolved','created')

