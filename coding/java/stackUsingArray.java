package coding.java;

public class stackUsingArray {
    private int array[];
    private int top;
    private int capacity;

    stackUsingArray(int capacity) {
        this.array = new int[capacity];
        this.capacity = capacity;
        this.top = -1;
    }

    public void push(int item){
        if (isFull()){
            throw new RuntimeException("Stack is Full ..1111 !!!");
        }
        array[++top] = item;
    }

    public int pop(){
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty ...2222 !!!");
        }
        return array[top--];
    }

    public int peek(){
        if (isEmpty()){
            throw new RuntimeException("Stack is empty ...333 !!!");
        }
        return array[top];
    }

    public boolean isEmpty(){
        return top == -1;
    }

    public boolean isFull(){
        return top == capacity - 1;
    }

    public void display(){

        if(isEmpty()){
            System.out.println("Stack is Empty !!!!!");
            return;
        }

        System.out.println("Stack Elements ....");

        for(int i = top; i >= 0; i--){
            System.out.println(array[i]);
        }
    }

    public static void main(String[] args) {
        
        stackUsingArray stack = new stackUsingArray(5);

        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);
        stack.push(60);
        

        stack.display();

        System.out.println("Top Element : " + stack.peek());
        System.out.println("Pooped Element : " + stack.pop());

        stack.display();
    }
    
}
