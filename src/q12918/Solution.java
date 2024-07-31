package q12918;

// 문자열다루기 기본
// https://school.programmers.co.kr/learn/courses/30/lessons/12918

class Solution {
    public boolean solution(String s) {

        if(s.length() == 4 || s.length() == 6){
            try {

                int x = Integer.parseInt(s);
                return true;

            } catch(NumberFormatException e) {

                return false;

            }
        }
        else return false;
    }
}
