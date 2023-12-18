using System;

namespace ConsoleApp33
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            int offset = 3;
            string output = string.Empty;

            foreach (var item in input)
            {
                if (item >= 97 && item <= 122)
                {
                    int decodedValue = item - offset;

                    if (decodedValue < 97)
                    {
                        int correctValue = 123 - (97 - decodedValue);
                        output += (char)(correctValue);
                    }
                    else
                    {
                        output += (char)(decodedValue);
                    }
                    
                }
                else if (item >= 65 && item <= 90)
                {
                    int decodedValue = item - offset;

                    if (decodedValue < 65)
                    {
                        int correctValue = 91 - (65 - decodedValue);
                        output += (char)(correctValue);
                    }
                    else
                    {
                        output += (char)(decodedValue);
                    }
                }
                else
                {
                    output += item;
                }   
            }

            Console.WriteLine(output);
        }
    }
}