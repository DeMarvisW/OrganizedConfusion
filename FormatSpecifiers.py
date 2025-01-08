# FORMAT SPECIFIERS JAN 08 2025

# format specifiers  = {value:flags} format a value based on what flags are inserted
# Flags Oberved below: CAN PAIR AND MIX AND MATCH ALL FLAGS BY INCLUDING THEM TOGETHER AFTER COLON.

# .(number)f = Round to that many decimal places (f means floating point number = display that many decimal points).
# :(numbwer) = allocate that many spaces.
# :03 = allocate and zero pad that many spaces.
# :< = Left Justify.
# :> = Right Justify.
# :^ = Center Allign.
# :+ = Use a plus sign to indicate positive value.
# := = Place sign to left most position.
# :  = insert a space before positive numbers.
# :, = Comma separator.

price1 = 3.14
price2 = 400
price3 = 1400

print(F"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
