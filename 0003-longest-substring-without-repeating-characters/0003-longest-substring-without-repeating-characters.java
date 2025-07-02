class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        Set<Character> chset = new HashSet<>();
        int left = 0;
        for (int right = 0; right < n; right++){
            if(!chset.contains(s.charAt(right))){
                chset.add(s.charAt(right));
                maxLength = Math.max(maxLength ,(right - left) + 1);
            }else{
                while(chset.contains(s.charAt(right))){
                    chset.remove(s.charAt(left));
                    left++;
                }
                chset.add(s.charAt(right));
            }
        }
        return maxLength;
    }
}