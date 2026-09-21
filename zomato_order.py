def remove_last_item(order_list):
    remove_item = order_list.pop()
    return remove_item

order_list = ["pizza", "burger", "pasta", "sushi"]
removed = remove_last_item(order_list)

print("removed item:", removed)
print("updated order list:", order_list)