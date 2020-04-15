public class Solution {
    public int MaxArea(int[] height) {
        int maxArea=0;
        int left=0;
        int right=height.Length-1;
        while(left<right){
            maxArea=Math.Max(maxArea,Math.Min(height[right],height[left])*(right-left));
            if(height[right]>height[left])
                left++;
            else
                right--;
        }
        return maxArea;
    }
}
