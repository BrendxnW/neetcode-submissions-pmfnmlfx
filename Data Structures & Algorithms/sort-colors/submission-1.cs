public class Solution {
    public void SortColors(int[] nums) {
        
        int l = 0;
        int r = nums.Length - 1;
        int i = 0;

        while(i <= r) {
            int temp = 0;
            
            if (nums[i] == 0) {
                temp = nums[i];
                nums[i] = nums[l];
                nums[l] = temp;
                l++;
            }
            else if (nums[i] == 2) {
                temp = nums[i];
                nums[i] = nums[r];
                nums[r] = temp;
                r--;
                i--;
            }
            i++;
        }

    }
}