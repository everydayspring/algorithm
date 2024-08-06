package q134240;

// 푸트 파이트 대회
// https://school.programmers.co.kr/learn/courses/30/lessons/134240

class Solution {
    public String solution(int[] food) {
        String answer = "0";

        for(int i = food.length - 1; i > 0; i--){
            for(int j = 0; j < food[i] / 2; j++){
                answer = i + answer + i;
            }
        }
        return answer;
    }
}
