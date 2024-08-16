package q133499;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] strO = {"aya", "ye", "woo", "ma"};
        String[] strX = {"ayaaya", "yeye", "woowoo", "mama"};

        for (int i = 0; i < babbling.length; i++) {
            for (int j = 0; j < strO.length; j++) {
                babbling[i] = babbling[i].replaceAll(strX[j], "1").replaceAll(strO[j], " ");
            }
            if (babbling[i].trim().isEmpty()) {
                answer++;
            }
        }
        return answer;
    }
}