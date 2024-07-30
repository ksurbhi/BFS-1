from queue import Queue

class Solution:
    '''
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Edge case: if the grid is empty, return 0
        if grid == None or len(grid) == 0:
            return 0
        
        q = Queue()
        freshOranges = 0
        total_min = 0
        # Directions array representing Up, Down, Left, Right moves
        Dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # Traverse the grid to count fresh oranges and add rotten ones to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.put([i, j])  # Add coordinates of rotten oranges to the queue
                elif grid[i][j] == 1:
                    freshOranges += 1  # Count fresh oranges
        
        # If there are no fresh oranges, no time is needed to rot them
        if freshOranges == 0:
            return 0
        
        # Start BFS traversal
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                for d in Dir:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]
                    # If the adjacent cell contains a fresh orange, rot it
                    if (nr >= 0 and nr < len(grid) and nc >= 0 
                    and nc < len(grid[0]) and grid[nr][nc] == 1):
                        q.put([nr, nc])
                        grid[nr][nc] = 2  # Mark orange as rotten
                        freshOranges -= 1  # Decrease count of fresh oranges
            total_min += 1  # Increase time after each level of BFS
        
        # If there are still fresh oranges left, return -1
        if freshOranges != 0:
            return -1
        
        return total_min - 1  # Subtract 1 because the last increment occurs after all oranges have rotted
