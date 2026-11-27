public class Solution {
    public void SortColors(int[] nums) {
    
        for (int l = 0; l < nums.Length; l++) {
            int r = l + 1;

            while (r < nums.Length) {
                if (nums[l] > nums[r]){
                    int temp = nums[l];
                    nums[l] = nums[r];
                    nums[r] = temp;
                }
                r++;
            }
        }

    }
}