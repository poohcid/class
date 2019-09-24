public class Car{
    private double num;
    private int count;

    public Car(){
        this(3.14, 200);
    }

    public Car(double num){
        this(num, 200);
    }

    public Car(double num, int count){
        this.num = num;
        this.count = count;
    }

    public double getNum(){
        return num;
    }

    public void setNum(double num){
        this.num = num;
    }

    public void setCount(int count){
        this.count = count;
    }

    public int getCount(){
        return count;
    }

    public void copy(Car car1){
        car1.setNum(num);
        car1.setCount(count);
    }

    public String toString(){
        return ""+num+" "+count;
    }
}