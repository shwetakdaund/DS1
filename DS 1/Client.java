import java.rmi.Naming;

public class Client{
    public static void main(String[] args) {           //here
            try{
        String url ="//localhost:1098/ArithmeticService";           
        Server arithmeticService = (Server) Naming.lookup(url);          //here

    int a =10;
    int b = 5;

    System.out.println("Addition of " + a + "+" + b + "=" + arithmeticService.add(a,b));
    System.out.println("Addition of " + a + "-" + b + "=" + arithmeticService.subtract(a,b));
    System.out.println("Addition of " + a + "*" + b + "=" + arithmeticService.multiply(a,b));
    System.out.println("Addition of " + a + "/" + b + "=" + arithmeticService.divide(a,b));
    
    }
    catch(Exception e){
        e.printStackTrace();           //here
    }
}
}