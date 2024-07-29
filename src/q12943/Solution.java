package q12943;

// 클라츠 추측
// https://school.programmers.co.kr/learn/courses/30/lessons/12943

// * 문제 오류로 조건을 500 -> 400 으로 수정

class Solution {
    public int solution(int num) {
        int answer = 0;

        if(num == 1) return 0;

        while(true) {

            answer++;

            if(num % 2 == 0) {
                num /= 2;
            } else {
                num = num * 3 + 1;
            }

            if(answer >= 400) {
                return -1;
            } else if (num == 1){
                return answer;
            }

        }

    }
}
