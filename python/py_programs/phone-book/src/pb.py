def insert_number(book):
  name=input("Enter Name:")
  number=input("Enter Number:")
  book.append([name,number])

def print_book(book):
  print("***PhoneBook*****")
  for n in book:
    print("Name:",n[0]," Number:",n[1])


def search(book):
  name=input("Enter Name:")
  for n in book:
    if(name in n[0]):
      print("Name:",n[0]," Number:",n[1])

def load(filename):
  book=[]
  f=open(filename)
  while True:
    l=f.readline()
    if not l:
      break
    ll=l.split(";")
    book.append([ll[0],ll[1][:-1]])  
  return book

def save (book,filename):
  f=open(filename,"w")
  for n in book:
    f.write(n[0])
    f.write(";")
    f.write(n[1])
    f.write("\n")
  f.close()