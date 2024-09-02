from odoo import models, fields, api

class Car(models.Model):
    _name = "car.management"
    _description = "Car Management"
    _rec_name = "model"

    #Car name
    model = fields.Char(string="Car Model", required=True)

    #image of the car
    image = fields.Image(string="Image")

    # Original owner
    owner_id = fields.Many2one('car.owner', string="Owner")
    #owners email
    owner_id_email = fields.Char(string="Owner's Email", related="owner_id.email")

    # Renter of the car
    borrower_id = fields.Many2one('borrower.details', string="Borrower")
    #Renters email
    borrower_id_email = fields.Char(string="Borrower's email",related='borrower_id.email')

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
    status = fields.Selection([("available", "Available"), ("rented", "Rented")],string="Status", help="Availability of the car", default="available", compute="_getStatusUpdated")


    @api.depends("borrower_id")
    def _getStatusUpdated(self):
        print(self)
        for record in self:
            record.status = "available"
            print(record.borrower_id)
            if record.borrower_id:
                record.status = "rented"


    @api.onchange("model")
    @api.onchange("color")
    @api.onchange("manufacturer")
    @api.onchange("license")
    def _capitalize_letters(self):
        for record in self:
            if record.model:
                    record.model = record.model.capitalize()
            if record.color:
                    record.color = record.color.capitalize()
            if record.manufacturer:
                    record.manufacturer = record.manufacturer.capitalize()
            if record.license:
                    record.license = record.license.upper()

