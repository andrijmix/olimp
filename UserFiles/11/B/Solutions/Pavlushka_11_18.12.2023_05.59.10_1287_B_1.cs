using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
	static void Main()
	{
		var result = Console.ReadLine()
			.Select(x => char.IsLetter(x) ? 
			(char)(((x - 'a' - 3 + 26) % 26) + 'a') : x);

		Console.WriteLine(new string(result.ToArray()));
	}
}