from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        return 5

    def validate_release_date(self, value):
        if value.year <= 2000:
            raise serializers.ValidationError('ERRO! Só aceitamos filmes a parti do ano 2000.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('ERRO! Resumo deve ter menos de 200 catacteres.')

