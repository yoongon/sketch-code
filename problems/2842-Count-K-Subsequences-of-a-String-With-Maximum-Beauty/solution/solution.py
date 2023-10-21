class Solution:
    def helper(self, cnt):
        maxi = max(cnt.values())
        elements = []
        for k, v in cnt.items():
            if v == maxi:
                elements.append(k)
        return elements

    def sol(self, cnt, k):
        elements = self.helper(cnt)
        size = len(elements)
        if size >= k:
            return cnt[elements[0]] ** k * math.comb(size, k)
        ncnt = collections.Counter(cnt)
        for elem in elements:
            del ncnt[elem]
        return cnt[elements[0]] ** size * self.sol(ncnt, k - size)

    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)
        if len(cnt) < k:
            return 0
        return self.sol(cnt, k) % (10 ** 9 + 7)


'''
        s       : bcca
        dic     : {a:1, b:1, c:2}

                    sol({a:1, b:1, c:2}, k=2)
                        elems   : [c]
                        size    : 1
                        ddic    : {a:1, b:1}

                        2 ** 1 * sol({a:1, b:1}, k=1)

                                        elems   : [a, b]
                                        size    : 2
                                        res     : 1**2 * 2 Combi 1
                                         /





1. Problem
    - Given a string s and an integer k
    - k-subsequence is a subsequence of s having length k
    - unique
    - maximum among all k-subsequence
    - 

2. TCs
    tc1)
    s       : bcca
    k       : 2
    res     : 4


3. Brain Storming
    - find the most popular one?
    - get number of combination??


    s       : bcca
    k       : 2
    dic     : {b:1, c:2, a:1}


                {b:1, c:2, a:1}, k = 2
                    dic[c] * 
                /
        {b:1, a:1}, k = 1
        dic[b], dic[a] => 2 ???



    s       : abbcd
    k       : 4
            {b:2, a:1, c:1, d:1},   k = 4
                    dic[b] * 
                /
        {a:1, c:1, d:1}, k = 3
            dic[a] * dic[c] * dic[d]



        if the number of most popular one is less than k?
            => dic[the most popular one] * recursion???



            {b:1, c:2, a:1}, k = 2
            /

        s       : bcd
        k       : 2

            {b:1, c:1, d:1}
                if most popular is greater than  k
                    the number combination k ????


        s       : aabbcc
        k       : 2

            a) find the most popular one
                1) check the size

            b) if size > k:
                return dic[the popular] ** k  * size Combination k
               else:
                return dic[the popular] ** size * 
                        do the recursion??


                def helper(dic):
                    maximum size
                    return elements 

                def sol(dic, k):
                    elements = helper(dic)
                    size = len(elements)
                    if size > k:
                        return dic[elements[0]] ** k * size Combination k
                    return dic[elements[0]] ** size * sol(new_dic, size)
'''