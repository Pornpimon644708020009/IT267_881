from cusorder import customer,order

cus = customer.Customer("Jame","Nontraburi")
ord = order.Order("15-06-22","packed")

print (f'Order of {cus.cus_name} on {ord.date} is {ord.status}')