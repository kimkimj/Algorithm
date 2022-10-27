import java.util.HashMap;
import java.util.Map;

public class ProgrammersHash {
    /*
    * participant 배열에 있는 참가자를 hash table에 저장. Key = 이름. Value = 0
    * completion 배열에 있는 참가자를 같은 hash table에서 찾고, value를 1로 고침
    * hash table의 key set을 모두 iterate
    * key가 0 (completion에 없는 참가자) 이면 그 사람 이름 return
    *
    *ERROR: 동명이인이 있고, 한사람이 완주했을 때 무조건 완주한 사람으로 처리됨
    *REFACTOR: allParticipants의 value를 count로 사용.
    * */

    public static void main(String[] args) {
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};

        System.out.println(solution(participant, completion));
    }
    public static String solution(String[] participant, String[] completion) {
        Map<String, Integer> allParticipants = new HashMap<>();

        // 참가자 이름 모두 저장
        for (int i = 0; i < participant.length; i++) {
            String key = participant[i];
            if (!allParticipants.containsKey(key)){
                allParticipants.put(key, 0);
            }
            allParticipants.put(key, allParticipants.get(key) + 1);
        }

        // 완주한 이름 모두 value 고치기
        for (int i = 0; i < completion.length ; i++) {
            String key = completion[i];
            allParticipants.put(key, allParticipants.get(key) - 1);
        }

        for (String key: allParticipants.keySet()){
            if(allParticipants.get(key) > 0){
                return key;
            }
        }
        return "";
    }
}
