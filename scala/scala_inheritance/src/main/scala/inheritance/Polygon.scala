package Inheritance

class Polygon {
    def area: Double = 0.0
}

object Polygon {
    def main(args: Array[String]) = {
        var poly = new Polygon;
        var rect = new Rectangle(12, 15)
        var triangle = new Triangle(12, 15)
        printArea(poly)
        printArea(rect)
        printArea(triangle)
    }

    def printArea(p: Polygon) {
        println(p.area)
    }
}