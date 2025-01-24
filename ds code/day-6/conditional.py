# write a program to calculate gepco bill
#input units

units = int(input("Enter the units: "))
consumer_type = input("please enter consumer type(for domestic d, for commercial c)")
if consumer_type == 'd':
      if units <= 100:
        bill = units * 2
      elif units <= 200:
            bill = 100 * 2 + (units - 100) * 5
      else:
            bill = 100 * 2 + 100 * 5 + (units - 200) * 7
elif consumer_type == 'c':
      if units <= 100:
            bill = units * 5
      elif units <= 200:
            bill = 100 * 5 + (units - 100) * 7
      else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
      print("Invalid consumer type")
      bill = 0
print("Your bill is: ", bill)