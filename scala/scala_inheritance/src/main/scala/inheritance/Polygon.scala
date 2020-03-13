package Inheritance

abstract class Polygon {
    def area: Double = 0.0
}

object Polygon {
    def main(args: Array[String]) = {
        var rect = new Rectangle(12, 15)
        var triangle = new Triangle(12, 15)
        printArea(rect)
        printArea(triangle)
    }

    def printArea(p: Polygon) {
        val this_area = p.area
        val class_name = p.getClass.getName
        println(s"area of class $class_name is $this_area")
    }
}