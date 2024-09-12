from django.db import models

# Create your models here.


class Parent(models.Model):
    """
involvement int REFERENCES involvements(id), -- участие (ШМ, институт, вожатая, гостевой, выбыла, наставник, стажер, ...)
feedback boolean, -- отзыв?
"""
    DAD = "Папа"
    MOM = "Мама"

    PARENT_CHOICES = [
        (DAD, "Папа"),
        (MOM, "Мама")
    ]

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.CharField(max_length=50, choices=PARENT_CHOICES, default=MOM, verbose_name='Пол')
    phone = models.PositiveBigIntegerField(verbose_name='Телефон')

    def __str__(self):
        sex_ = 'Папа' if self.sex else 'Мама'
        return f'{sex_}: {self.name} {self.surname}'

    class Meta:
        verbose_name = 'родитель'
        verbose_name_plural = 'родители'


class Hero(models.Model):
    """
mother_id int REFERENCES parents(id) NOT NULL,
father_id int REFERENCES parents(id),
mentor_id int REFERENCES mentors(id),
cell_id int REFERENCES cells(id), -- ячейка (локация, время тренировки)
new boolean,
first_training_date date,
planned_first_training_date date,
profile boolean, -- анкета
photo text
"""

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.BooleanField(verbose_name='Пол')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'Герой: {self.name} {self.surname}'

    class Meta:
        verbose_name = 'герой'
        verbose_name_plural = 'герои'
