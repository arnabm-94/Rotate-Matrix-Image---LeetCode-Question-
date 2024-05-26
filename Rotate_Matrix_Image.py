'''
#Problem Statement:

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Example:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

'''
#HINT:

To rotate an 𝑛 × 𝑛 2D matrix by 90 degrees clockwise in-place, you can follow these steps:

Transpose the matrix: Convert rows into columns.
Reverse each row: This will achieve the 90 degrees clockwise rotation.
Step-by-step Explanation
Transpose the matrix: For a matrix element at position (i, j), transpose swaps it to position (j, i).
Reverse each row: After transposing, reversing the rows will complete the 90-degree rotation.

'''
#Solution : 1

def rotate(matrix):
    n = len(matrix)
    
    # Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate(matrix)

print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

#===========================================================

#leetcode solution 


def rotate(matrix):

#Get the number of rows/columns in the square matrix and store it in the variable n.
    n = len(matrix)
 
    # Transpose the matrix
#Start a loop that iterates over the rows.
    for i in range(n):  # Iterate over the rows

#Start a nested loop that iterates over the columns starting from the current row i. 
#This ensures we only swap elements in the upper triangle of the matrix, avoiding double swaps.
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'

#Swap the elements at positions (i, j) and (j, i).
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
    # Reverse each row
#Start a loop that iterates over each row in the matrix.
    for row in matrix:  # Iterate over each row in the matrix

#Reverse the elements in the current row.
        row.reverse()  # Reverse the elements in the current row

'''
The time complexity of this code is O(n^2), 
as both the transpose and reverse steps involve nested loops 
that iterate over all the elements in the matrix. 
The space complexity is O(1), as the rotation is performed in-place 
without allocating any additional data structures.
'''
