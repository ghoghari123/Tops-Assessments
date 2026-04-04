from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Student


@receiver(m2m_changed, sender=Student.courses.through)
def student_enrolled(sender, instance, action, **kwargs):
    if action == "post_add":
        print(f"{instance.name} enrolled in new course(s)")