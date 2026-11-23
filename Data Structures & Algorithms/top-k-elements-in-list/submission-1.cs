public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {

        Dictionary<int, int> count = new();
        int[] res = new int[k];

        foreach (int num in nums) {
            count[num] = count.GetValueOrDefault(num, 0) + 1;
        }
        int index = 0;

        while (k > 0) {
            int highValue = count.MaxBy(pair => pair.Value).Key;
            res[index] = highValue;
            count.Remove(highValue);
            k--;
            index++;
        }



        return res;

    }
}
