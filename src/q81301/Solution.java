package q81301;

// 숫자 문자열과 영단어
// https://school.programmers.co.kr/learn/courses/30/lessons/81301

class Solution {
    public int solution(String s) {
        String[] strNum = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < strNum.length; i++) {
            s = s.replace(strNum[i], Integer.toString(i));
        }

        return Integer.parseInt(s);
    }
}