class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0

        for i in range(0, len(row), 2):
            first = row[i]
            partner = first ^ 1

            if row[i + 1] == partner:
                continue

            partner_idx = pos[partner]
            row[i + 1], row[partner_idx] = row[partner_idx], row[i + 1]
            pos[row[i + 1]] = i + 1
            pos[row[partner_idx]] = partner_idx
            
            swaps += 1

        return swaps
