class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set <Integer> numSet = new HashSet<>();
        for (int num: nums){
            numSet.add(num);
        }
        return (numSet.size() != nums.length);
        
    }
}