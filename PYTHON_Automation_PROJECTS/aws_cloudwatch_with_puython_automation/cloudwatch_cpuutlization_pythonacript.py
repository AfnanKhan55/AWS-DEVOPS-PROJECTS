import boto3
import datetime

cloudwatch = boto3.client('cloudwatch')

metric_name = 'CPUUtilization'
namespace = 'AWS/EC2'
instance_id = 'i-0bf30c5320d4190e9'

end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(hours=1)

response = cloudwatch.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': namespace,
                    'MetricName': metric_name,
                    'Dimensions': [{'Name': 'InstanceId', 'Value': instance_id}],
                },
                'Period': 300,
                'Stat': 'Average',
            },
            'ReturnData': True,
        },
    ],
    StartTime=start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
    EndTime=end_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
)

metric_data = response['MetricDataResults'][0]['Values']
print("Metric Data:", metric_data)
