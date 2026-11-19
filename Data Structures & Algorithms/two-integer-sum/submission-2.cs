public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        
        Dictionary<int, int> seen = new();
    
        for (int i = 0; i < nums.Length; i++) {
            int num = nums[i];
            int compliment = target - num;

            if (seen.ContainsKey(compliment)) {
                return [seen[compliment], i];
            }
            seen[num] = i;

        }
        return [];
    }
}
