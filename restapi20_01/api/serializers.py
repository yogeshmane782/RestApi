from rest_framework import serializers
from api.models import Student
class StudentSerializer(serializers.Serializer):
    rollno=serializers.ImageField()
    name=serializers.CharField(max_length=20)
    course=serializers.CharField(max_length=15)
    fee=serializers.FloatField()

    def create(self,data):
        return Student.objects.create(**data)
    def update(self,instance,validated_data):
        instance.rollno=validated_data.get('rollno')
        instance.name=validated_data.get('name',instance.name)
        instance.course=validated_data.get('course',instance.course)
        instance.fee=validated_data.get('fee',instance.fee)
        instance.save()
        return instance
