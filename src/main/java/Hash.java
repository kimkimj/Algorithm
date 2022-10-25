import static java.util.Objects.hash;

public class Hash {
    private int size = 1000;
    private int[] bucket = new int[size];

    public Hash(int size){
        this.size = size;
        this.bucket = new int[size];
    }

    public void insert(int key, int value){
        int hashCode = hash(key);
        bucket[hashCode] = value;
        System.out.println(key + " " + hashCode + "방에 저장");
    }

    public int search(int key){
        return bucket[hash(key)];
    }
}
