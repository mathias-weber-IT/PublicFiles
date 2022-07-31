SELECT

  Run_Date,

  row_expectations.dataset as dataset,

  row_expectations.name as expectation,

  row_expectations.passed_records,

  row_expectations.failed_records

FROM

  (

    SELECT timestamp AS Run_Date,

      explode(

        from_json(

          details :flow_progress :data_quality :expectations,

          "array<struct<name: string, dataset: string, passed_records: int, failed_records: int>>"

        )

      ) row_expectations

    FROM

      event_log_raw

    WHERE

      event_type = 'flow_progress'

  )
