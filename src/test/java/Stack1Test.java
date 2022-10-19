import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Stack1Test {
    @Test
    void pushTest() {
        Stack1 stack1 = new Stack1();
        int[] arr = stack1.push(10);
        stack1.push(20);
        Assertions.assertEquals(10, arr[0]);
        Assertions.assertEquals(20, arr[1]);
    }

}