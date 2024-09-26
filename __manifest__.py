{
    "name": "Vroom Vroom Car Rental Service",
    "version": "2.0",
    "author": "Nikhil K.",
    "category": "Management",
    "summary": "A inherited version of Car Rental Management System",
    "depends": ["base","sale"],
    "installable": True,
    "application": True,
    "data": ["data/car_model_sequence.xml", "views/people.xml", "views/car_model_view.xml","views/car_owners_view.xml", "views/borrower_view.xml", "views/set_can_be_purchased_view.xml", "views/setting_view.xml", "report/professional_template.xml", "report/CRM_report.xml","views/menu.xml", "security/ir.model.access.csv"]
}