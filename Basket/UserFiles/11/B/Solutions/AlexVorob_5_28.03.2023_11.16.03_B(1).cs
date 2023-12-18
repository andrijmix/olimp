internal class Program
{
    private static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine());
        string text = Console.ReadLine();
        for (int i = 0; i < n; i++)
        {
            Console.Write(text + " ");
        }
    }
}