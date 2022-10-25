import static java.util.Objects.hash;

public class Hash {
    private int size = 1000;
    private int[] bucket = new int[size];

    public Hash(int size){
        this.size = size;
        this.bucket = new int[size];
    }

    public int hash(String key) {
        int asciiSum = 0;
        for (int i = 0; i < key.length(); i++) {
            asciiSum += key.charAt(i);
        }
        return asciiSum % size;
    }

    public void insert(String key, int value){
        int hashCode = hash(key);
        bucket[hashCode] = value;
        System.out.println(key + " " + hashCode + "방에 저장");
    }

    public int search(String key){
        return bucket[hash(key)];
    }
}
