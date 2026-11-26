public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> numSet = new(nums);
        int maxCount = 0;

        foreach (int num in numSet) {
            if (!numSet.Contains(num - 1)) {
                int length = 1;

                while (numSet.Contains(num + length)) {
                    length++;
                }
            maxCount = Math.Max(maxCount, length);
            }
        }
        return maxCount;
    }
}
