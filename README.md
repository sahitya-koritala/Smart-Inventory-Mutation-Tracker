# Smart-Inventory-Mutation-Tracker
Day-9 challenge of Python: This project demonstrates the use of Python data structures like lists and dictionaries to manage an inventory system. It focuses on understanding the difference between shallow copy and deep copy through practical implementation.

###  Objective

- To store and manage inventory data
- To use functions for performing operations
- To apply shallow and deep copy
- To observe how changes affect original data
- To compare and analyze results

### Data Used

Each item in the inventory contains:

 - Item name
 - Price
 - Stock
 - Supplier rating (nested field)

###  Working / Logic

- First, the inventory is created using a function. Then shallow copy and deep copy of the data are made.
- After that, a 10% discount is applied to all items. The stock of only one item is modified using roll number logic (roll_number % length).
- Then, the original data and copied data are compared using loops and conditions. The differences are displayed along with a summary of changed and unchanged items.
- Finally, output is used to check whether the data is shared or separate in shallow and deep copy.

###  Output

The program displays:

- Original inventory
- Shallow copy result
- Deep copy result
- Differences between data
- Summary tuple (changed, unchanged)
- Evidence of copy behavior

### Key Concept

- Shallow Copy:
Only the outer structure is copied. Inner data is shared, so changes affect the original.

- Deep Copy:
A complete copy is created. Changes do not affect the original data.

### Learning Outcomes
- Understanding of lists and nested dictionaries
- Use of functions, loops, and conditions
- Clear idea of shallow copy vs deep copy
- Ability to compare and analyze data

### How to Run
- Run the Python program
- Enter roll number as input
- Check the output and observe differences

### Conclusion

This program helps in understanding how shallow copy and deep copy work with nested data. It clearly shows how changes behave differently in both cases.
