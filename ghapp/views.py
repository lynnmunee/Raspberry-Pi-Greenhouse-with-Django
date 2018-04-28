from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import SensorData, ActivityMeta
#from .GHMCS_OO import GreenhouseSystem as GreenHouse

def index(request):
	return render(request, 'ghapp/index.html')

def control_panel(request, command):
	pass

def system_preview(request):
	'''
	if request.user.is_authenticated:
		greenhouse = GreenHouse()
		activities_qs = list(ActivityMeta.objects.all())[:3]
		context = {
			'temperature':str(greenhouse.get_temperature()),
			'humidity':str(greenhouse.get_humidity()),
			'soil_moisture':str(greenhouse.get_soil_moisture()),
			'activities':activities_qs
		}
		rendered = render(request, 'ghapp/system_preview.html', context=context)
	else:
		rendered = render(request, 'ghapp/index.html')
	return rendered

	'''
	if request.user.is_authenticated:
		sensor_qs = list(SensorData.objects.all())[0]
		activities_qs = list(ActivityMeta.objects.all())[:3]
		context = {
			'temperature':str(sensor_qs.temperature),
			'humidity':str(sensor_qs.humidity),
			'soil_moisture':str(sensor_qs.get_soil_moisture_state_display()),
			'activities':activities_qs
		}
		rendered = render(request, 'ghapp/system_preview.html', context=context)
	#'''