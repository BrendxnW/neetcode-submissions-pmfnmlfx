public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> match = new();


        foreach (string word in strs) {
            int[] code = new int[26];
            

            foreach (char c in word) {
                int index = c - 'a';
                code[index] += 1;
            }
            string key = String.Join(',', code);

            if (match.ContainsKey(key)){
                match[key].Add(word);
            }
            else {
                match[key] = new List<string>();
                match[key].Add(word);
            }
        }

        return match.Values.ToList();
    }
}
