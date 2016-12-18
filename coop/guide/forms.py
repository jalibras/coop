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


class NaturalProblemForm(ModelForm):
    class Meta:
        model = NaturalProblem
        exclude = ['owner']

    def clean(self):
        data = super(NaturalProblemForm,self).clean()
# put some custom validation logic here
        return data


class AddNaturalProblemForm(ModelForm):
    class Meta:
        model = NaturalProblem
        exclude = ['exists']

    def clean(self):
        #if self.instance.problemimage_set.all().count()==0:
            #raise forms.ValidationError('You must upload at least one image for this problem')
        return super(AddNaturalProblemForm,self).clean()



