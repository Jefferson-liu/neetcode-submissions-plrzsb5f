class Solution {
    public boolean isAnagram(String s, String t) {
        Map <Character, Integer> c1 = new HashMap<>();
        Map <Character, Integer> c2 = new HashMap<>();
        for (char sChar: s.toCharArray()){
            c1.put(sChar, c1.getOrDefault(sChar, 0) + 1);
        }
        for (char tChar: t.toCharArray()){
            c2.put(tChar, c2.getOrDefault(tChar, 0) + 1);
        }
        return c1.equals(c2);
    }
}
