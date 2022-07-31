# Replace the text in the Storage Location to the desired pipeline storage location. This can be found in the pipeline configuration under 'storage'.

storage_location = "dbfs:/pipelines/XXXXXXXXXXXXXXXXXXXXXXX"

event_log_path = storage_location + "/system/events"

# Read the event log into a temporary view so it's easier to query.

event_log = spark.read.format('delta').load(event_log_path)

event_log.createOrReplaceTempView("event_log_raw")
