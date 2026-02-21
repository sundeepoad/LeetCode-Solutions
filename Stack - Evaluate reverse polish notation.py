class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ## pop last two ints from stack
        ## perform operation on those if i == operator
        st = []

        operators = ['+', '-', '*','/']

        for i in tokens:
            if i in operators and st:
                item1 = st.pop()
                item2 = st.pop()

                if i == '+':
                    st.append(item2 + item1)
                if i == '-':
                    st.append(item2 - item1)
                if i == '*':
                    st.append(item2 * item1)
                if i == '/':
                    st.append(int(item2 / item1))
            
            else:
                st.append(int(i))
        return st[0]
