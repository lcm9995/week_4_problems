class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_num = 0
        curr_string = ""
        for char in s:
            if char.isdigit():
                curr_num = curr_num *10 + int(char)
            elif char == '[':
                stack.append((curr_num, curr_string))
                curr_num = 0
                curr_string = ""
            elif char == "]":
                temp = stack.pop()
                curr_string = temp[1]+ temp[0]*curr_string 
            else:
                curr_string += char
        return curr_string