class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> map=new HashMap<>();
        for(String c:strs){
            char[] ch=c.toCharArray();
            Arrays.sort(ch);
            String key=new String(ch);
            if(!map.containsKey(key)){
                map.put(key,new ArrayList<>());
            }
            map.get(key).add(c);
        }
        return new ArrayList<>(map.values());
    }
}
