from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # If there are no courses, return True (nothing to complete)
        if numCourses == 0:
            return True
        
        # Step 1: Initialize the indegree array to keep track of the number of prerequisites for each course
        indegree = [0] * numCourses
        
        # Step 2: Create an adjacency list (graph) to map prerequisites
        mymap = collections.defaultdict(list)
        
        # Step 3: Count of courses that can be completed without prerequisites
        count = 0
        
        # Step 4: Initialize a queue to perform BFS
        q = Queue()
        
        # Step 5: Fill the indegree array and adjacency list (graph)
        for preq in prerequisites:
            a = preq[0]  # course a
            b = preq[1]  # course b (prerequisite for course a)
            indegree[a] += 1  # increment indegree for course a
            mymap[b].append(a)  # add course a to the list of courses dependent on b
        
        # Step 6: Add all courses with no prerequisites (indegree 0) to the queue
        for i in range(numCourses):
            if indegree[i] == 0:
                q.put(i)
                count += 1
        
        # If no course can be started (all courses have prerequisites), return False
        if count == 0:  # there is a cycle
            return False
        
        # Step 7: Process the courses in the queue
        while not q.empty():
            curr = q.get()  # Get a course with no prerequisites
            if curr in mymap:  # Check if this course is a prerequisite for others
                edges = mymap[curr]  # Get all courses that depend on the current course
                for edge in edges:
                    indegree[edge] -= 1  # Decrement the indegree of dependent courses
                    if indegree[edge] == 0:  # If a course has no more prerequisites
                        q.put(edge)
                        count += 1  # Increment the count of courses that can be completed
        
        # If all courses can be completed, count should equal numCourses
        return count == numCourses
