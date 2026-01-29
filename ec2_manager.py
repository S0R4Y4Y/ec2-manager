#!/usr/bin/env python3
import boto3
import argparse
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='ap-southeast-2')

def list_instances():
    """List all EC2 instances with their status"""
    print("\n=== EC2 Instances ===\n")

    response = ec2.describe_instances()

    if not response['Reservations']:
        print("No instances found!")
        return

    # Print header
    print(f"{'Instance_ID':<20} {'Name':<25} {'Type':<15} {'State':<15}")
    print("-" * 75)

    # Loop through instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']

            # Get name from tags
            name = 'N/A'
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']

            if state == 'running':
                state = Fore.GREEN + state + Style.RESET_ALL
            elif state == 'stopped':
                state = Fore.RED + state + Style.RESET_ALL
            elif state == 'pending':
                state = Fore.YELLOW + state + Style.RESET_ALL

            print(f"{instance_id:<20} {name:<25} {instance_type:<15} {state:<15}")

    print()

def start_instance(instance_id):
    """Start an EC2 instance"""
    print(f"\nStarting instance {instance_id}...")

    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"✓ Instance {instance_id} is starting!")
    except Exception as e:
        print(f"✗ Error: {e}")

def stop_instance(instance_id):
    """Stop an EC2 instance"""
    print(f"\nStopping instance {instance_id}...")

    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"✓ Instance {instance_id} is stopping!")
    except Exception as e:
        print(f"✗ Error: {e}")

def get_instance_info(instance_id):
    """Get detailed info about an instance"""
    print(f"\n=== Instance Details: {instance_id} ===\n")

    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        print(f"Instance ID:     {instance['InstanceId']}")
        print(f"Instance Type:   {instance['InstanceType']}")
        print(f"State:           {instance['State']['Name']}")
        print(f"Public IP:       {instance.get('PublicIpAddress', 'N/A')}")
        print(f"Private IP:      {instance.get('PrivateIpAddress', 'N/A')}")
        print(f"Launch Time:     {instance['LaunchTime']}")

        # Show tags
        if 'Tags' in instance:
            print("\nTags:")
            for tag in instance['Tags']:
                print(f"  {tag['Key']}: {tag['Value']}")

        print()

    except Exception as e:
        print(f"✗ Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='EC2 Instance Manager')
    parser.add_argument('action', choices=['list', 'start', 'stop', 'info'],
                       help='Action to perform')
    parser.add_argument('--instance-id', help='EC2 Instance ID')

    args = parser.parse_args()

    if args.action == 'list':
        list_instances()

    elif args.action == 'start':
        if not args.instance_id:
            print("Error: --instance-id required for start action")
            return
        start_instance(args.instance_id)

    elif args.action == 'stop':
        if not args.instance_id:
            print("Error: --instance-id required for stop action")
            return
        stop_instance(args.instance_id)

    elif args.action == 'info':
        if not args.instance_id:
            print("Error: --instance-id required for info action")
            return
        get_instance_info(args.instance_id)

if __name__ == '__main__':
    main()
