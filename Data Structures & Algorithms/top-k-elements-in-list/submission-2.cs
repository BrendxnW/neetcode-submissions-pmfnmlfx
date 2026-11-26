public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {

        Dictionary<int, int> seen = new();
        int[] res = new int[k];

        foreach (int num in nums) {
            seen[num] = seen.GetValueOrDefault(num, 0) + 1;
        }
        
        while (k > 0) {

            int highValue = seen.MaxBy(value => value.Value).Key;
            res[k - 1] = highValue;
            seen.Remove(highValue);
            k--;
        }
        return res;
    }
}
