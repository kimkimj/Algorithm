package DataStructures;

import java.util.Stack;

public class Parenthesis{
    // )()(
    public static boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if('(' == s.charAt(i)){
                stack.push(s.charAt(i));
            } else if(')' == s.charAt(i)) {
                if(stack.empty()){
                    return false;
                } else{
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();

        /*
        if (s.charAt(0) == ')'){
            return false;
        }

        for (int i = 0; i < s.length(); i++){
            char current = s.charAt(i);
            if (stack.isEmpty()){
                stack.push(current);
            } else{
                if (stack.peek() == '(' && current == ')'){ //(는 무조건 stack에 넣고 )면 스택에 (가 있다면 pop해준다.
                    stack.pop();
                // )가 남는 경우에도 계속 )를 넣고, 마지막에 사이즈 체크를 해 return false를 하게 된다
                } else{
                    stack.push(current);
                }
            }
        }
        return stack.isEmpty();*/
    }
}