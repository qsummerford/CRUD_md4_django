from django.test import TestCase
from app import models

class TestStore(TestCase):
    def test_can_create_food(self):
        store = models.create_contact("Tacos", "El Agave", "6622347654", True)

        self.assertEqual(store.id, 1)
        self.assertEqual(store.food, "Tacos")
        self.assertEqual(store.company, "El Agave")
        self.assertEqual(store.phone, "6622347654")
        self.assertTrue(store.is_favorite)

    def test_can_view_all_food_at_once(self):
        food_data = [
            {
                "food": "Tacos",
                "company": "El Agave",
                "phone": "6622347654",
                "is_favorite": True,
            },
            {
                "food": "P5",
                "company": "Tequilas",
                "phone": "6622345555",
                "is_favorite": True,
            },
            {
                "food": "Fried Beans",
                "company": "El Pueblo",
                "phone": "6625448047",
                "is_favorite": False
            }
        ]

        for data in food_data:
            models.create_store(
                data["food"],
                data["company"],
                data["phone"],
                data["is_favorite"]
            )

        stores = models.all_food()

        self.assertEqual(len(stores), len(food_data))

        food_data = sorted(food_data, key=lambda c: c.name)
        for bottle, wrappers in zip(food_data, stores):
            self.assertEqual(bottle["food"], wrappers.food)
            self.assertEqual(bottle["company"], wrappers.company)
            self.assertEqual(bottle["phone"], wrappers.phone)
            self.assertEqual(bottle["is_favorite"], wrappers.is_favorite)

    def test_can_search_by_name(self):
        food_data = [
            {
                "food": "Tacos",
                "company": "El Agave",
                "phone": "6622347654",
                "is_favorite": True,
            },
            {
                "food": "P5",
                "company": "Tequilas",
                "phone": "6622345555",
                "is_favorite": True,
            },
            {
                "food": "Fried Beans",
                "company": "El Pueblo",
                "phone": "6625448047",
                "is_favorite": False
            }
        ]

        for data in food_data:
            models.create_store(
                data["name"],
                data["email"],
                data["phone"],
                data["is_favorite"]
            )

        self.assertIsNone(models.find_food_by_name("poop"))

        store = models.find_food_by_name("Tacos")

        self.assertIsNotNone(store)
        self.assertEqual(store.company, "El Agave")

    def test_can_view_favorites(self):
        food_data = [
            {
                "food": "Tacos",
                "company": "El Agave",
                "phone": "6622347654",
                "is_favorite": True,
            },
            {
                "food": "P5",
                "company": "Tequilas",
                "phone": "6622345555",
                "is_favorite": True,
            },
            {
                "food": "Fried Beans",
                "company": "El Pueblo",
                "phone": "6625448047",
                "is_favorite": False
            }
        ]

        for data in food_data:
            models.create_store(
                data["name"],
                data["company"],
                data["phone"],
                data["is_favorite"]
            )

        self.assertEqual(len(models.fav_food()), 2)

    def test_can_update_food_company(self):
        food_data = [ 
            {
                "food": "Tacos",
                "company": "El Agave",
                "phone": "6622347654",
                "is_favorite": True,
            },
            {
                "food": "P5",
                "company": "Tequilas",
                "phone": "6622345555",
                "is_favorite": True,
            },
            {
                "food": "Fried Beans",
                "company": "El Pueblo",
                "phone": "6625448047",
                "is_favorite": False
            }
        ]

        for data in food_data:
            models.create_store(
                data["name"],
                data["email"],
                data["phone"],
                data["is_favorite"]
            )
        
        models.update_company("Tacos", "Taco Shop")

        self.assertEqual(
            models.find_food_by_name("Tacos").company, "Taco Shop"
        )

    def test_can_delete_contact(self):
        food_data = [ 
             {
                "food": "Tacos",
                "company": "El Agave",
                "phone": "6622347654",
                "is_favorite": True,
            },
            {
                "food": "P5",
                "company": "Tequilas",
                "phone": "6622345555",
                "is_favorite": True,
            },
            {
                "food": "Fried Beans",
                "company": "El Pueblo",
                "phone": "6625448047",
                "is_favorite": False
            }
        ]

        for data in food_data:
            models.create_store(
                data["food"],
                data["company"],
                data["phone"],
                data["is_favorite"]
            )

        models.delete_food("P5")

        self.assertEqual(len(models.all_food()), 2)