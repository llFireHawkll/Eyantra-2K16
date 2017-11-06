# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Cross_A_Crater (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task2
*  Filename: imgLib.py
*  Version: 1.5.0  
*  Date: November 21, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
#Complete the both function mentioned below, and return the desired outputs
#Additionally you may add your own methods here to help both methods mentioned below
###################Do not add any external libraries#######################

"""
* Team Id :         3035
* Author List :     SPARSH DUTTA, PRIYANSH JAIN, ABHINAV JAIN, ABHIMANYU SINGHAL
* Filename:         imgLib.py
* Theme:            CC-eYRC Specific
* Functions:        detectCellVal(img_gray,grid_map), isValid(row,col), BFS(grid_map,src,dest), solveGrid(grid_map)
* Global Variables: rowNum, colNum
"""

import cv2
import numpy as np

# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map

"""
* Function Name: detectCellVal
* Input:         img_gray -> The image of the grid which we want to store in gridmap and solve for shortest path
                 grid_map -> An Array of 14x14, basically a matrix which is used to store all the 0 and 1 of the image we have provided using image processing 
* Output:        grid_map -> An Array 0f 14x14 in which now all the 0 and 1 are stored is returned
* Logic:         Using image processing as our tool we are taking an empty grid map and then applying concepts of image processing to store the values of the image
                 provided in the grid map, so what we are actually doing is that we are taking,
                 we are considering small section of images using contour concept and then comparing that image with the given digits images,
                 if the shape matches then we enter the value of the digit in the grid map with which the our small section of image matches,
                 we are breaking our image in 14x14 parts and comparing each part with digits given, then writing the digit matched in the grid map
* Example Call:  detectCellVal(img_gray,grid_map)
"""
def detectCellVal(img_gray,grid_map):
	# your code here
        # Here we have just comparing section of our images with the given digits images and if the condition of 1 or 0 is true then we
        # store that digit in our grid map and then returning the grid map.
        for i in range(0, 14):
                for j in range(0, 14):
                    img1 = img_gray[(i*50):((i*50)+50), (j*50):((j*50)+50)]
                    ret1,thresh1 = cv2.threshold(img1,127,255,0)
                    contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                    # This if condtion is used to check that whether our small section of image has any digit or not
                    # if no digit is found then we place 0 in the grid map at that position
                    if(len(contours1) == 1):
                        grid_map[i][j] == 0

                    # else we start comparing the digit found with 0 or 1     
                    else :
                        cnt1 = contours1[1]

                        for k in range(0,2):
                            img2 = cv2.imread('digits/'+str(k)+'.jpg')
                            gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                            ret2,thresh2 = cv2.threshold(gray2,127,255,0)
                            contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                            cnt2 = contours2[1]

                            # Consider ret2 as the value if the shape matches then ret2 value is equal to 0.0 else some postive floating value
                            ret2 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
                            if(ret2 == 0.0):
                                grid_map[i][j] = k
                                break
        # At last when all the chunks of image have been processed we return the grid map for futher processing
	return grid_map



# So from here onwards our main logic for the shortest path algorithm code starts.
"""
* Function Name: isValid
* Input:         row,col -> Both take an integer as input  
* Output:        0 -> when given row and col are not valid index in the grid map array of 14x14
                 1 -> when given row and col are valid index in the grid map array of 14x14
* Logic:         simple comparision logic is used to i.e ((row >= 0) and (row < 14) and (col >= 0) and (col < 14))
* Example Call:  isValid(1,2)
"""
def isValid(row,col):
    return ((row >= 0) and (row < 14) and (col >= 0) and (col < 14))



# Here we have declared two lists that are rowNum and colNum which we are going to use to find the neighbours of the current node, used in BFS,
# The rowNum and colNum are GLOBAL VARIABLE
# rowNum, colNum: These are simply the list consisting of indexes of neighbours (combined togther) use in during BFS procedure, 
rowNum = [0, -1, -1, -1, 0, 1, 1, 1]
colNum = [-1, -1, 0, 1, 1, 1, 0, -1]




# This is the heart of the program, our BFS function which is used to find the shortest path and its length,
"""
* Function Name: BFS
* Input:         grid_map -> An Array of 14x14 in which we have stored all the 0 and 1 of the given problem image using image processing
                 src      -> The coordinates of the starting point, i.e. The point from where are BFS begins
                 dest     -> The coordinates of the finishing point, i.e. The point where are BFS ends
* Output:        dist -> The distance from the source to destination (shortest distance)
                 path -> The shortest path taken to reach destination from source
                 0    -> Returns 0 when no path is found
* Logic:         Here we use the concept of Breadth First Search in order to find out the shortest path and shortest distance taken to reach destination
                 from source (Here only one source and destination are taken at a time)
* Example Call:  BFS(grid_map, [13,1], [0,1])
"""
def BFS(grid_map,src,dest):

    # This if condition is used to check whether the given source and destination are valid points or not i.e. the source and destination are 1 or not.        
    if(not(grid_map[src[0]][src[1]]) or not(grid_map[dest[0]][dest[1]])):
        return 0

    # Here we are creating two matrices of the same size as of grid map, that is a visited matrix in which all entry at first are false and
    # second is the parent matrix in which we are going to store the parent of the current node which will help us in backtracing and find the shortest path route,
    visited = [ [False for i in range(14)] for j in range(14) ]
    parent = [ [[-1, -1] for i in range(14)] for j in range(14) ]

    # As we are starting from source, so we have to mark it true in the visited matrix
    visited[src[0]][src[1]] = True


    # Here we have created path as an empty list, which will be used to store the shortest route,
    path = []

    # Here queue is a list in which we are providing the starting source coordinates and the route length
    queue = [[src, 0]]


    # This is a while loop which will run till the list queue is not empty when the list will be empty the condition in the while loop will be false and the
    # program will exit from the loop

    # The basic of loop is find the Shortest Path,
    while(len(queue)):

        # Here we are extracting and x, y and distance from the list queue,     
        x = queue[0][0][0]
        y = queue[0][0][1]
        dist = queue[0][1]

        # This if condition is used to check that whether we have reached our destination or not,
        if (x == dest[0] and y == dest[1]):
            # if the, above if condition is true, then we will proceed further to extract the shortest route,
            current = dest

            # Now in this while loop we are backtracing and this gives us the route,
            while(cmp(parent[current[0]][current[1]], [-1, -1])):
                x_cood = current[1] + 1 
                y_cood = current[0] + 1
                path.append((x_cood, y_cood))
                current = parent[current[0]][current[1]]
            # At last we are adding our source in the list and reversing the list as the list of route is in the reverse order, and at last returing the data.    
            x_cood = current[1] + 1 
            y_cood = current[0] + 1
            path.append((x_cood, y_cood))
            path.reverse()
            return dist, path

        # Here we popping out the first data in the list, we are making this list behave like a queue data structure, FIFO,
        queue.pop(0)

        # Here in the for loop we are visiting all the neighbours of the current node and checking if they are correct path or not,
        # using the if condition and marking them as visited if they satisfy all the condition and also marking their parent in the parent matrix,
        # and at last we are appending the correct neighbours in the queue list. "THIS IS THE BFS ALGORITHM" 
        for i in range(8):
            row = x + rowNum[i]
            col = y + colNum[i]
            
            if (isValid(row, col) and grid_map[row][col] and (not visited[row][col])):               
                visited[row][col] = True
                parent[row][col] = [x, y]
                queue.append([[row, col], dist + 1])       
    return 0
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length

"""
* Function Name: sovleGrid
* Input:         grid_map -> An Array of 14x14 in which we have stored all the 0 and 1 of the given problem image using image processing
* Output:        route_path   -> It is the actual shortest path, here we have considered all possible sources and destination
                 route_length -> It is the actual shortest length, here we have considered all possible sources and destination
* Logic:         Main logic here is that, we have considered all possible sources and destination and store them in the array and then traversing from each source
                 to each destination and then finding the shortest length from our solution list then returing the apt shortest path and shortest length
* Example Call:  solveGrid(grid_map)
"""
def solveGrid(grid_map):
	route_length=0
	route_path=[]
	solution=[]
        minNum = 999999
	#your code here

        # Here we are taking two empty list that are src and dest in which using the for loop we are putting all
        # the possible source and destination from the gridmap which we are getting as input,
        src = []
        dest = []
        for i in range(14):
                if(grid_map[13][i] == 1):
                        src.append([13, i])
        for i in range(14):
                if(grid_map[0][i] == 1):
                        dest.append([0, i])

        # Now we are taking empty list solution in which we are storing all the possible solution of the BFS from all possible
        # sources and destination,
        for i in range(len(src)):
                for j in range(len(dest)):
                        solution.append(BFS(grid_map, src[i], dest[j]))

        # Now in this loop we are selecting only the solution in which the route length is greater than 0, and here we are also
        # calculating the minimum of the distance from all the BFS i.e. the shortest length,
        for i in range(len(solution)):
                if(solution[i] > 0):
                    if(solution[i][0] > 0 and solution[i][0] < minNum):
                        minNum = solution[i][0]
                    route_length = minNum  

        # In this loop we are selecting the route path which is having the smallest route length,    
        for i in range(len(solution)):
                if(solution[i] > 0):
                    if(solution[i][0] == minNum):
                        route_path = solution[i][1]
                        break
        # And finally we are returing the required.        
        return route_path, route_length
############################################################################################
