from django import forms
from django.forms import ModelForm

from guide.models import NaturalProblem,ArtificialProblem,ProblemVideo,Comment


class ProblemVideoForm(ModelForm):
    class Meta:
        model = ProblemVideo
        fields = ['embed_code']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class AddArtificialProblemForm(ModelForm):
    class Meta:
        model = ArtificialProblem
        exclude = ['exists','owner']



class AddNaturalProblemForm(ModelForm):
    class Meta:
        model = NaturalProblem
        exclude = ['exists','owner']

    def clean(self):
        #if self.instance.problemimage_set.all().count()==0:
            #raise forms.ValidationError('You must upload at least one image for this problem')
        return super(AddNaturalProblemForm,self).clean()



