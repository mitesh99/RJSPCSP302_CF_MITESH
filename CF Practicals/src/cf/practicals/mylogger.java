/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cf.practicals;

/**
 *
 * @author hp
 */
import java.io.*; 
import java.util.logging.*; 
public class mylogger
{
public static void main(String args[])
{
Logger l=Logger.getLogger(mylogger.class.getName()); 
FileHandler fh;
try
{
fh=new FileHandler("d:/mylogfile.log",true); 
l.addHandler(fh);
l.setLevel(Level.ALL); 
SimpleFormatter sf=new SimpleFormatter(); 
fh.setFormatter(sf);
l.info("Myfirstlog");
}
catch(SecurityException e)
{
e.printStackTrace();
}
catch(IOException e)
{
e.printStackTrace();
}
l.info("HiHowru?");
}
}