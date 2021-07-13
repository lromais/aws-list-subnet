import boto3


def lambda_handler(event, context):
    if not bool(event):
        raise Exception('No event defined!')
    ec2 = boto3.resource('ec2')
    subnets = ec2.subnets.all()
    for subnet in list(subnets):
        free_ips = subnet.available_ip_address_count
        n = int(subnet.cidr_block.split('/')[1])
        cidr_ips = 2**(32-n)
        used_ips = cidr_ips - free_ips
        calc= free_ips * 100
        print('VPC={:s}, Subnet={:s}: VPC-CIDR={:d}, Ips_reservados_AWS=5, Ips_usados={:d}, ips_Livres={:d}, total_percent_livre={:0f}%'.\
            format(subnet.vpc_id, subnet.id, cidr_ips, used_ips - 5, free_ips, calc / cidr_ips))
