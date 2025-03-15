import boto3
import time

ec2 = boto3.client('ec2')
cw = boto3.client('cloudwatch')

instance_id = 'i-0476ca0139192aabf'

def start_instance():
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting EC2 instance with ID: {instance_id}")

def stop_instance():
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping EC2 instance with ID: {instance_id}")

def get_cpu_utilization():
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = 300  
    dimensions = [{'Name': 'InstanceId', 'Value': instance_id}]

    response = cw.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': namespace,
                        'MetricName': metric_name,
                        'Dimensions': dimensions
                    },
                    'Period': period,
                    'Stat': 'Average'
                },
                'ReturnData': True,
            },
        ],
        StartTime=time.time() - 3600,  
        EndTime=time.time(),
    )

    if 'MetricDataResults' in response:
        datapoints = response['MetricDataResults'][0]['Values']
        if datapoints:
            print(f"Average CPU Utilization: {datapoints[-1]}%")
        else:
            print("No CPU utilization data available.")
    else:
        print("Unable to fetch CPU utilization data.")

def main():
    while True:
        action = input("Enter 'start' to start the instance, 'stop' to stop it, 'monitor' to check CPU utilization, or 'exit' to quit: ")
        if action == 'start':
            start_instance()
        elif action == 'stop':
            stop_instance()
        elif action == 'monitor':
            get_cpu_utilization()
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please enter 'start', 'stop', 'monitor', or 'exit'.")

if __name__ == "__main__":
    main()

