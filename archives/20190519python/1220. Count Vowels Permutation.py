class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        '''
        cur_a=[1]
        cur_e=[1]
        cur_i=[1]
        cur_o=[1]
        cur_u=[1]
        for k in range(1,n):
            num_a=cur_a[-1]
            num_e=cur_e[-1]
            num_i=cur_i[-1]
            num_o=cur_o[-1]
            num_u=cur_u[-1]
            a_next,e_next,i_next,o_next,u_next=0,0,0,0,0
            e_next+=num_a
            a_next+=num_e
            i_next+=num_e
            a_next+=num_i
            e_next+=num_i
            o_next+=num_i
            u_next+=num_i
            i_next+=num_o
            u_next+=num_o
            a_next+=num_u
            cur_a.append(a_next)
            cur_e.append(e_next)
            cur_i.append(i_next)
            cur_o.append(o_next)
            cur_u.append(u_next)
        return (cur_a[-1]+cur_e[-1]+cur_i[-1]+cur_o[-1]+cur_u[-1])%(10**9 + 7)
