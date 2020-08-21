
class Solution:

    def generate_parentheses(self,n):

        self.ans = []

        self.gp(n,n,'')

        return self.ans

    def gp(self,no,nc,s):

        if no > nc: #base case
            return
        if no == 0 and nc == 0: #base case e garantia de bem formado
            self.ans.append(s)
        if no == 0: # se já esgotei os opening, só resta fechar
            self.gp(no,nc-1,s+')')
        else: # caso normal, onde as opções possíveis são abrir e fechar
            self.gp(no-1,nc,s+'(')
            self.gp(no,nc-1,s+')')


if __name__ == "__main__":

    solution = Solution()

    p = solution.generate_parentheses(3)
    print (p)