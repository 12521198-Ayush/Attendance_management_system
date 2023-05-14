from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        student_id = request.data.get('student_id')

        try:
            student = Student.objects.get(student_id=student_id)
            student.delete()

            return Response({
                'status': 200,
                'message': 'Student deleted successfully',
            })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Student not found',
                'error': 'The student with the provided ID does not exist'
            })

class AttendanceUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        student_id = request.data.get('student_id')
        attendance_percentage = request.data.get('attendance_percentage')

        try:
            student = Student.objects.get(student_id=student_id)
            student.attendance_percentage = attendance_percentage
            student.save()
            
            return Response({
                'status': 200,
                'message': 'Attendance updated successfully',
                'data': {
                    'student_id': student.student_id,
                    'attendance_percentage': student.attendance_percentage
                }
            })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Student not found',
                'error': 'The student with the provided ID does not exist'
            })


class ChangePasswordView(APIView):
    def patch(self, request):
        student_id = request.data.get('student_id')
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        try:
            student = Student.objects.get(student_id=student_id)
            if student.password == current_password:
                student.password = new_password
                student.save()

                return Response({
                    'status': 200,
                    'message': 'Password changed successfully',
                })
            else:
                return Response({
                    'status': 401,
                    'message': 'Unauthorized',
                    'error': 'Incorrect current password'
                })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Student not found',
                'error': 'The student with the provided ID does not exist'
            })

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        serialized_data = serializer.data
        for data in serialized_data:
            data.pop('password', None)

        return Response({
            'status': 200,
            'message': 'Success',
            'data': serialized_data
        })

class StudentCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 201,
                'message': 'Student created successfully',
                'data': serializer.data
            })
        
        return Response({
            'status': 400,
            'message': 'Invalid data',
            'errors': serializer.errors
        })
    

class StudentDetailView(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        password = request.data.get('password')
        try:
            student = Student.objects.get(student_id=student_id)
            print(student.student_id)
            print(student.password)
            if student.password == password:
                serializer = StudentSerializer(student)
                return Response({
                    'status': 200,
                    'message': 'Success',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 401,
                    'message': 'Unauthorized',
                    'error': 'Incorrect password'
                })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Not found',
                'error': 'Student not found'
            })

class StudentDeleteAllView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        try:
            Student.objects.all().delete()
            return Response({
                'status': 200,
                'message': 'All students deleted successfully',
            })
        except Exception as e:
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'error': str(e),
            })
