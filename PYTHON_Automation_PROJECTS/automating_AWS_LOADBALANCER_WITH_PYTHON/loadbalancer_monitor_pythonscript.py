import boto3

client = boto3.client('elbv2')

def create_application_load_balancer(name, subnets):
    response = client.create_load_balancer(
        Name=name,
        Subnets=subnets,
        Type='application'
    )
    return response

lb_name = 'flaskelb'
subnets_list = ['subnet-026b090890b8bd43e', 'subnet-0aa4c19fecaa2a6d1']
response = create_application_load_balancer(lb_name, subnets_list)
print(response['LoadBalancers'][0]['LoadBalancerArn'])

import boto3
from datetime import datetime, timedelta

cloudwatch_client = boto3.client('cloudwatch')

elb_name = 'flaskelb'

end_time = datetime.now()
start_time = end_time - timedelta(days=1)

metric_name = 'RequestCount'
dimensions = [
    {
        'Name': 'LoadBalancerName',
        'Value': elb_name
    },
]

response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/ELB',
                    'MetricName': metric_name,
                    'Dimensions': dimensions
                },
                'Period': 300,
                'Stat': 'Sum',
            },
            'ReturnData': True,
        },
    ],
    StartTime=start_time,
    EndTime=end_time,    
)

print("Metric Data:", response['MetricDataResults'])
for datapoint in response.get('MetricDataResults', []):
    print(f"Time: {datapoint['Timestamps']}, Request Count: {datapoint['Values']}")

