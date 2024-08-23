package q118666;

import java.util.HashMap;

class Solution {
    public String solution(String[] survey, int[] choices) {
        HashMap<Character, Integer> scores = new HashMap<>();
        scores.put('R', 0);
        scores.put('T', 0);

        scores.put('C', 0);
        scores.put('F', 0);

        scores.put('J', 0);
        scores.put('M', 0);

        scores.put('A', 0);
        scores.put('N', 0);

        for (int i = 0; i < survey.length; i++) {
            char disagree = survey[i].charAt(0);
            char agree = survey[i].charAt(1);

            if (choices[i] < 4) {
                scores.put(disagree, scores.get(disagree) + 4 - choices[i]);
            } else if (choices[i] > 4) {
                scores.put(agree, scores.get(agree) + choices[i] - 4);
            }
        }

        StringBuilder answer = new StringBuilder();
        answer.append(scores.get('R') >= scores.get('T') ? "R" : "T");
        answer.append(scores.get('C') >= scores.get('F') ? "C" : "F");
        answer.append(scores.get('J') >= scores.get('M') ? "J" : "M");
        answer.append(scores.get('A') >= scores.get('N') ? "A" : "N");

        return answer.toString();
    }
}