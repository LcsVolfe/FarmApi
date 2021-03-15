from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.city


class Owner(models.Model):
    active = models.BooleanField(default=True)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    # cnpj = models.CharField(max_length=100, null=True, blank=True)
    # cpf = models.CharField(max_length=100, null=True, blank=True)
    # email = models.EmailField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # phone = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Farm(models.Model):
    active = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    TYPE = (
        (0, 'Tipo 1'),
        (1, 'Tipo 2'),
        (2, 'Tipo 3')
    )
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    type = models.IntegerField(choices=TYPE, default=0)
    fuel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class MachineVeclocity(models.Model):
    active = models.BooleanField(default=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    march = models.IntegerField()


class MachineEquipment(models.Model):
    TYPE = (
        (0, 'Tipo 1'),
        (1, 'Tipo 2'),
        (2, 'Tipo 3')
    )
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    qty = models.IntegerField()
    exits = models.IntegerField()
    exit_capacity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    exit_reach = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True)
    reservoil = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type = models.IntegerField(choices=TYPE, default=0)

    def __str__(self):
        return self.name


class Harvest(models.Model):
    active = models.BooleanField(default=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    result = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    machines = models.ManyToManyField(Machine)


class Activity(models.Model):
    active = models.BooleanField(default=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


class Planting(models.Model):
    active = models.BooleanField(default=True)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    seed = models.CharField(max_length=100, null=True, blank=True)


class SamplingPoint(models.Model):
    active = models.BooleanField(default=True)
    accuracy = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    planting = models.ForeignKey(Planting, on_delete=models.CASCADE, null=True)
    start = models.DateTimeField(null=True, blank=True)
    grid = models.IntegerField(null=True, blank=True)


class ClinicalAnalysis(models.Model):
    active = models.BooleanField(default=True)
    nLab = models.CharField(max_length=100, null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    argila = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ph = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    smp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    p = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    k = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ctc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    samplingPoint = models.ForeignKey(SamplingPoint, on_delete=models.CASCADE, null=True)


class PlantingArea(models.Model):
    active = models.BooleanField(default=True)
    accuracy = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    planting = models.ForeignKey(Planting, on_delete=models.CASCADE, null=True)


class CompactionPoint(models.Model):
    active = models.BooleanField(default=True)
    SamplingPoint = models.ForeignKey(SamplingPoint, on_delete=models.CASCADE, null=True)
    depth = models.IntegerField(null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)