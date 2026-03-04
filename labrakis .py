

# Write a function:

# def manage_inventory(action: str, inventory: dict, product: str = None, quantity: int = None) -> dict:
#     """
#     Manage a store inventory with actions: add, remove, update, check.
#     """

# Requirements:
# 	1.	inventory is a dictionary where:
# 	•	Keys = product names (strings)
# 	•	Values = quantities (integers)
# Example:

# {"apple": 10, "banana": 5}


# 	2.	action can be one of:
# 	•	"add" → add a product with given quantity. If it already exists, increase quantity.
# 	•	"remove" → remove a product completely.
# 	•	"update" → change the quantity of a product to the given value.
# 	•	"check" → return the quantity of a product.
# 	3.	Use nested if-else to handle action logic.
# 	4.	Use loops where needed (for example, when printing all items after update or remove).
# 	5.	Handle exceptions:
# 	•	If quantity is not an integer when required → raise and catch ValueError.
# 	•	If the product doesn’t exist when trying to update/remove/check → raise and catch KeyError.

# ⸻

# Example Usage:

# inventory = {"apple": 10, "banana": 5}

# # Add
# inventory = manage_inventory("add", inventory, "orange", 7)
# # {"apple": 10, "banana": 5, "orange": 7}

# # Update
# inventory = manage_inventory("update", inventory, "banana", 12)
# # {"apple": 10, "banana": 12, "orange": 7}

# # Check
# manage_inventory("check", inventory, "apple")
# # Output: "apple has 10 items in stock"

# # Remove
# inventory = manage_inventory("remove", inventory, "orange")
# # {"apple": 10, "banana": 12}