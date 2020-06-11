package Inheritance

trait Shape {
    def color: String;
}

abstract class Polygon {
    def area: Double
}

object Polygon {
    def main(args: Array[String]) = {
        var rect = new Rectangle(12, 15)
        var triangle = new Triangle(12, 15)
        printArea(rect)
        println(rect.color)
        // show_color(rect)
        printArea(triangle)
        println(triangle.color)
        // show_color(triangle)
    }

    def printArea(p: Polygon) {
        val this_area = p.area
        val class_name = p.getClass.getName
        println(s"area of class $class_name is $this_area")
    }

    // def show_color(p: Polygon) {
    //     val color = p.color
    //     val class_name = p.getClass.getName
    //     println(s"color of class $class_name is $color_")
    // }
}