from rest_framework import serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        many=True,
        write_only=True,
        source='courses'
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'age', 'courses', 'course_ids', 'created_at']

    def validate_age(self, value):
        if value < 5:
            raise serializers.ValidationError("Age must be greater than 5")
        return value