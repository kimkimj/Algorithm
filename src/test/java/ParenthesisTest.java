import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ParenthesisTest {
    @Test
    @DisplayName("solve_return_boolean")
    void parenthesis(){
        Parenthesis p1 = new Parenthesis();
        assertTrue(p1.solution("()()"));
        assertTrue(p1.solution("(())()"));
        assertFalse((p1.solution(")()(")));
        assertFalse((p1.solution(")()(")));
        //assertFalse(p1.solution("())("));

    }
}