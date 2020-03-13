package Inheritance

class Triangle(var width: Double, var height: Double) extends Polygon {
    override def area: Double = width * height / 2
}