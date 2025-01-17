import pytest
from django.urls import reverse
from app.models import Musician, Category, TagPost, Alive

@pytest.mark.django_db
def test_musician_str():
    category = Category.objects.create(name="Rock", slug="rock")
    user = User.objects.create_user(username="testuser", password="password")
    musician = Musician.objects.create(
        title="John Lennon",
        slug="john-lennon",
        content="Famous musician",
        cat=category,
        user=user
    )
    assert str(musician) == "John Lennon"

@pytest.mark.django_db
def test_category_str():
    category = Category.objects.create(name="Rock", slug="rock")
    assert str(category) == "Rock"

@pytest.mark.django_db
def test_tagpost_str():
    tag = TagPost.objects.create(tag="Legend", slug="legend")
    assert str(tag) == "Legend"

@pytest.mark.django_db
def test_alive_str():
    alive = Alive.objects.create(died="2020", age=40)
    assert str(alive) == "2020"

@pytest.mark.django_db
def test_musician_get_absolute_url():
    category = Category.objects.create(name="Rock", slug="rock")
    user = User.objects.create_user(username="testuser", password="password")
    musician = Musician.objects.create(
        title="John Lennon",
        slug="john-lennon",
        content="Famous musician",
        cat=category,
        user=user
    )
    expected_url = reverse('post', kwargs={'post_slug': "john-lennon"})
    assert musician.get_absolute_url() == expected_url