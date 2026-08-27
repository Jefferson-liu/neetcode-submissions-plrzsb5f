class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numInd = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (numInd.containsKey(nums[i]) && nums[i] * 2 == target){
                return new int[]{numInd.get(nums[i]), i};
            }
            else{
                numInd.put(nums[i], i);
            }
            if (numInd.containsKey(target - nums[i]) && numInd.get(target - nums[i]) != i){
                return new int[]{numInd.get(target - nums[i]), numInd.get(nums[i])};
            }
        }
        return new int[]{0,0};
    }
}
