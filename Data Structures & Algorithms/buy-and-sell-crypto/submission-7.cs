public class Solution {
    public int MaxProfit(int[] prices){

        int maxProfit = 0;
        
        int l = 0;
        for (int r = 0; r < prices.Length; r++) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                maxProfit = Math.Max(maxProfit, profit);
            }
            else {
                l = r;
            }
        }
        return maxProfit;

    }
}
