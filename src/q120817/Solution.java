package q120817;

// 배열의 평균값
// https://school.programmers.co.kr/learn/courses/30/lessons/120817

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;

        for(int i = 0; i < numbers.length; i++) {
            answer += numbers[i];
        }

        answer /= numbers.length;

        return answer;
    }
}