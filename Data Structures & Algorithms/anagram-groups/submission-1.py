class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = []
        res = []
        # Count chars
        for w in strs:
            wordmap = {}
            for c in w:
                wordmap[c] = wordmap.get(c, 0) + 1

            for i, group in enumerate(res):
                firstwordmap = {}
                for c in group[0]:
                    firstwordmap[c] = firstwordmap.get(c, 0) + 1 
                if firstwordmap == wordmap:
                    res[i].append(w)
                    break
            else:
                group = [w]
                res.append(group)
                
        return res


        
        
        

            