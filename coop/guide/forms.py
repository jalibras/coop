from django import forms
from django.forms import ModelForm

from guide.models import NaturalProblem,ArtificialProblem,ProblemVideo,Comment,Sector


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
        exclude = ['exists','owner','approved','done_by']
        widgets = {
                'sector':forms.Select(choices=(('a','a'),)),
                }



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




