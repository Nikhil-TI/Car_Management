from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Car(models.Model):
        _name = "car.management"
        _description = "Car Management"
        _rec_name = "model"

        #Car name
        model = fields.Char(string="Car Model", required=True)

        #image of the car
        image = fields.Image(string="Image")

        # Original owner
        owner_id = fields.Many2one('car.owner', string="Owner", required=True)
        #owners email
        owner_id_email = fields.Char(string="Owner's Email", related="owner_id.email")

        #rental record
        rental_id = fields.Many2many("car.rental", "car_management_rental_rel", "car_id", "rental_id", string="Rentals", readonly=True)

        # Renter of the car
        borrower_id = fields.Many2one(string="borrower", related="rental_id.borrower_id", readonly=True)
        #Renters email
        borrower_id_email = fields.Char(string="Borrower's email",related='borrower_id.email')

        #color
        color = fields.Char(string="Color", required=True)

        #currency import id
        currency_id= fields.Many2one("res.currency", string="Currency", required=True)
        #cost of the car per day
        cost= fields.Monetary(string="Cost for rental per day", currency_field="currency_id")

        #made by
        manufacturer = fields.Char(string="Manufacturer", required=True)

        #license plate
        license = fields.Char(string="License Plate", required=True)

        #year of manufacturing
        YOM = fields.Integer(string="Year of Manufacturing", required=True)

        # #last day of service
        service = fields.Date(string="Lase Date of Service", required=True)
        
        # milage
        mileage = fields.Float(string="Mileage", required=True)

        #status
        status = fields.Selection([("available", "Available"), ("rented", "Rented")],string="Status", help="Availability of the car", default="available", compute="_getStatusUpdated")

        @api.constrains("mileage", "service", "YOM")
        def _field_constrains(self):
                for record in self:
                        current_date = datetime.now().date()
                        current_year = current_date.year
                
                        if record.YOM > current_year:
                                raise ValidationError("Year of manufacturing cannot be grater then the current year!")
                
                        if record.service < current_date:
                                raise ValidationError("The car has exceeded the last date of service. Thus it cannot be added. Please try adding a different car which has not reached it last date of service")
                        
                        if record.mileage < 1:
                                raise ValidationError("Mileage cannot be zero or negative")

        @api.depends("borrower_id")
        def _getStatusUpdated(self):
                for record in self:
                        record.status = "available"
                        print(record.borrower_id)
                        if record.borrower_id:
                                record.status = "rented"
                

        # Capitalizing the record in the model        
        @api.onchange("license", "model", "color", "manufacturer")
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


        def view_car_details(self):
                
                # Action to open the form view of the car
                return {
                'type': 'ir.actions.act_window',
                'name': 'Car Details',
                'view_mode': 'form',
                'res_model': 'car.management',
                'res_id': self.id,  # The ID of the record to open
                'target': 'current',  # Open in the current window
                }
