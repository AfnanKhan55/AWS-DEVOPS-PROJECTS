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

