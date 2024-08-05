package q12915;

// 문자열 내 마음대로 정렬하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12915

import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};

        for(int i = 0; i < strings.length; i++){
            strings[i] = strings[i].charAt(n) + strings[i];
        }

        Arrays.sort(strings);

        for(int i = 0; i < strings.length; i++){
            strings[i] = strings[i].substring(1);
        }

        return strings;
    }
}