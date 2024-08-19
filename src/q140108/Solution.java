package q140108;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int match = 0;
        int unmatch = 0;
        String target = "";
        String[] str = s.split("");

        for (String n : str) {
            if (match == 0) {
                target = n;
            }

            if (target.equals(n)) {
                match++;
            } else {
                unmatch++;
            }

            if (match == unmatch) {
                answer++;
                match = 0;
                unmatch = 0;
            }
        }

        if (match != 0) answer++;

        return answer;
    }
}