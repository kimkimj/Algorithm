import java.util.EmptyStackException;

public class Stack02 {
    private Integer[] arr;
    private int top=0;
    public Stack02(){
        arr=new Integer[10000]; }
    public Stack02(int size){

        this.arr = new Integer[size];
    }
    public void push(int value){
        arr[top++] = value;
    }
    public Integer[] getArr(){
        return arr;
    }

    public int pop(){
        if (top == 0){
            throw new EmptyStackException();
        }
        return arr[--top];
    }

    public boolean isEmpty(){
        return top == 0;
    }

    public int peek() {
        if (top == 0){
            throw new EmptyStackException();
        }
        return arr[top - 1];
    }
}