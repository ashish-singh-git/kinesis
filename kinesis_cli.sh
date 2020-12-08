aws kinesis describe-stream --stream-name [stream_name] --region [region]

aws kinesis put-record --stream-name [stream_name] --partition-key [partition_key] --data [data] --region [region] --cli-binary-format raw-in-base64-out

aws kinesis get-shard-iterator --stream-name [stream_name] --shard-iterator-type TRIM_HORIZON --shard-id [shard_id]

aws kinesis get-records --shard-iterator [shard_iterator] --limit 2

echo [data] | base64 --decode