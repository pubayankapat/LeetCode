class Solution {
    public int maxArea(int[] height) {
        int lp = 0;
        int rp = height.length - 1;
        int maxWater = 0;
        while(lp < rp){
            int h = Math.min(height[lp],height[rp]);
            int w = rp - lp;
            maxWater = Math.max(maxWater, h * w);
            if(height[lp] < height[rp]) 
                lp++;
            else
                rp--;
        }
        return maxWater;
    }
}