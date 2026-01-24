from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationSerializer, RegisterSerializer

from django.contrib.auth.models import User
from .models import Application, Job

from .serializers import JobSerializer


@api_view(["GET"])
def hello_api(request):
    return Response({"message": "hello from Django API", "status": "ok"})


@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "user registered", "status": "ok"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def basic_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    # Authentication logic here
    try:
        user = User.objects.get(username=username, password=password)
        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "message": "Login success..!!",
            },
            status=status.HTTP_200_OK,
        )
    except User.DoesNotExist:
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def apply_job(request):
    serializer = ApplicationSerializer(data=request.data)
    # Check if user has already applied for the job
    if Application.objects.filter(
        job_id=request.data.get("job"), applicant_id=request.data.get("applicant")
    ).exists():
        return Response(
            {"message": "You have already applied for this job."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Application submitted successfully"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
