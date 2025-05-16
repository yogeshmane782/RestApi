from api.models import Student
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    rollno=serializers.IntegerField()
    name=serializers.CharField(max_length=20)
    course=serializers.charField(max_length=15)
    fee=serializers.FloatField()

    def create(self,data):
        return Student.objects.create(**data)
    def update(self,instance,stud_upd):
        instance.rollno=stud_upd.get('rollno')
        instance.name=stud_upd.get('name')
        instance.course=stud_upd.get('course')
        instance.fee=stud_upd.get('fee')
        instance.save()
        return instance