#list of Districts
Districts = ["Mbale", "Masaka", "Mubende", "Mityana", "Mukono", "Mbarara", "Kampala", "Jinja",
"Busia", "Tororo"]
print("List of Districts:", Districts)
#Appending/adding Districts
Districts.append("Iganga")
Districts.append("Wakiso")
Districts.append("Hoima")
print("List of Districts after appending:", Districts)
#Size of list of Districts
print("Size of list:", len(Districts))
#For loop
for district in Districts:
 print(district)
#Removing Districts
Districts.remove(Districts[0])
#While loop
condition = 0
while condition < 1:
 print(Districts)
 condition += 1