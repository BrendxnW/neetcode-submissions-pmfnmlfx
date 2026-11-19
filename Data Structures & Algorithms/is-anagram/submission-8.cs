public class Solution {
    public bool IsAnagram(string s, string t) {

        Dictionary<char, int> seen = new();
        Dictionary<char, int> seen2 = new();
        

        if (s.Length != t.Length) {
            return false;
        }

        foreach (char c in s) {
            seen[c] = seen.GetValueOrDefault(c, 0) + 1;
        }

        foreach (char c in t) {
            seen2[c] = seen2.GetValueOrDefault(c, 0) + 1;
        }

        foreach (char c in seen.Keys) {
            if (!seen2.ContainsKey(c) || seen[c] != seen2[c]) {
                return false;
            }
        }
        return true;

    }
}
