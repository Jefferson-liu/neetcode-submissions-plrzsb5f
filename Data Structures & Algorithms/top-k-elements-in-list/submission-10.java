class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> topK = new ArrayList<>();
        for (int i = 0; i <= nums.length; i ++){
            topK.add(new ArrayList<Integer>());
        }
        Map<Integer, Integer> intCount = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            intCount.put(nums[i], intCount.getOrDefault(nums[i], 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : intCount.entrySet()){
            int num = entry.getKey();
            int freq = entry.getValue();
            topK.get(freq).add(num);
        }
        List<Integer> ans = new ArrayList<>();
        for (List<Integer> lst: topK){
            ans.addAll(lst);
        }
        Collections.reverse(ans);
        return ans.subList(0, Math.min(k, ans.size())).stream().mapToInt(Integer::intValue).toArray();

    }
}
