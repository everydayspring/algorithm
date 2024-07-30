package q12948;

// 핸드폰 번호 가리기
// https://school.programmers.co.kr/learn/courses/30/lessons/12948

class Solution {
    public String solution(String phone_number) {
        char[] charArr = phone_number.toCharArray();

        for(int i = charArr.length - 5; i >= 0; i--) {
            charArr[i] = '*';
        }

        return new String(charArr);
    }
}
