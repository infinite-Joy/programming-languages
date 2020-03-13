package example

class User(var name: String, var age: Int) {
  override def toString = s"User(name=$name, age=$age)"

  def this() {
    this("Joydeep", 1000)
  }

  def this(name: String) {
    this(name, 100)
  }
  
}

object Demo {
  def main(args: Array[String]) = {
    var user1 = new User("Joydeep", 30)
    println(user1.toString)
    var user2 = new User()
    println(user2.toString)
    var user3 = new User("Joydeep")
    println(user3.toString)

  }
}

trait Greeting {
  lazy val greeting: String = "hello"
}
