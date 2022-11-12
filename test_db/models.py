from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f'Name of category is {self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TestData(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked') #NEW
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author') #NEW
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    population = models.IntegerField()
    mayor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mayor_cities')
    citizen = models.ManyToManyField(User, through='TestDataRelation', related_name='citizen_cities')

    def __str__(self):
        return f'Id {self.id}: {self.title} | {self.population}'

    class Meta:
        verbose_name = 'Запись в бд'
        verbose_name_plural = 'Записи в бд'


class TestDataRelation(models.Model):
    RATE_CHOICES = (
        (1, 'fine'),
        (2, 'good'),
        (3, 'amazing')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(TestData, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    city_on_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    class Meta:
        verbose_name = 'Оценка пользователя'
        verbose_name_plural = 'Оценки пользователя'

    def __str__(self):
        return f'{self.user.username}: {self.city.title} RATE {self.rate}/3'


class Like(models.Model):
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(TestData, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return f'Like on {self.post.title} by {self.user.username}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'






