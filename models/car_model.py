from odoo import models, fields

class Car(models.Model):
    _name = "car.management"
    _description = "Car Management"

    #Car name
    model = fields.Char(string="Car Model", required=True)

    # Original owner
    owner_id = fields.Many2one('car.owner', string="Owner")

    # Renter of the car
    borrower_id = fields.Many2one('borrower.details', string="Borrower")

    #color
    color = fields.Char(string="Color")

    #made by
    manufacturer = fields.Char(string="Manufacturer", required=True)

    #license plate
    license = fields.Char(string="License Plate", required=True)

    #year of manufacturing
    YOM = fields.Integer(string="Year of Manufacturing", required=True)

    # #last day of service
    service = fields.Date(string="Lase Date of Service", required=True)
    
    # milage
    mileage = fields.Float(string="Mileage")

    #status
    status = fields.Char(string="Status")
