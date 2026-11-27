public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int pointer = nums1.Length - 1;

        while (m > 0 && n > 0) {
            if (nums1[m - 1] > nums2[n - 1]) {
                nums1[pointer] = nums1[m - 1];
                m--;
            }
            else{
                nums1[pointer] = nums2[n - 1];
                n--;
            }
            pointer--;
        }

        while (n > 0) {
            nums1[n - 1] = nums2[n - 1];
            n--;
            pointer--;
        }
    }
}