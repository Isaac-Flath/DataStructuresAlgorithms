Task0:  The complexity is O(4) as there are 2 assignment statements and 2 print statements.  This is simplified to show just the order as O(1)

Task1: O(n).  This is a linear solution because we go through each input only once (in the destructured assignment statments).

Task2: O(n^2).  The worste case is caused by the two loops (aggregation loop, and finding max loop).  If the unique telephone numbers are equal to the count of telephone numbers this worste case will occur. 

Task3:  O(9n).  The worste case is that every line of code in the loop is run (6).  This would be true if every call was both from and to Banagalore.  In addition there are 2 that are run based on size of data from the destructured assignments at the top, and the final complexity coming from casting the list to a set to deduplicate.

task4:  O(4n).  The destructured assignment, the phone numbers, and the loop in the telemarketers are the only complexity and code run for this solution.