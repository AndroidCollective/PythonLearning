for i in range(1,13):
    for j in range(1,13):
        print("{0:2} times {1:2} is {2:2}".format(j,i,i*j))
    print("-" * 80)

shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)