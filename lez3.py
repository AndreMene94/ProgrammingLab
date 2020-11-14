#13-11-2020

#Read Csv File
myFile = open("shampoo_sales.csv", "r")
print(myFile.read())
myFile.close

#Slice Strings
myString = "superman"
print (myString[0:3]) #carat
print (myString[3:7])
print (myString[0:-1])

#Slice Csv File [0:50]
myFile = open("shampoo_sales.csv", "r")
myFileCont = myFile.read()
if (len(myFileCont)>50):
  print(myFileCont[0:50])
else:
  print(myFileCont)
myFile.close()

#Read Csv File - line by line!
myFile = open("shampoo_sales.csv", "r")
for line in myFile:
  print(line)
myFile.close()

#Write to files
myFile = open("saluti.txt","w")
myFile.write("Ciao")

#String Split
myString = "Ciao, come va?"
elementList = myString.split(",") #['ciao', ' come va?']
print(elementList)

#String to number conversion
myString = "5.5"
myNumber = float(myString)

#Add elements to list
myList = [1,2,3,4]
myList.append(5)
print (myList)