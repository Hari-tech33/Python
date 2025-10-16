heading = """
\nBook Store
Trivandrum\n  """

book_1 = "\nBook Title: {}\t - ₹{}\n".format("Python Basics", 450)
book_2 = "\n Book Title: {}\t - ₹{}\n".format("Data Science Intro", 600)

total_price = 450 + 600
total_amount = "\nTotal Amount:\t ₹{}\n".format(total_price)

msg = total_amount + ' \n"Thank you and Visit Again"'

bill = heading + book_1 + book_2 + msg
print(bill.upper())








 






