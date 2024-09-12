import datetime

from django.db import models

# Create your models here.


class Parent(models.Model):
    """
involvement int REFERENCES involvements(id), -- участие (ШМ, институт, вожатая, гостевой, выбыла, наставник, стажер, ...)
feedback boolean, -- отзыв?

участие = список записей: тип(ШМ, СД, вож, наст), дата с, дата по
или статус

"""
    DAD = "Папа"
    MOM = "Мама"
    GR_M = "Бабушка"
    GR_F = "Дедушка"
    MOTHER_IN_CLASS = "Вожатая класса"

    PARENT_CHOICES = [
        (DAD, "Папа"),
        (MOM, "Мама"),
        (GR_M, "Бабушка"),
        (GR_F, "Дедушка"),
        (MOTHER_IN_CLASS, "Вожатая класса")
    ]

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.CharField(max_length=50, choices=PARENT_CHOICES, default=MOM, verbose_name='Пол')
    phone = models.PositiveBigIntegerField(verbose_name='Телефон')

    # team = models.JSONField(verbose_name='Участие')
    # участие = список записей: тип(ШМ, СД, вож, наст), дата с, дата по

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

    BOY = "Мальчик"
    GIRL = "Девочка"

    HERO_CHOICES = [
        (BOY, "Мальчик"),
        (GIRL, "Девочка")
    ]

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.CharField(max_length=50, choices=HERO_CHOICES, verbose_name='Пол')
    birth_date = models.DateField(verbose_name='Дата рождения')

    # team = models.JSONField(verbose_name='Отряд')
    # отряд = список записей: тип(мощные, отв, с мамой, пред_к, командиры), дата с, дата по

    # рассылки клиентам many to many
    # ребята в отряды. нужны виды отрядов и связь.

    # сущность "курс" или "статус" или "состояние, настрой"
    # ребенок, отряд, с, по
    # родитель, программа, с, по

    def __str__(self):
        return f'Герой: {self.name} {self.surname}'

    class Meta:
        verbose_name = 'герой'
        verbose_name_plural = 'герои'


class Program(models.Model):
    """
involvements
name varchar(100) -- участие (ШМ, институт, вожатая, гостевой, выбыла, наставник, ...

products
description varchar(100), -- 4 тренировки, 12 тренировок, слёт, ...
price int

"""

    PROGRAM_CHOICES = [
        ("Сила Дружбы", "Сила Дружбы"),
        ("Школа Мам", "Школа Мам"),
        ("Институт", "Институт"),
        ("Вожатая", "Вожатая"),
        ("Гостевой", "Гостевой"),
        ("Выбыли", "Выбыли"),
        ("Наставник", "Наставник"),
        ("Стажёр", "Стажёр"),
        ("Интересуется", "Интересуется"),
        ("Не интересуется", "Не интересуется"),
    ]

    parent = models.ForeignKey(Parent, verbose_name='Родитель', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=PROGRAM_CHOICES, verbose_name='Вид программы')
    start_from = models.DateField(verbose_name='с')
    stop_at = models.DateField(verbose_name='по', null=True, blank=True)

    def __str__(self):
        return f'{self.parent} {self.type} {"+" if self.is_active() else "-"}'

    def is_active(self):
        today = datetime.datetime.now()
        return (self.start_from < today) and (self.stop_at is None)

    class Meta:
        verbose_name = 'программа'
        verbose_name_plural = 'программы'


# сущность "курс" или "статус" или "состояние, настрой"
# ребенок, отряд, с, по
# родитель, программа, с, по


class Team(models.Model):

    TEAM_CHOICES = [
        ("Мощный", "Мощный"),
        ("Отважный", "Отважный"),
        ("Отряд мам", "Отряд мам"),
        ("Пред.командир", "Пред.командир"),
        ("Командир", "Командир"),
        ("Выбыл", "Выбыл"),
    ]

    hero = models.ForeignKey(Hero, verbose_name='Герой', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TEAM_CHOICES, verbose_name='Вид отряда')
    start_from = models.DateField(verbose_name='с')
    stop_at = models.DateField(verbose_name='по', null=True, blank=True)

    def __str__(self):
        return f'{self.hero} {self.type} {"+" if self.is_active() else "-"}'

    def is_active(self):
        today = datetime.datetime.now()
        return (self.start_from < today) and (self.stop_at is None)

    class Meta:
        verbose_name = 'отряд'
        verbose_name_plural = 'отряды'
