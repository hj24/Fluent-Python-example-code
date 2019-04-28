promos = []

def promotion(promo_func):
	promos.append(promo_func)
	return promo_func

@promotion
def fidelity(order):
	return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total() * .1
	return discount

@promotion
def large_order(order):
	distinct_items = {item.product for item in order.cart}
	if len(distinct_items) >= 10:
		return order.total() * .07
	return 0

def best_promo(order):
	return max(promo(order) for promo in promos)

b = 6

def f(a):
	c = bv(2)
	print(a)
	print(b)
	

def bv(c):
	return 1

f(3)