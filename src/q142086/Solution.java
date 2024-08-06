package q142086;

// 가장 가까운 같은 글자
// https://school.programmers.co.kr/learn/courses/30/lessons/142086

import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        List<Character> arr = new ArrayList<>();

        for(int i = 0; i < s.length(); i++) {
            if(i == 0 || !arr.contains(s.charAt(i))){
                answer[i] = -1;
            } else {
                int j = i - 1;
                while(s.charAt(i) != arr.get(j)){
                    j--;
                }
                answer[i] = i - j;
            }
            arr.add(s.charAt(i));
        }
        return answer;
    }
}