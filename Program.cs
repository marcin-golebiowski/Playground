using System.Collections.Generic;

namespace C_14
{
    public static class StringExtensions
    {
        // Instance-style extension members
        extension(string)
        {
            //    👇 static extension method
            public static bool HasValue(string value)
                => !string.IsNullOrEmpty(value);
        }

        extension<T>(IEnumerable<T> source)
        {
            public bool IsEmpty => !source.Any();
            public IEnumerable<T> Where(Func<T, bool> predicate) => source.Where(predicate);
        }

        // Type-level (static) extension members
        extension(string target)
        {
            //   👇 no static modifier
            public bool HasValue2 => !string.IsNullOrEmpty(target);
            //                 👆 'this' receiver parameter  removed

        }
    }


    internal class Program
    {
        delegate bool TryParse<T>(string text, out T result);

        static void Main(string[] args)
        {
            //1. Getting generic type names: You can now use the nameof(List<>), which will evaluate to List.
            string nameOfType = nameof(List<>);
            Console.WriteLine(nameOfType);


            //2.Simplified Lambda syntax: This will remove the current requirement of having to declare parameter types when using modifiers.
            TryParse<int> parse1 = (text, out result) =>
                Int32.TryParse(text, out result); // Valid in C# 14

            // Currently required:
            TryParse<int> parse2 = (string text, out int result) =>
                Int32.TryParse(text, out result);


            //3. Command class before and after
            // Preview in C# 13: It’s worth noting that the field keyword is available as a preview feature in C# 13.

            //4. Extension members (instance and static)

            //5. First -class Span<T> conversions

            void Print(ReadOnlySpan<char> text)
            {
                foreach (var ch in text) Console.Write(ch);
            }

            string s = "hello";
            char[] buffer = ['w', 'o', 'r', 'l', 'd'];

            Print(s);        // string -> ReadOnlySpan<char>
            Print(buffer);   // char[] -> ReadOnlySpan<char>

            void Mutate(Span<int> span) { span[0] = 42; }
            Mutate(span: new int[] { 1, 2, 3 });  // array -> Span<int>


            //6. User-defined compound assignment operators
            var c = new Counter(1);
            c += 4; // uses your operator +


            //7. Null - conditional assignment

            var customer = TryGetCustomer();

            customer?.UpdateName("New Name"); // Calls UpdateName only if customer is not null

        }


        static Customer TryGetCustomer()
        {
            // Simulate fetching a customer, which may return null
            return null; // or return new Customer { Name = "Existing Name" };
        }

    public readonly record struct Counter(int Value)
        {
            public static Counter operator +(Counter c, int delta) => new(c.Value + delta);
            // Compound assignment hooks into your operator implementation

           
        }

        class Customer
        {
            public string Name { get; set; }
            public void UpdateName(string newName)
            {
                Name ??= newName; // Assigns newName only if Name is null
            }
        }
        

        class Command
        {
            private string _msg;
            public string Message
            {
                get => _msg;
                set => _msg = value ?? throw new ArgumentNullException(nameof(value));
            }
        }

        class CommandInCSharp14
        {
            public string Message
            {
                get;
                set => field = value ?? throw new ArgumentNullException(nameof(value));
            }
        }
    }
}
