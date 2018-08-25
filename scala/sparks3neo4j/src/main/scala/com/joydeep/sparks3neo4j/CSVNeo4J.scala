package com.joydeep.SparkS3Neo4j

import org.apache.spark.{SparkConf, SparkContext}
import org.neo4j.spark._
import org.graphframes._

/**
  * Use this to test the app locally, from sbt:
  * sbt run
  *  (+ select CSVNeo4JLocal when prompted)
  */
object CSVNeo4JLocal extends App{
  val conf = new SparkConf()
    .setMaster("local")
    .setAppName("my awesome app")

  Runner.run(conf)
}

/**
  * Use this when submitting the app to a cluster with spark-submit
  * */
object CSVNeo4J extends App{
  // spark-submit command should supply all necessary config elements
  Runner.run(new SparkConf())
}

object Runner {
  def run(conf: SparkConf, inputFile: String, outputFile: String): Unit = {
    val sc = new SparkContext(conf)

    // Create the rdd of the s3 csv data.
    val lines = sc.textFile("s3a://gdelt-open-data/events/20180823.export.csv")

    // filter out only the columns that we want.
    val filteredlines = lines.map(_.split("\t")).map{x => (x(0), x(15))}

    // Build the dataframe
    val newNames = Seq("event", "place")
    val df = filteredlines.toDF(newNames: _*)

    // Push to Neo4J
    Neo4jDataFrame.mergeEdgeList(sc, df, ("Event",Seq("event")),("HAPPENED_IN",Seq.empty),("PLACE",Seq("place")))
  }
}
