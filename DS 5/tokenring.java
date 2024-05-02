import java.util.Scanner;
public class tokenring{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter nodes");
        int nodes= sc.nextInt();

        System.out.println("Ring formed");

        for(int i=0;i<nodes;i++){
        System.out.print(i + " ");
        }
        System.out.println("0");

        int choice = 0;
        do{
        System.out.println("Enter Sender");
        int Sender = sc.nextInt();

        System.out.println("Enter Receiver");
        int Receiver = sc.nextInt();

        System.out.println("Enter data");
        String data = sc.next();

        int token = 0;

        for(int i=token;i<Sender;i++){                 //
            System.out.print(i+"->");
        }
        System.out.println(Sender);
        System.out.println("Sender " + Sender + " sending data "+ data);
            

        for(int i=Sender; i!=Receiver;i=(i+1)%nodes){
            System.out.println("Data "+ data + " is forwarded by " + i);
        }
        System.out.println("Receiver "+ Receiver+ " received the data "+ data);
        token = Sender;

        System.out.println("Do you want to proceed press 1 else 0");
        choice = sc.nextInt();
    }
        while(choice==1);
    }
}