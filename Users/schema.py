import graphene
from graphene_django import DjangoObjectType
from .models import Student, Grade, Course, CoursePerStudent


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        
        
class GradeType(DjangoObjectType):
    class Meta:
        model = Grade
        
        
class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class CousePerStudentType(DjangoObjectType):
    class Meta:
        model = CoursePerStudent
        
        
class Query(graphene.ObjectType):
    students  =  graphene.List(StudentType)
    grade = graphene.List(GradeType)
    course = graphene.List(CourseType)
    course_per_student = graphene.List(CousePerStudentType)
    
    def resolve_students(self,info,**kwargs):
        return Student.objects.all()
    
    def resolve_grade(self,info,**kwargs):
        return Grade.objects.all()
    
    def resolve_course(self,info,**kwargs):
        return Course.objects.all()
    
    def resolve_course_per_student(self,info,**kwargs):
        return CoursePerStudent.objects.all()