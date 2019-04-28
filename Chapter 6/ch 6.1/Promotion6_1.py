from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

	def __init__(self, product, quantity, price):
		self.product = product
		self.quantity = quantity
		self.price = price

	def total(self):
		return self.price * self.quantity

class Order:
	
	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion
		
	def total(self):
		if not  hasattr(self, '_total'):
			self._total = sum(item.total() for item in self.cart)
		return self._total

	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)
		return self.total() - discount

	def __repr__(self):
		fmt = '<Order total: {:.2f} due: {:.2f}>'
		return fmt.format(self.total(), self.due())

class Promotion(ABC): # 策略：抽象基类

	@abstractmethod
	def discount(self, order):
		# 返回折扣金额
		pass

class FidelityPromo(Promotion):	# 第一个具体策略

	def discount(self, order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):

	def discount(self, order):
		discount = 0
		for item in order.cart:
			if item in order.cart:
				if item.quantity >= 20:
					discount += item.total() * .1
		return discount

class LargeOrderPromo(Promotion):

	def discount(self, order):
		distinct_items = {item.product for item in order.cart}
		if len(distinct_items) >= 10:
			return order.total() * .07
		return 0

if __name__ == '__main__':
	joe = Customer('John Doe', 0)
	ann = Customer('Ann Smith', 1100)
	cart = [
		LineItem('banana', 4, .5),
		LineItem('apple', 10, 1.5),
		LineItem('watermellon', 5, 5.0)
	]
	print(Order(joe, cart, FidelityPromo()))
	print(Order(ann, cart, FidelityPromo()))





