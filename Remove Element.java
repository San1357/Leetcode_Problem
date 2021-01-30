class Solution {
    public int removeElement(int[] nums, int val) {
        int reWrittenIndex = 0;
        for (int index = 0; index < nums.length; index++) {
            if (nums[index] != val) {
                nums[reWrittenIndex++] = nums[index];
            }
        }

        return reWrittenIndex;
    }
}
