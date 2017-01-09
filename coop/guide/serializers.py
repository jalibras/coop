from rest_framework import serializers

from guide.models import ArtificialProblem, NaturalProblem, ProblemImage, Area





class ArtificialProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtificialProblem
        exclude = ()


class NaturalProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalProblem
        exclude = ()

class ProblemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemImage
        exclude = ()

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = ()



