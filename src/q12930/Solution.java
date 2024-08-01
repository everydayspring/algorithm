package q12930;

// 이상한 문자 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12930#

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.split(" ");

        for(int i = 0; i < strArr.length; i++) {
            String[] strArr2 = strArr[i].split("");
            for(int j = 0; j < strArr2.length; j++) {
                if(j % 2 == 0) {
                    answer += strArr2[j].toUpperCase();
                } else {
                    answer += strArr2[j].toLowerCase();
                }
            }
            answer += " ";
        }

        answer = answer.substring(0, answer.length() - 1);

        if(s.substring(s.length() - 1).equals(" ")){
            answer += s.substring(answer.length());
        }


        return answer;
    }
}
