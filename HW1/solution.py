# Online Merch

shirt_price = 28
hat_price = 18
number_of_shirts = 3
number_of_hats = 2
shipping_per_item = 3
tax_rate = 0.07

shirt_total = shirt_price * number_of_shirts
hat_total = hat_price * number_of_hats

merchandise_subtotal = shirt_total + hat_total

total_items = number_of_shirts + number_of_hats
shipping_cost = total_items * shipping_per_item

sales_tax = merchandise_subtotal * tax_rate

final_total = merchandise_subtotal + shipping_cost + sales_tax

print("Merchandise subtotal: $" + str(merchandise_subtotal))
print("Shipping: $" + str(shipping_cost) + ", Final total: $" + str(final_total))
