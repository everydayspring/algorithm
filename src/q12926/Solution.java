package q12926;

// 시저 암호
// https://school.programmers.co.kr/learn/courses/30/lessons/12926

class Solution {
    public String solution(String s, int n) {
        String answer = "";
        int num;

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i)==' '){
                answer += " ";
            }else if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z'){
                num = (int)s.charAt(i) + n;
                num = num > 122 ? num - 26 : num;
                answer += (char)num;

            } else {
                num = (int)s.charAt(i) + n;
                num = num > 90 ? num - 26 : num;
                answer += (char)num;
            }
        }
        return answer;
    }
}