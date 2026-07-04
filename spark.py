from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data =[
    (1, "Alice"),
    (2, "Hentry"),
    (3, "John"),
    (None, "Kamal"),

]

df = spark.createDataFrame(data, ["id", "name"])
df.filter(df.id.isNotNull()).show

employees = spark.createDataFrame([(1,"Nethmi","DE-1"),(2,"Dasuni","DE-2"),(2,"Imasha","DE-2")],("id","name","dept"))
departments = spark.createDataFrame([("DE-1","HR"),("DE-2","IT"),("DE-2","Finance")])
employees.join(departments,employees.dept==departments.id,"left").show()