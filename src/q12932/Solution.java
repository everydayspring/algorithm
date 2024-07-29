package q12932;

// 자연수 뒤집어 배열로 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12932

class Solution {
    public int[] solution(long n) {
        int len = Long.toString(n).length();

        int[] answer = new int[len];

        for (int i = 0; i < len; i++) {
            answer[i] = (int) (n % 10);
            n *= 0.1;
        }

        return answer;
    }
}