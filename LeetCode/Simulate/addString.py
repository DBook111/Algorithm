class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10 
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return '1' + res if carry else res
    
    
    def addStrings_zzl(self, num1: str, num2: str) -> str:
        # 456 77
        l1, l2 = len(num1), len(num2)
        is_carry = 0
        stack = []
        if l1 > l2:            
            i, j = l1 - 1, l2 - 1
            while l2 - j != l2 + 1:                                                  
                # 取出 num2 的小位
                n2 = int(num2[j])
                # 取出 num1 的小位
                n1 = int(num1[i])
                current_num = (n1 + n2 + 1) if is_carry == 1 else (n1 + n2)                
                if current_num > 9:
                    is_carry = 1
                    stack.append(str(current_num % 10)) 
                else:
                    is_carry = 0
                    stack.append(str(current_num)) 
                i -= 1
                j -= 1    
                    
            for i in range(l1 - l2 - 1, -1, -1):                
                current_num = (int(num1[i]) + 1) if is_carry == 1 else int(num1[i])
                if int(num1[i]) + is_carry > 9:
                    is_carry = 1
                    stack.append(str(current_num % 10))
                else:
                    is_carry = 0
                    stack.append(str(current_num))
            if is_carry == 1:
                stack.append("1")
            
        else:
            i, j = l1 - 1, l2 - 1
            while l1 - i != l1 + 1:                                                  
                # 取出 num2 的小位
                n2 = int(num2[j])
                # 取出 num1 的小位
                n1 = int(num1[i])
                current_num = (n1 + n2 + 1) if is_carry == 1 else (n1 + n2)                
                if current_num > 9:
                    is_carry = 1
                    stack.append(str(current_num % 10)) 
                else:
                    is_carry = 0
                    stack.append(str(current_num)) 
                i -= 1
                j -= 1    
                    
            for i in range(l2 - l1 - 1, -1, -1):                
                current_num = (int(num2[i]) + 1) if is_carry == 1 else int(num2[i])
                if int(num2[i]) + is_carry > 9:
                    is_carry = 1
                    stack.append(str(current_num % 10))
                else:
                    is_carry = 0
                    stack.append(str(current_num))
            if is_carry == 1:
                stack.append("1")
        
        res = ''
        while stack:
            res += stack.pop()
        return res
                    
solu = Solution()
print(solu.addStrings("1", "9"))