# Copyright (c) 2024, vincent ndegwa and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):

	def validate(self):
		add_on_items=[]
		if self.add_ons:
			for add_on in self.add_ons:
				if add_on.item in add_on_items:
					frappe.throw(f"Add-on {add_on.item} is already added. Please remove the duplicate entry.")
				add_on_items.append(add_on.item)

	def before_save(self):
		total_add_ons = 0
		if self.add_ons:
			for add_on in self.add_ons:
				total_add_ons += float(add_on.amount)
		self.total_amount = float(self.flight_price) + total_add_ons

	
	def before_submit(self):
		if self.status != 'Boarded':
			frappe.throw(f"Ticket status must be 'Boarded' before submitting")

	def before_insert(self):
		random_int = random.randint(0, 99)
		random_char = chr(random.randint(ord('A'), ord('B')))
		self.seat = f"{random_int}{random_char}"
