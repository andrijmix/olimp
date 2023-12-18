using System;

namespace olimpA
{
    class Progmam
    {
        static void Main(string[] args)
        {
            uint a = 0;
            string str = "";
            try
            {
                Console.Write("Enter word or string for repeat: ");
                str = Console.ReadLine();
                Console.Write($"Enter number of state for repeat this ({str}): ");
                a = Convert.ToUInt32(Console.ReadLine());
                Console.WriteLine("In working");
                for (int i = 0; i < a; i++)
                {
                    Console.WriteLine(str);   
                }
                Console.WriteLine("Done repeated");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
        }
    }
}