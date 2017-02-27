"""feb15_schools_comezo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from feb15_schools_comezo.views import *
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^teacher-tagging/$', TemplateView.as_view(template_name="teacher_tagging.html"), name='teacher-tagging'),
    url(r'^student-teacher-upload/$', TemplateView.as_view(template_name="student_teacher_upload.html"), name=''),
    url(r'^test/$', TemplateView.as_view(template_name="test.html"), name=''),

    url(r'^success/$', TemplateView.as_view(template_name="success.html"), name='success'),
    #url(r'^exam-input/$', TemplateView.as_view(template_name="exam_input.html"), name=''),
    url(r'^school_register$', school_register, name='school-register'),
    url(r'^register/$', index, name='register'),
    url(r'^$', landing, name='landing'),
    url(r'^login/$', custom_login, name='login'),
    url(r'^login-redirect/$', login_redirect, name='login-redirect'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login/'}, name='logout'),
    url(r'^class-input/$', class_input, name='class-input'),
    url(r'^class-insert/$', class_insert, name='class-insert'),
    url(r'^section-input/$', section_input, name='section-input'),
    url(r'^section-insert/$', section_insert, name='section-insert'),
    url(r'^subject-input/$', subject_input, name='subject-input'),
    url(r'^add-subject/$', add_subject, name='add-subject'),
    url(r'^subject-insert/$', subject_insert, name='subject-insert'),
    url(r'^exam-input/$', exam_input, name='exam-input'),
    url(r'^add-exam/$', add_exam, name='add-exam'),
    url(r'^exam-insert/$', exam_insert, name='exam-insert'),
    url(r'^student/excel/$', StudentExcelView.as_view(), name='student_excel'),
    url(r'^teacher/excel/$', TeacherExcelView.as_view(), name='teacher_excel'),
    url(r'^student/excel/update/$', student_excel_upload, name='student_excel_update'),
    url(r'^teacher/excel/update/$', teacher_excel_upload, name='teacher_excel_update'),
    url(r'^teacher-tagging/$', teacher_tagging, name='teacher-tagging'),
    url(r'^subject-teacher/excel/$', SubjectTeacherExcelView.as_view(), name='subject_teacher_excel'),
    url(r'^subject-teacher/excel/update/$', subject_teacher_excel_upload, name='subject_teacher_excel_update'),
    url(r'^add-teacher-tagging/$', add_teacher_tagging, name='add-teacher-tagging'),
    url(r'^class/teacher/excel/$', ClassTeacherExcelView.as_view(), name='class_teacher_excel'),
    url(r'^class-teacher/excel/update/$', class_teacher_excel_upload, name='class_teacher_excel_update'),
    url(r'^class-teacher-tagging/$', class_teacher_tagging, name='class-teacher-tagging'),

]
