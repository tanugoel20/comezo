import datetime
import hashlib
import uuid
from os.path import splitext
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


def get_ga_hash(self):
    return hashlib.md5(str(self.id).encode('utf-8')).hexdigest()


def is_comezo(self):
    return self.email.endswith("@comezo.in")


User.add_to_class('ga_hash', get_ga_hash)
User.add_to_class('is_comezo', is_comezo)



class school_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='school_profile')
    school_id = models.CharField(max_length=200, unique=True)
    school_name = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    start_class = models.CharField(max_length=200, null=True)
    end_class = models.CharField(max_length=200, null=True)
    section_class1 = models.IntegerField(null=True)
    section_class2 = models.IntegerField(null=True)
    section_class3 = models.IntegerField(null=True)
    section_class4 = models.IntegerField(null=True)
    section_class5 = models.IntegerField(null=True)
    section_class6 = models.IntegerField(null=True)
    section_class7 = models.IntegerField(null=True)
    section_class8 = models.IntegerField(null=True)
    section_class9 = models.IntegerField(null=True)
    section_class10 = models.IntegerField(null=True)
    section_class11 = models.IntegerField(null=True)
    section_class12 = models.IntegerField(null=True)

def create_school_profile(**kwargs):
    user = kwargs["instance"]

    if kwargs["created"] or user.school_profile is None:
        profile = school_info()
        user.school_profile = profile
        profile.user = user
        profile.save()

    return user.school_profile


post_save.connect(create_school_profile, sender=User)


class subjects(models.Model):
    subject_name = models.CharField(max_length=200)

    class Meta:
        pass


class subject_class(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)
    subject_id = models.ForeignKey(subjects, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=200)

    class Meta:
        pass


class exams(models.Model):
    exam_type = models.CharField(max_length=200)

    class Meta:
        pass


class exam_class(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200, null=True)
    exam_id = models.ForeignKey(exams, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=200)

    class Meta:
        pass


class student_info(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=200, null=True)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)
    admission_no = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    doj = models.CharField(max_length=200)
    parent_name = models.CharField(max_length=200)
    parent_contact = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        pass


class marksheet(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)
    subject_marks = models.CharField(max_length=200)
    exam_type = models.CharField(max_length=200)

    class Meta:
        pass


class attendance(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    student_id = models.ForeignKey(student_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)
    days_present = models.IntegerField(null=True)
    days_absent = models.IntegerField(null=True)

    class Meta:
        pass


class teacher_info(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200, null=True)
    teacher_id = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, null=True)

    class Meta:
        pass


class teacher_subject(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(teacher_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    class Meta:
        pass


class class_teacher(models.Model):
    school_id = models.ForeignKey(school_info, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(teacher_info, on_delete=models.CASCADE)
    class_id = models.CharField(max_length=200)
    section_id = models.CharField(max_length=200)

    class Meta:
        pass


