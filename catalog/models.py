from django.db import models

# Create your models here.

class Location(models.Model):
    """
    Model representing a student location (e.g. Science Fiction, Non Fiction).
    """
    city = models.CharField(max_length=50,
                            help_text="Қаланың атын еңгізіңіз")
    region = models.CharField(max_length=50,
                            help_text="Қаланың районың еңгізіңіз")


    def get_absolute_url(self):
        """
        Returns the url to access a particular teacher and student instance.
        """
        return reverse('location-detail', args=[str(self.id)])
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.city

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Student(models.Model):
    """
    Model representing a student (but not a specific copy of a student).
    """
    FirstName = models.CharField(max_length=50, help_text="Есімің еңгізіңіз")
    LastName = models.CharField(max_length=50, help_text="Тегін еңгізіңіз")
    Email = models.CharField(max_length=50, help_text="Почтасын еңгізіңіз")
    date_of_birth = models.DateField(null=True, blank=True)
    Items = models.CharField(max_length=50, help_text="Пәндерің еңгізіңіз")
    Receipts = models.CharField(max_length=50, help_text="Максатын еңгізіңіз")
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because student can only have one teacher, but teachers can have multiple students
    # Student as a string rather than object because it hasn't been declared yet in the file.
    Phone = models.CharField('Phone', max_length=20,
                            help_text='20 саннан тұрады. Телефон нөмерін еңгізіңіз')
    Address = models.CharField('Address', max_length=50, help_text="Адресын еңгізіңіз")
    location = models.ManyToManyField(Location, help_text='Select a location for this student')

    # ManyToManyField used because location can contain many students. Students can cover many locations.
    # Location class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.FirstName + ' ' + self.LastName

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this employee.
        """
        return reverse('student-detail', args=[str(self.id)])

# Create your models here.

class Teacher(models.Model):
    """
    Model representing an teacher.
    """
    name = models.CharField(max_length=100, help_text="Аты-жөнің еңгізіңіз")
    Email = models.CharField(max_length=50, help_text="Почтасын еңгізіңіз")
    date_of_birth = models.DateField(null=True, blank=True)
    Items = models.CharField(max_length=50, help_text="Пәндерің еңгізіңіз")
    Phone = models.CharField('Phone', max_length=20,
                             help_text='20 саннан тұрады. Телефон нөмерін еңгізіңіз')
    Address = models.CharField('Address', max_length=50, help_text="Адресын еңгізіңіз")
    location = models.ManyToManyField(Location, help_text='Select a location for this teacher')

    # ManyToManyField used because location can contain many teachers. Teachers can cover many locations.
    # Location class has already been defined so we can specify the object above.
    class Meta:
        ordering = ["name"]


    def get_absolute_url(self):
        """
        Returns the url to access a particular teachers instance.
        """
        return reverse('teacher-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {0}'.format(self.name)



