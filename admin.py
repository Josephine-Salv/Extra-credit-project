from django.contrib import admin

#Register models
from django.contrib import admin
from .models import Flight, Passenger

#Register flight model
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin', 'destination', 'departure', 'arrival', 'capacity')
    search_fields = ('flight_number', 'origin', 'destination')
    list_filter = ('departure', 'arrival')

#Register Passenger model
@admin.register(Passenger)
class PasseengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'flight')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('flight')
