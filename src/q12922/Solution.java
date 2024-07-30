package q12922;

// 수박수박수박수박수박수?
// https://school.programmers.co.kr/learn/courses/30/lessons/12922

class Solution {
    public String solution(int n) {
        String waterMelon = "수박";
        String answer = "";

        for(int i = 0; i < n/2; i++){
            answer += waterMelon;
        }

        if(n % 2 != 0) {
            answer += "수";
        }

        return answer;
    }
}