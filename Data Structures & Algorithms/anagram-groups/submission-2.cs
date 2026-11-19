public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> seen = new();
        List<string> res = new();

        foreach (string word in strs) {
            int[] code = new int[26];
            foreach (char c in word) {
                int index = c - 'a';
                code[index] += 1;
            }
            string key = string.Join(",", code);
            if (seen.ContainsKey(key)){
                seen[key].Add(word);
            }
            else {
                seen[key] = new List<string>();
                seen[key].Add(word); 
            }
        }

        return seen.Values.ToList();

    }
}
