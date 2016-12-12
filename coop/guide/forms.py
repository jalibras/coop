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
        exclude = []

