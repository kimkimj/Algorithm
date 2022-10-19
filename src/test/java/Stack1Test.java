import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Stack1Test {
    @Test
    @DisplayName("push and pop works")
    void pushAndPop(){
        Stack1 stack1 = new Stack1();
        stack1.push(10);
        stack1.push(20);
        Assertions.assertEquals(20, stack1.pop());
        Assertions.assertEquals(10, stack1.pop());

        stack1.push(30);
        Assertions.assertEquals(30, stack1.pop());
    }

}