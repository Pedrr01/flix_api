from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieModelSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate_value = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate_value:
            return round(rate_value,1)  
        
        return None

    def validate_release_date(self, value):
        if value.year <= 2000:
            raise serializers.ValidationError('ERRO! Só aceitamos filmes a parti do ano 2000.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('ERRO! Resumo deve ter menos de 200 catacteres.')

