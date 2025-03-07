import pb1 as pb

with open("book.txt", "w") as file:
    file.write("") # Create an empty file 

book=pb.load("book.txt")
while True:
  print("\n***************")
  print("1: Insert Number")
  print("2: Search number")
  print("3: Print All numbers")
  print("10:Exit")
  s=input("?")
  if s=="10":
    break
  elif s=="1":
    pb.insert_number(book)
  elif s=="2":
    pb.search(book)
  elif s=="3":
    pb.print_book(book)

pb.save(book,"book.txt")