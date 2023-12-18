internal class Program
{
    private static void Main(string[] args)
    {
        string[] inp = Console.ReadLine().Split(' ');
        int a = int.Parse(inp[0]);
        int b = int.Parse(inp[1]);
        int c = a + b;
        Console.WriteLine(c);
    }
}