from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self):
        return super().setUp()

    def make_category(self):
        return Category.objects.create(name='Category')

    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
        title='Recipe Title',
        description='Recipe Description',
        slug='recipe-title',
        preparation_time=30,
        preparation_time_unit='minutes',
        servings=4,
        servings_unit='people',
        preparation_steps='Preparation steps here',
        preparation_steps_html=False,
        is_published=True,
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-title',
            preparation_time=30,
            preparation_time_unit='minutes',
            servings=4,
            servings_unit='people',
            preparation_steps='Preparation steps here',
            preparation_steps_html=False,
            is_published=True,
        )
