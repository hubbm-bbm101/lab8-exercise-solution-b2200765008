import sys
student = {}
with open(sys.argv[1],"r+",encoding="utf-8") as students:
    for i in students:
        if i[0] == "*":
            continue
        else:
            i = i.strip(" \n")
            name,content = i.split(":")
            student[name] = content

sql_string = ",".join("%s"%j for j in sys.argv[2:])
list1 =sql_string.split(",")
for l in list1:
  try:
    print("Name:{},".format(l),"University:{}".format(student[l]),end=" ")
  except:
    print("No record of '{}' was found!".format(l),end=" ")
