import java.util.Stack;

public class Parenthesis{
    // )()(
    public static boolean solution(String s) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < s.length(); i++){
            char current = s.charAt(i);
            if (!st.isEmpty()){
                if ((current == ')' && st.peek() == '(') || (current == '(' && st.peek() == ')')) {
                    st.pop();
                } else{
                    st.push(current);
                }
            } else{
                // if the stack is empty, and the parenthesis is )
                if (current == ')'){
                    return false;
                } else {
                    st.push(current);
                }
            }
        }
        return st.isEmpty();
    }
}