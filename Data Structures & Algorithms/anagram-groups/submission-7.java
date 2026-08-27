class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> anagrams = new HashMap<>();
        for (String s: strs){
            int[] alphaMap = new int[26];
            
            for (int i = 0; i < s.length(); i++){
                alphaMap[s.charAt(i) - 'a'] += 1; 
            }
            List<Integer> counts = Arrays.stream(alphaMap).boxed().collect(Collectors.toList());
            anagrams.computeIfAbsent(counts, k -> new ArrayList<>()).add(s);
        }
        List<List<String>> ans = new ArrayList<>();
        for (List<String> lst: anagrams.values()){
            ans.add(lst);
        }
        return ans;
    }
}
