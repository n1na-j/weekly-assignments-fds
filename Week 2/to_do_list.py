# Tasks on the todo list
tasks = ["Buy new shirts", "Buy new sunglasses", "Walk 30 minutes", "Find a recipe for this evening", "Clean up desk", "Go to the gym", "Work on assignment FML"]
print("Tasks on the to-do list: ", tasks)

# New tasks "order pizza"
new_tasks = "Order pizza"
# Append "order pizza" to the todo list
tasks.append(new_tasks)
# Update todo list
print("New task on the to-do list: ", tasks)


# New item from user to the todo list
user_task = input("Add something on the to-do list: ")
tasks.append(user_task)
# Update to-do list
print("This is the updated to-do list: ", tasks)


# Count all tasks
print("There are", len(tasks), "tasks on the to-do list")


# Remove the first task of the to-do list 
tasks.pop(0)

# Check if first task has been removed
print("The first task has been removed. Check it out:", tasks)

# Remove "Buy new sunglasses"
tasks.remove("Buy new sunglasses")
# Check if "Buy new sunglasses" has been removed
print("We have bought new sunglasses. It has been removed from the to-do list:", tasks)


# Minimum tasks
min_tasks = 4
# Maximum tasks
max_tasks = 6

# Tell the user to do more when task list is shorter than min_tasks
if (len(tasks) < min_tasks):
    print("You have",len(tasks),"tasks on the to-do list. You have time to do more!")

# Tell the user to do less when task list is longer than max_tasks
if (len(tasks) >= max_tasks):
    print("You already did", len(tasks), "tasks. You've done enough for now!")
