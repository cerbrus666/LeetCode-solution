This method is to solve this problem is called Horizontal Scanning
The steps are:
1. Firstly store the first string in list as prefix
2. Loop through the words lists, starting from the second word
3. Compare the word with the prefix, if not the same, then trim down the alphabet by 1 for each loop
4. Terminate the loop once the word is equal to prefix
5. The latest prefix will take the trimmed down prefix
6. Return the prefix for next word in the word lists
7. Repeat Step 3. until 6. until the loops for word lists are finished, return the trimmed down prefix
8. If the case where there is no common prefix between two words, which makes prefix compare with words continue looping and trim until prefix is empty, then just return empty string