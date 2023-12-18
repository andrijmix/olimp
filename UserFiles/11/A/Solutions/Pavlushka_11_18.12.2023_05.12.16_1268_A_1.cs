using System;
using System.Collections.Generic;
using System.Linq;
public class Program
{
	public static void Main(string[] args)
	{
		var numbers = Console.ReadLine().Split(" ")
			.Select(x => Convert.ToInt32(x))
			.Where(x => (x % 7) == 0 && (x % 5) != 0);

		Console.WriteLine(string.Join(" ", numbers));
	}
}