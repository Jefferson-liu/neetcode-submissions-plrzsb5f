class Solution {

    public String encode(List<String> strs) {
        List<Integer> lens = new ArrayList<>();
        if (strs.size() == 0){
            return "";
        }

        for (String s: strs){
            lens.add(s.length());
        }
        String lengths = "";
        for (int len: lens){
            lengths += len + " ";
        }
        String result = "";
        result += lens.size() + " ";
        result += lengths;
        result += String.join(" ", strs);
        return result;

    }

    public List<String> decode(String str) {
        if (str.length() == 0){
            return new ArrayList<String>();
        }
        String[] splits = str.split(" ");
        int numWords = Integer.parseInt(splits[0]);
        int[] lens = Arrays.stream(splits, 1, numWords + 1).mapToInt(Integer::parseInt).toArray();
        int strStart = 0;
        for (int i = 0; i < numWords + 1; i++){
            strStart += splits[i].length() + 1;
        }
        String strs = str.substring(strStart);
        List<String> ans = new ArrayList<>();
        int start = 0;
        for (int len: lens){
            ans.add(strs.substring(start, Math.min(start + len, strs.length())));
            
            start += len + 1;
        }
        return ans;
        

    }
}
