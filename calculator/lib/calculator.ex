defmodule Calculator do
  use Application

  def start(_type, _args) do
    Calculator.main()
    Supervisor.start_link([], strategy: :one_for_one)
  end

  def input_numbers do
    IO.puts("Enter your first number: ")
    first_number =
      IO.gets("")
      |> String.trim()
      |> String.to_float()

    IO.puts("Enter your operator: ")
    operator =
      IO.gets("")
      |> String.trim()

    IO.puts("Enter your second number: ")
    second_number =
      IO.gets("")
      |> String.trim()
      |> String.to_float()

    calculator(first_number, operator, second_number)
  end


  def calculator(f, o, s) do
    result =
      case o do
        "+" -> f + s
        "-" -> f - s
        "*" -> f * s
        "/" -> f / s
        "%" -> rem(f, s)
        _ -> IO.puts("Something Went Wrong"); 0
      end
    output_result(result)
  end


  def output_result(r) do
    IO.puts(:"The Result Is #{r}")
  end

  def main do
    IO.puts("Calculator Is Running")
    input_numbers()
  end
end
