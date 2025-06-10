/**
 * 冒泡排序算法实现
 * 包含基础版本和优化版本的冒泡排序
 * 
 * @author Cursor AI (Claude-4-opus max)
 * @date 2024
 */
public class BubbleSort {
    
    /**
     * 基础版本的冒泡排序
     * 时间复杂度：O(n²)
     * 空间复杂度：O(1)
     * 
     * @param arr 待排序的数组
     */
    public static void bubbleSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        // 外层循环控制排序趟数
        for (int i = 0; i < n - 1; i++) {
            // 内层循环控制每趟比较次数
            for (int j = 0; j < n - 1 - i; j++) {
                // 如果前面的数大于后面的数，交换位置
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                }
            }
        }
    }
    
    /**
     * 优化版本1：添加标志位，如果某趟没有交换，说明已经有序
     * 最好情况时间复杂度：O(n)
     * 
     * @param arr 待排序的数组
     */
    public static void bubbleSortOptimized1(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;  // 标记是否发生交换
            
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    swapped = true;
                }
            }
            
            // 如果这一趟没有发生交换，说明已经有序
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 优化版本2：记录最后一次交换的位置，下次只需要比较到这个位置
     * 
     * @param arr 待排序的数组
     */
    public static void bubbleSortOptimized2(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int n = arr.length;
        int lastSwapIndex = n - 1;  // 记录最后一次交换的位置
        
        while (lastSwapIndex > 0) {
            int currentSwapIndex = 0;  // 当前趟最后一次交换的位置
            
            for (int j = 0; j < lastSwapIndex; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j + 1);
                    currentSwapIndex = j;  // 更新最后交换位置
                }
            }
            
            lastSwapIndex = currentSwapIndex;
        }
    }
    
    /**
     * 鸡尾酒排序（双向冒泡排序）
     * 从两个方向进行冒泡排序，可以在某些情况下更快
     * 
     * @param arr 待排序的数组
     */
    public static void cocktailSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int left = 0;
        int right = arr.length - 1;
        
        while (left < right) {
            // 从左到右冒泡
            for (int i = left; i < right; i++) {
                if (arr[i] > arr[i + 1]) {
                    swap(arr, i, i + 1);
                }
            }
            right--;
            
            // 从右到左冒泡
            for (int i = right; i > left; i--) {
                if (arr[i] < arr[i - 1]) {
                    swap(arr, i, i - 1);
                }
            }
            left++;
        }
    }
    
    /**
     * 交换数组中两个元素的位置
     * 
     * @param arr 数组
     * @param i 第一个元素的索引
     * @param j 第二个元素的索引
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    /**
     * 打印数组
     * 
     * @param arr 待打印的数组
     * @param message 打印前的提示信息
     */
    private static void printArray(int[] arr, String message) {
        System.out.print(message + ": ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
    
    /**
     * 复制数组
     * 
     * @param arr 原数组
     * @return 复制后的新数组
     */
    private static int[] copyArray(int[] arr) {
        int[] newArr = new int[arr.length];
        System.arraycopy(arr, 0, newArr, 0, arr.length);
        return newArr;
    }
    
    /**
     * 测试冒泡排序的性能
     * 
     * @param arr 待排序数组
     * @param sortName 排序算法名称
     * @param sortMethod 排序方法
     */
    private static void testSort(int[] arr, String sortName, java.util.function.Consumer<int[]> sortMethod) {
        int[] testArr = copyArray(arr);
        long startTime = System.nanoTime();
        sortMethod.accept(testArr);
        long endTime = System.nanoTime();
        
        System.out.println("\n" + sortName + ":");
        printArray(testArr, "排序后");
        System.out.println("耗时: " + (endTime - startTime) / 1000 + " 微秒");
    }
    
    /**
     * 主函数：演示和测试各种冒泡排序算法
     */
    public static void main(String[] args) {
        System.out.println("=== 冒泡排序算法演示 ===\n");
        
        // 测试用例1：普通数组
        int[] testArray1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("测试用例1：普通未排序数组");
        printArray(testArray1, "原始数组");
        
        testSort(testArray1, "基础冒泡排序", BubbleSort::bubbleSort);
        testSort(testArray1, "优化版本1（带标志位）", BubbleSort::bubbleSortOptimized1);
        testSort(testArray1, "优化版本2（记录最后交换位置）", BubbleSort::bubbleSortOptimized2);
        testSort(testArray1, "鸡尾酒排序（双向冒泡）", BubbleSort::cocktailSort);
        
        // 测试用例2：已经排序的数组
        System.out.println("\n\n测试用例2：已排序数组（测试最优情况）");
        int[] testArray2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        printArray(testArray2, "原始数组");
        
        testSort(testArray2, "基础冒泡排序", BubbleSort::bubbleSort);
        testSort(testArray2, "优化版本1（带标志位）", BubbleSort::bubbleSortOptimized1);
        
        // 测试用例3：逆序数组
        System.out.println("\n\n测试用例3：逆序数组（测试最坏情况）");
        int[] testArray3 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        printArray(testArray3, "原始数组");
        
        testSort(testArray3, "基础冒泡排序", BubbleSort::bubbleSort);
        testSort(testArray3, "优化版本1（带标志位）", BubbleSort::bubbleSortOptimized1);
        
        // 测试用例4：包含重复元素
        System.out.println("\n\n测试用例4：包含重复元素的数组");
        int[] testArray4 = {5, 2, 8, 2, 9, 1, 5, 5};
        printArray(testArray4, "原始数组");
        
        testSort(testArray4, "基础冒泡排序", BubbleSort::bubbleSort);
        
        // 测试用例5：单个元素和空数组
        System.out.println("\n\n测试用例5：边界情况");
        int[] testArray5 = {42};
        int[] testArray6 = {};
        
        System.out.println("单元素数组：");
        printArray(testArray5, "原始数组");
        bubbleSort(testArray5);
        printArray(testArray5, "排序后");
        
        System.out.println("\n空数组：");
        printArray(testArray6, "原始数组");
        bubbleSort(testArray6);
        printArray(testArray6, "排序后");
        
        // 性能对比测试
        System.out.println("\n\n=== 性能对比测试 ===");
        System.out.println("生成包含1000个随机数的数组进行测试...\n");
        
        int[] largeArray = new int[1000];
        java.util.Random random = new java.util.Random();
        for (int i = 0; i < largeArray.length; i++) {
            largeArray[i] = random.nextInt(1000);
        }
        
        // 测试各种排序算法的性能
        long start, end;
        
        int[] test1 = copyArray(largeArray);
        start = System.nanoTime();
        bubbleSort(test1);
        end = System.nanoTime();
        System.out.println("基础冒泡排序耗时: " + (end - start) / 1000000 + " 毫秒");
        
        int[] test2 = copyArray(largeArray);
        start = System.nanoTime();
        bubbleSortOptimized1(test2);
        end = System.nanoTime();
        System.out.println("优化版本1耗时: " + (end - start) / 1000000 + " 毫秒");
        
        int[] test3 = copyArray(largeArray);
        start = System.nanoTime();
        bubbleSortOptimized2(test3);
        end = System.nanoTime();
        System.out.println("优化版本2耗时: " + (end - start) / 1000000 + " 毫秒");
        
        int[] test4 = copyArray(largeArray);
        start = System.nanoTime();
        cocktailSort(test4);
        end = System.nanoTime();
        System.out.println("鸡尾酒排序耗时: " + (end - start) / 1000000 + " 毫秒");
        
        System.out.println("\n程序执行完毕！");
    }
} 