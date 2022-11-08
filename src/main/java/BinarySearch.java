public class BinarySearch {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int num = 9;
        System.out.println(solution(arr, num));
    }


    // This method returns the index of the given number in a given array
    public static int solution(int[] arr, int num){

        // Bug: 처음 나눈 반에서 찾는 숫자가 없다면 무한 반복..-> start midIndex & end midIndex
        int startIndex = 0;
        int endIndex = arr.length - 1;
        int midIndex = endIndex / 2;

        while (midIndex >= startIndex && midIndex <= endIndex) { // while(start <= end){
            if (num == arr[midIndex]){
                return midIndex;
            } else if (num > arr[midIndex]){
                startIndex = midIndex + 1;
                System.out.println("the number is higher than " + arr[midIndex]);
            } else {
                endIndex = midIndex - 1;
                System.out.println("the number is lower than " + arr[midIndex]);
            }
            midIndex = (startIndex + endIndex) / 2;
        }
        return -1;
    }
}
