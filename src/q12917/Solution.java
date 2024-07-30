package q12917;

// 문자열 내림차순으로 배치하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12917

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] arr  = s.toCharArray();

        Arrays.sort(arr);
        System.out.println(arr);

        for(int i = arr.length - 1; i >= 0; i--) {
            answer += arr[i];
        }

        return answer;
    }
}
