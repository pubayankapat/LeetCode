class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        if (strs == null || strs.length == 0)
            return "";
        for (String str: strs){
            while(!str.startsWith(prefix)){
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }
}