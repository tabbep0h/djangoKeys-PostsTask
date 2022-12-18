from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Название", max_length=100)
    url = models.CharField("Ссылка", max_length=100)
    content = models.TextField("Контент", max_length=1000)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, default=None)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, default=None)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"