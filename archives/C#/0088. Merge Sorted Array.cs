public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int length_num1=m+n-1;
        while(m>0 && n>0){
            if (nums1[m-1]>=nums2[n-1]){
                nums1[length_num1]=nums1[m-1];
                length_num1-=1;
                m-=1;
            }
            else{
                nums1[length_num1]=nums2[n-1];
                length_num1-=1;
                n-=1;
            }
        }
        if(m==0){
            for(int i=0;i<n;i++){
                nums1[i]=nums2[i];
            }
        }
    }
}
