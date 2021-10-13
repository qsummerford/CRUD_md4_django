from django.db import models

# Create your models here.
class Store(models.Model):
    food = models.TextField()
    company = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()

def create_store(name, company, phone, is_favorite):
    store = Store(name=name, company=company, phone=phone, is_favorite=is_favorite)
    store.save()
    return store

def all_food():
    return Store.objects.all()

def find_food_by_name(food):
    try:
        return Store.objects.get(food=food)
    except Store.DoesNotExist:
        return None

def fav_food():
    return Store.objects.filter(is_favorite=True)

def update_company(food, new_company):
    store = find_food_by_name(food)
    store.company = new_company
    store.save()

def delete_food(food):
    store = find_food_by_name(food)
    store.delete()