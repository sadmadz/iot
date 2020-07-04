from rest_framework import serializers

from .models import Thing, Home, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'code', 'name')


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'name', 'created_at', 'updated_at')


class ThingSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=False, read_only=True)
    type = TypeSerializer(many=False, read_only=True)

    class Meta:
        model = Thing
        fields = (
            'id', 'name', 'home', 'type', 'status', 'description', 'thing_row', 'thing_column',
            'created_at',
            'updated_at')


class HomeIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Home
        fields = ('id',)


class ThingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = (
            'id', 'name', 'home', 'type', 'status', 'description', 'thing_row', 'thing_column',
            'created_at',
            'updated_at')

    # def create(self, validated_data):
    #     home_id = validated_data.pop('home')['id']
    #     home_instance = Home.objects.get(id=home_id)
    #     thing_instance = Thing.objects.create(home=home_instance, **validated_data)
    #     return thing_instance
    #
    # def update(self, instance, validated_data):
    #     thing_instance = Thing.objects.get(id=instance.id)
    #     return thing_instance
