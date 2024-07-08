class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p_to_s = {}
        s_to_p = {}
        
        for char, word in zip(pattern, words):
            # a가 b 문자에 있다가 현재 값이랑 같은지비교
            if char in p_to_s:
                if p_to_s[char] != word:
                    return False
            else:
                p_to_s[char] = word
            
            if word in s_to_p:
                if s_to_p[word] != char:
                    return False
            else:
                s_to_p[word] = char
        
        return True
