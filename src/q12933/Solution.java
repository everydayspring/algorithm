package q12933;

// 정수 내림차순으로 배치하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12933

import java.util.*;

class Solution {
    public long solution(long n) {
        long answer;
        String str = "";
        String[] strArr = Long.toString(n).split("");
        Arrays.sort(strArr, Collections.reverseOrder());

        for (String s : strArr) {
            str += s;
        }

        answer = Long.parseLong(str);

        return answer;
    }
}