import pytest
from model import Musician, Category, TagPost, Alive
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_musician_with_category_and_tags():
    category = Category.objects.create(name="Jazz", slug="jazz")
    user = User.objects.create_user(username="testuser", password="password")
    tag1 = TagPost.objects.create(tag="Saxophone", slug="saxophone")
    tag2 = TagPost.objects.create(tag="Improvisation", slug="improvisation")

    musician = Musician.objects.create(
        title="Charlie Parker",
        slug="charlie-parker",
        content="Famous jazz musician",
        cat=category,
        user=user
    )
    musician.tags.set([tag1, tag2])

    assert musician.cat == category
    assert musician.tags.count() == 2
    assert tag1 in musician.tags.all()
    assert tag2 in musician.tags.all()


@pytest.mark.django_db
def test_create_musician_with_alive():
    alive = Alive.objects.create(died="2005", age=60)
    category = Category.objects.create(name="Classical", slug="classical")
    user = User.objects.create_user(username="testuser", password="password")

    musician = Musician.objects.create(
        title="Beethoven",
        slug="beethoven",
        content="Classical musician",
        cat=category,
        user=user,
        alive=alive
    )

    assert musician.alive == alive
    assert musician.alive.died == "54"