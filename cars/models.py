from django.db import models

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.equipment


class Car(models.Model):

    
    ENGINE_TYPES = [
        ("benzyna", "Benzynowy"),
        ("diesel", "Diesel"),
        ("elektryk", "Elektryczny"),
        ("hybryda", "Hybrydowy")
    ]
    GEARBOX_TYPES = [
        ("manual", "Manualna"),
        ("automat", "Automatyczna")
    ]
    BODY_TYPES = [
        ("hatchbeck", "hatchback"),
        ("sedan", "kareta"),
        ("combi", "combi"),
        ("suv", "SUV"),
        ("coupe", "coupe"),
    ]
    CLASSIFICATIONS = [
        ("a", "mini"),
        ("b", "miejskie"),
        ("c", "kompaktowe"),
        ("d", "rodzinne"),
        ("e", "wyższośrednie"),
        ("f", "luksusowe"),
        ("s", "sportowe"),
        ("h", "kabriolety"),
        ("i", "terenowe"),
        ("m", "van")
    ]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPES)
    seats_count = models.PositiveSmallIntegerField()
    gearbox_type = models.CharField(max_length=50, choices=GEARBOX_TYPES)
    mileage_limit = models.PositiveIntegerField()
    doors_count = models.PositiveIntegerField()
    engine_power = models.PositiveSmallIntegerField()
    engine_capacity = models.PositiveSmallIntegerField()
    fuel_usage = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50, choices=BODY_TYPES)
    classification = models.CharField(max_length=50, choices=CLASSIFICATIONS)
    value = models.PositiveBigIntegerField()
    availability = models.BooleanField()
    trunk_capacity = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.brand + " " + self.model
    
    @staticmethod
    def