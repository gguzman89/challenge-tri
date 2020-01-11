from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=30)
    # level = models.ForeignKey(Course, related_name='levels', )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    language_code = models.CharField(max_length=2)
    level_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    _level = models.ForeignKey(Level, related_name='courses', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name