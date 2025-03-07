
def load(filename):
  book=[]
  f=open(filename)
  while True:
    l=f.readline()
    if not l:
      break
    l=l[:-1]
    ll=l.split(";")
    book.append(ll)  
  return book

def save(pb,filename):
  f=open(filename,"w")
  for n in pb:
    f.write(n[0])
    f.write(";")
    f.write(n[1])
    f.write("\n")
  f.close()

def insert_number(pb):
  name=input("Enter Name:")
  number=input("Enter Number:")
  pb.append([name,number])

def search(pb):
  name=input("Enter Name:")
  person_found=False 
  for n in pb:
    if(name in n[0]):
      print("Name:",n[0]," Number:",n[1])
      person_found=True
  if not person_found:
    print("No Person Found")
  input("Press Enter")

def print_book(pb):
  print("***PhoneBook*****")
  for n in pb:
    print("Name:",n[0]," Number:",n[1])
  input("Press Enter")

