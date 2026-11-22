public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> seen = new();

        int res = 0;

        foreach (int num in nums) {
            seen[num] = seen.GetValueOrDefault(num, 0) + 1;
            if (seen[num] > nums.Length / 2) {
                res = num;
            }
        }

        return res;

    }
}