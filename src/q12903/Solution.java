package q12903;

// 가운데 글자 가져오기
// https://school.programmers.co.kr/learn/courses/30/lessons/12903

class Solution {
    public String solution(String s) {
        String answer = "";

        if(s.length() % 2 == 0){
            answer = Character.toString(s.charAt(s.length() / 2 - 1));
            answer += Character.toString(s.charAt(s.length() / 2));
        } else {
            answer = Character.toString(s.charAt(s.length() / 2));
        }

        return answer;
    }
}
