import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class Stack02Test {
    @BeforeEach
    void setUp() {
        System.out.println("before each");
    }
    @Test
    @DisplayName("push")
    void push() {
        Stack02 st = new Stack02();
        st.push(10);
        st.push(20);
        Integer[] arr=st.getArr();
        assertEquals(20, arr[0]);
        assertEquals(10, arr[1]);
    }
    @Test
    void pushAndPop() {
        Stack02 st = new Stack02();
        st.push(10);
        st.push(20);
        assertEquals(20, st.pop());
        assertEquals(10, st.pop());
        st.push(30);
        assertEquals(30, st.pop());
    }

    @Test
    void isEmpty(){
        Stack02 st = new Stack02();
        assertTrue(st.isEmpty());
        st.push(10);
        assertFalse(st.isEmpty());

    }
}