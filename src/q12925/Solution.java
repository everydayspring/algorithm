package q12925;

// 문자열을 정수로 바꾸기
// https://school.programmers.co.kr/learn/courses/30/lessons/12925

class Solution {
    public int solution(String s) {
        int answer = 0;
        int minus = 1;

        if (s.charAt(0) == '-') {
            s = s.substring(1);
            minus = -1;
        }

        answer = minus * Integer.parseInt(s);

        return answer;
    }
}
