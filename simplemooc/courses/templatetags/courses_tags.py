from django.template import Library

register = Library()

from simplemooc.courses.models import Enrollment

@register.inclusion_tag('templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context

@register.simple_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)


@register.inclusion_tag('templatetags/my_courses_dash.html')
def my_courses_dash(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context