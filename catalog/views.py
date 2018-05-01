from django.shortcuts import render

# Create your views here.

from .models import Student, Teacher, Location
import datetime

def index(request):
    num_teachers = Teacher.objects.count()
    num_students = Student.objects.all().count()
    num_locations = Location.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    time = datetime.datetime.now()
    w_day = time.weekday()
    w_day = w_day
    day = time.day
    month = time.month
    year = time.year
    microsecond = time.microsecond
    second = time.second
    minute = time.minute
    hour = time.hour
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_students': num_students, 'num_teachers': num_teachers, 'num_locations': num_locations, 'num_visits': num_visits,
                 'weekday': w_day,
                 'hour': hour, 'minute': minute, 'second': second, 'microsecond': microsecond,
                 'day': day, 'month': month, 'year': year, },  # num_visits appended

    )

from django.views import generic


class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 2


class TeacherDetailView(generic.DetailView):
    model = Teacher


class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2


class StudentDetailView(generic.DetailView):
    model = Student

class LocationListView(generic.ListView):
    model = Location
    paginate_by = 2


class LocationDetailView(generic.DetailView):
    model = Location


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Location


class LocationCreate(CreateView):
    model = Location
    fields = '__all__'


class LocationUpdate(UpdateView):
    model = Location
    fields = ['city', 'region']


class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student


class StudentCreate(CreateView):
    model = Student
    fields = '__all__'


class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Teacher


class TeacherCreate(CreateView):
    model = Teacher
    fields = '__all__'


class TeacherUpdate(UpdateView):
    model = Teacher
    fields = '__all__'


class TeacherDelete(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers')
