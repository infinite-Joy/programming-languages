package example

import java.util.Date

object Hello {
  def add(x: Int, y: Int) = x + y;
  def subtract(x: Int, y: Int) = x - y;
  def multiply(x: Int, y: Int) = x * y;
  def divide(x: Int, y: Int) = x / y;
  def subtract_double(x: Double, y: Double) = x - y;

  // higher order functions
  def math(x: Double, y: Double, f: (Double, Double) => Double) = f(x, y);

  // partially applied function
  def log(date: Date, message: String) = {
    println(date + " " + message);
  }

  def main(args: Array[String]) = {
    println("computation for simple add function: " + add(45, 15))
    println("computation for subtract_double: " + math(45.1, 15.1, subtract_double))

    val date = new Date;
    val newLog = log(date, _: String)
    newLog("the message 1")
    newLog("the message 2")
    newLog("the message 3")
    newLog("the message 4")
  }
}

trait Greeting {
  lazy val greeting: String = "hello"
}
