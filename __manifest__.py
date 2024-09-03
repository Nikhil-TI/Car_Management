{
    'name': "Car Management System",
    "version": "1.0",
    "category": "Management",
    "summary": "Module for managing cars",
    "author":"Nikhil Kumar",
    "depends": ["base"],
    "installable": True,
    "application": True,
    "data": ["views/car_views.xml", "views/borrower_views.xml", "views/owner_views.xml", "views/car_rental_view.xml", "views/menus.xml", "security/ir.model.access.csv"],
    # "data": ["views/carView.xml", "security/ir.model.access.csv"],
    # "data": ["data/borrower.details.csv","data/car.owner.csv", "data/car.management.csv", "views/carView.xml","security/ir.model.access.csv"]
}