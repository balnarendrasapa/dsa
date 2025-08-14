from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]

        que = deque([rooms[0]])
        visited[0] = True

        while que:
            temp_rooms = que.popleft()

            for room in temp_rooms:
                if not visited[room]:
                    visited[room] = True
                    que.append(rooms[room])

        for i in visited:
            if not i:
                return False

        return True
