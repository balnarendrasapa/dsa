from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        length = 0
        temp_string = []
        for word in words:
            if length + len(word) + 1 <= maxWidth:
                length += len(word) + 1
                temp_string += [word]
            elif length + len(word) <= maxWidth:
                length += len(word)
                temp_string += [word]
            else:
                result += [temp_string]
                temp_string = [word]
                length = len(word) + 1

        if len(temp_string) != 0:
            result += [temp_string]

        justified = []
        for i in range(len(result)):
            line = result[i]
            if i == len(result) - 1:
                line_str = " ".join(line)
                line_str += " " * (maxWidth - len(line_str))
            else:
                total_chars = sum(len(word) for word in line)
                spaces_needed = maxWidth - total_chars
                if len(line) == 1:
                    line_str = line[0] + " " * spaces_needed
                else:
                    space_slots = len(line) - 1
                    even_space = spaces_needed // space_slots
                    extra_space = spaces_needed % space_slots

                    line_str = ""
                    for j in range(len(line) - 1):
                        line_str += line[j]
                        line_str += " " * (even_space + (1 if j < extra_space else 0))
                    line_str += line[-1]
            justified.append(line_str)

        return justified
