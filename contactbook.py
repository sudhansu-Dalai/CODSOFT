names = []
phone_numbers =[]
email_ids= []
address = []

num=int(input( "Enter Number Of contacts You Want To Add : "))
count =num

for i in range (num):
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    emails=input("Enter Email id : ")
    addr = input("Enter The Address : ")

    names.append(name)
    phone_numbers.append(phone_number)
    email_ids.append(emails)
    address.append(addr)

#Print The Contact List
print("\nName\t\tPhone Number\t\tEmail Id \t\t Address\n")

for i in range(num):
    print("{}\t\t{}\t\t{}\t\t{}".format(names[i],phone_numbers[i],email_ids[i],address[i]))


#Choice For Contact Add Or Delet

choice = input("\nDo You Want To Add or Delet :  ")

if choice.lower() =="add":

    while True:

        count = num+1
        name_add = input("Enter Name : ")
        phone_No_add = input("Enter Phone Number : ")
        email_id_add = input("Enter Email Id : ")
        address_add = input("Enter Address : ")
        names.append(name_add)
        phone_numbers.append(phone_No_add)
        email_ids.append(email_id_add)
        address.append(address_add)
        choice1 = input("\nDo You want to add more (yes/no)")
        if choice1.lower() !="yes":
            break


elif choice.lower() == "delet":
    while True :

        count = num+1
        delet = input("\nEnter Name you Want To Delet Contact : ")
        indexs = names.index(delet)
        nam =names.pop(indexs)
        ph_num = phone_numbers.pop( indexs)
        email_id = email_ids.pop( indexs)
        adds = address.pop( indexs)
        choice2 = input("Do You Want To Delet More (yes/no): ")
        if choice2.lower() !="yes":
            break


print("\n")
print("Finall Contact List \n" )
print("\n")

#Contact After Adding Or Delete The Contact
print("\nName\t\tPhone Number\t\tEmail Id \t\t Address\n")

for i in range(count):
    print("{}\t\t{}\t\t{}\t\t{}".format(names[i],phone_numbers[i],email_ids[i],address[i]))


#This Is For Search The Contact By Name Or Phone Number :

search_item = input("\nSearch Contact :  ")

print("\n")
print("Search Reasult : ")
print("\n")

if search_item in  names :
    index = names.index(search_item)
    ph_num = phone_numbers[index]
    email_id=email_ids[index]
    adds = address[index]
    print("Name : {}\nPhone Number : {}\nEmail id : {}\nAddress : {} ".format(
        search_item,ph_num,email_id,adds))
elif search_item in phone_numbers:
    index = phone_numbers.index(search_item)
    name = names.index(index)
    # ph_num = phone_numbers[index]
    email_id = email_ids[index]
    adds = address[index]
    print("Name : {}\nPhone Number : {}\nEmail id : {}\nAddress : {} ".format(
        name,search_item, email_id, adds))

else:
    print("Contact Not Found ")


#                   -------------  Complete  -------------

