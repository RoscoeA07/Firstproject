#This program is a simulation of a system where the user needs to
#enter their username and password compared to default username and password

#Default username and password
defaultusername = "admin"
defaultpassword = "admin@2026"

#Ask user to enter their login details
username = input("Enter your username: ")
password = input("Enter your password: ")

#Check the login details
if username == defaultusername and password == defaultpassword:
  print("you have successfully logged in")

elif username != defaultusername and password != defaultpassword:
  print("Both username and password are wrong")

elif username != defaultusername:
  print("The username is wrong")

else:
  print("The password is wrong")
