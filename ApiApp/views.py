from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Muscles, Exercice
from .serializers import MusclesSerializer, ExerciceSerializer


@csrf_exempt
def muscleApi(request, id=0):
    if request.method=='GET':
        muscles = Muscles.objects.all()
        muscles_serializer = MusclesSerializer(muscles, many=True)
        return JsonResponse(muscles_serializer.data, safe=False)
    elif request.method=='POST':
        muscle_data=JSONParser().parse(request)
        muscle_serializer = MusclesSerializer(data=muscle_data)
        if muscle_serializer.is_valid():
            muscle_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        muscle_data = JSONParser().parse(request)
        muscle = Muscles.objects.get(MuscleID=muscle_data['MuscleID'])
        muscle_serializer = MusclesSerializer(muscle, data=muscle_data)
        if muscle_serializer.is_valid():
            muscle_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        muscle = Muscles.objects.get(MuscleID=id)
        muscle.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    
@csrf_exempt
def exerciseApi(request, id=1):
    if request.method=='GET':
        exercises = Exercice.objects.all()
        exercises_serializer = ExerciceSerializer(exercises, many=True)
        return JsonResponse(exercises_serializer.data, safe=False)
    elif request.method=='POST':
        exercise_data=JSONParser().parse(request)
        exercise_serializer = ExerciceSerializer(data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        exercise_data = JSONParser().parse(request)
        exercise = Exercice.objects.get(ExerciceID=exercise_data['ExerciceID'])
        exercise_serializer = ExerciceSerializer(exercise, data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method=='DELETE':
        exercise = Exercice.objects.get(ExerciceID=id)
        exercise.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)