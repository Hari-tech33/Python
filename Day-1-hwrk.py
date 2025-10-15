ri_price, su_price, oil_price = 45, 40, 130
ri_qty, su_qty, oi_qty = 3, 2.5, 1.8

total_rice = ri_price * ri_qty
total_sugar = su_price * su_qty
total_oil = oil_price * oi_qty

print(total_rice, total_sugar, total_oil)

final_bill = total_rice + total_sugar + total_oil
print(final_bill)

final_int = int(final_bill)
print(final_int)
final_str = str(final_bill)
print(final_str)

import random
deliver = (random.randrange(5,10))

final_total = final_bill + deliver
print(final_total)



