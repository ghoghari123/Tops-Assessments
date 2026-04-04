from rest_framework.throttling import UserRateThrottle


class StudentThrottle(UserRateThrottle):
    scope = 'student'


class CourseThrottle(UserRateThrottle):
    scope = 'course'