public class Stack1 {
    private int[] arr;
    private int size;

    public Stack1(){
        arr = new int[1000];
        size = 0;
    }
    public int[] push(int value){
        if (size == arr.length){
            int[] bigger = new int[size * 2];
            for (int i = 0; i < size; i++) {
                bigger[i] = arr[i];
            }
            arr = bigger;
        }
        arr[size] = value;
        size++;
        return arr;
    }

}
