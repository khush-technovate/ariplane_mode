# Copyright (c) 2024, ne and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class AirplaneTicket(Document):
    def before_insert(self):
        random_integer = random.randint(1, 100)
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{random_integer}{random_letter}"

    def before_save(self):
        amount = 0
        for add_on in self.add_ons:
            amount += add_on.amount
        amount += self.flight_price
        self.total_amount = amount

    def validate(self):
        unique_add_ons = {}
        for add_on in list(self.add_ons):
            if add_on.item in unique_add_ons:
                self.remove(add_on)
            else:
                unique_add_ons[add_on.item] = add_on

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit the ticket unless the status is 'Boarded'.")
