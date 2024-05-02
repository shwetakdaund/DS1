import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ServerImpl extends UnicastRemoteObject implements Server{
    public ServerImpl () throws RemoteException{             //here
        super();
    }

    public int add(int a,int b)throws RemoteException{
        return a+b;
    }
    public int subtract(int a,int b)throws RemoteException{
        return a-b;
    }
    public int multiply(int a,int b)throws RemoteException{
        return a*b;
    }
    public double divide(int a,int b)throws RemoteException{
        if(b==0){
            throw new RemoteException("Cannot divide by 0");            //here
        }
        return a/b;
    }
    
    public static void main(String[] args) {
        try{
            int registryPort = 1098;
            Server arithmeticService = new ServerImpl();                                                                            //here
            java.rmi.registry.LocateRegistry.createRegistry(registryPort);
            java.rmi.Naming.rebind("//localhost:" + registryPort + "/ArithmeticService", arithmeticService);                      //here
            System.out.println("ArithmeticService is ready on " + registryPort);

        }catch(Exception e){
            e.printStackTrace();              //here
        }
    }
}
