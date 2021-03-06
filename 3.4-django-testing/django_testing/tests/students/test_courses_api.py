import pytest
from django.urls import reverse
from students.models import Course


# Получение одного курса
@pytest.mark.django_db
def test_get_courses(client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(course[0].id,))
    resp = client.get(url)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert course[0].id == resp_json.get('id')
    assert course[0].name == resp_json.get('name')


# Получение списка
@pytest.mark.django_db
def test_get_courses(client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = client.get(url)

    assert resp.status_code == 200
    assert len(resp.data) == 3


# Фильтрация по id
@pytest.mark.django_db
def test_filters_courses_id(client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = client.get(url, data={'id': courses[0].id})
    resp_json = resp.json()

    assert resp.status_code == 200
    assert courses[0].id == resp_json[0].get('id')


# Фильтр по названию
@pytest.mark.django_db
def test_filters_courses_name(client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = client.get(url, data={'name': courses[0].name})
    resp_json = resp.json()

    print(resp_json)

    assert resp.status_code == 200
    assert courses[0].name == resp_json[0].get('name')


# Создание
@pytest.mark.django_db
def test_create_courses(client):
    data = {
        'name': 'Python'
    }
    url = reverse('courses-list')
    resp = client.post(url, data=data)

    assert resp.status_code == 201
    assert resp.data['name'] == 'Python'


# Обновление
@pytest.mark.django_db
def test_update_courses(client, course_factory):
    data = {
        'name': 'Python'
    }
    courses = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(courses[0].id,))
    resp = client.patch(url, data=data)

    assert resp.status_code == 200
    assert resp.data['name'] == 'Python'


# Удаление
@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    courses = course_factory(_quantity=3)
    counts_objects = Course.objects.count()

    url = reverse('courses-detail', args=(courses[0].id,))
    resp = client.delete(url)

    assert resp.status_code == 204
    assert counts_objects - 1 == Course.objects.count()