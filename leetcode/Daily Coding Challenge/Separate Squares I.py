class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        check = lambda my,total=sum(l*l for _,_,l in a): \
            sum(l*min(my-y,l) for _,y,l in a if y<my)>=total/2

        lo,hi,eps = 0,max(y+l for _,y,l in a),1e-6
        while hi-lo>eps:
            m = (hi+lo)/2
            if check(m): hi = m
            else: lo = m

        return hi
