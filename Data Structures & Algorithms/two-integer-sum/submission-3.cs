public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        Dictionary<int, int> seen = new();

        for (int i = 0; i < nums.Length; i++){
            int compliment = target - nums[i];
            if (!seen.ContainsKey(compliment)) {
                seen[nums[i]] = i;
            }
            else {
                return [seen[compliment], i];
            }
        }
        return [];

    }
}
