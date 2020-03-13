package example

object Hello {
  def add(x: Int, y: Int) = x + y;
  def subtract(x: Int, y: Int) = x - y;
  def multiply(x: Int, y: Int) = x * y;
  def divide(x: Int, y: Int) = x / y;

  def main(args: Array[String]):T = {
    println(add(45, 15))
  }
}

trait Greeting {
  lazy val greeting: String = "hello"
}
