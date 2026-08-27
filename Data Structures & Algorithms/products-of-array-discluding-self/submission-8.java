class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        // Left products
        int left = 1;
        for (int i = 0; i < nums.length; i++) {
            result[i] = left;
            left *= nums[i];
        }

        // Right products
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] *= right;
            right *= nums[i];
        }

        return result;
    }
}
