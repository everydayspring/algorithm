package q138477;

// 명예의 전당 (1)
// https://school.programmers.co.kr/learn/courses/30/lessons/138477

import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        List<Integer> arr = new ArrayList<Integer>();

        for (int i = 0; i < score.length; i++) {
            if (i < k) {
                arr.add(score[i]);
            } else if (score[i] > Collections.min(arr)) {
                arr.remove(Collections.min(arr));
                arr.add(score[i]);
            }
            answer[i] = Collections.min(arr);
        }
        return answer;
    }
}