class Solution {
    public int[] productExceptSelf(int[] nums) {
        Map <Integer, Integer> prefix = new HashMap<>();
        Map <Integer, Integer> postfix = new HashMap<>();
        prefix.put(0, nums[0]);
        postfix.put(nums.length - 1, nums[nums.length - 1]);
        for (int i = 1; i < nums.length; i++){
            prefix.put(i, prefix.get(i-1) * nums[i]);
            postfix.put(nums.length - 1 - i, postfix.get(nums.length - i) * nums[nums.length - i - 1]);
        }
        int[] output = new int [nums.length];
        output[0] = postfix.get(1);
        output[nums.length - 1] = prefix.get(nums.length - 2);
        for (int i = 1; i < nums.length - 1; i++){
            output[i] = prefix.get(i - 1) * postfix.get(i + 1);
        }
        return output;

    }
}  
