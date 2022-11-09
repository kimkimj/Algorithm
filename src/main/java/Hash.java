import java.util.ArrayList;
import java.util.List;

import static java.util.Objects.hash;

public class Hash {

    class Node {
        private String key;
        private Integer value;

        public Node(String key, Integer value) {
            this.key = key;
            this.value = value;
        }

        public String getKey() {
            return key;
        }

        public Integer getValue() {
            return value;
        }
    }

    private int size = 1000;
    //private int[] table = new int[size];
    // Array of List<Node>
    private List<Node>[] table = new List[size];

    public Hash(int size){
        this.size = size;
        //this.table = new int[size];
    }

    public int hash(String key) {
        int asciiSum = 0;
        for (int i = 0; i < key.length(); i++) {
            asciiSum += key.charAt(i);
        }
        return asciiSum % size;
    }

    public void insert(String key, Integer value){
        int hashCode = hash(key);
        if (table[hashCode] == null) {
            table[hashCode] = new ArrayList<>();
        }
        table[hashCode].add(new Node(key, value));
    }

    public Integer get(String key) {
        List<Node> nodes = this.table[hash(key)];
        for (Node node : nodes) {
            if (key.equals(node.getKey())) {
                return node.value;
            }
        }
        return null;
    }

}
