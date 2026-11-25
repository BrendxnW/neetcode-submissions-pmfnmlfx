public class Solution {
    public void Rotate(int[] nums, int k) {
 
        int n = nums.Length;
        k %= n;

        Reverse(nums, 0, n - 1);
        Reverse(nums, 0, k - 1);
        Reverse(nums, k, n - 1);
    }
        private void Reverse(int[] arr, int l, int r) {
            
            while (l < r){
                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;

                l++;
                r--;
            }

    }
}