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
        #continue
        break
    print("Buy " + item)

found_at = None
item_to_find = "spam"
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found.".format(item_to_find))

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found.".format(item_to_find))


