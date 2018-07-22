import Dependencies._
      
lazy val nd4jVersion = "0.7.2"

lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      organization := "com.example",
      scalaVersion := "2.12.5",
    )),
    name := "Hello",
    libraryDependencies ++= Seq(
      "org.nd4j" % "nd4j-api" % nd4jVersion,
      "org.nd4j" % "nd4j-native-platform" % nd4jVersion % Test,
      "ch.qos.logback" % "logback-classic" % "1.2.1" % Test,
    ),
  )
