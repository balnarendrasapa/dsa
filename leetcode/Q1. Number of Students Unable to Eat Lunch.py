class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sd = deque(sandwiches)

        while st:
            if st[0] == sd[0]:
                st.popleft()
                sd.popleft()

            else:
                if sd[0] not in st:
                    break
                st.append(st.popleft())

        return len(st)
