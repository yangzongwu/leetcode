public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        Array.Sort(g);
        Array.Sort(s);
        int rep=0;
        int gstep=0;
        int sstep=0;
        while(gstep<g.Length && sstep<s.Length){
            if(s[sstep]>=g[gstep]){
                rep++;
                sstep++;
                gstep++;
            }
            else{
                sstep++;
            }
        }
        return rep;
    }
}
