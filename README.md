# EC2 Manager CLI Tool

A Python command-line tool to manage AWS EC2 instances with ease.

## Features

- List all EC2 instances with colored status
- Start/Stop/Reboot instances
- Show detailed instance information
- Estimate monthly costs
- Filter instances by tags
- Batch operations (start/stop multiple instances)

## Prerequisites

- Python 3.6+
- AWS Account with EC2 access
- boto3 library
- colorama library
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/S0R4Y4Y/ec2-manager.git
cd ec2-manager
```

2. Install dependencies:
```bash
pip3 install boto3 colorama
```

3. Configure AWS credentials:
```bash
aws configure
```

## Usage

### List all instances
```bash
python3 ec2_manager.py list
```

### Show cost estimates
```bash
python3 ec2_manager.py costs
```

### Start an instance
```bash
python3 ec2_manager.py start --instance-id i-1234567890abcdef
```

### Stop an instance
```bash
python3 ec2_manager.py stop --instance-id i-1234567890abcdef
```

### Reboot an instance
```bash
python3 ec2_manager.py reboot --instance-id i-1234567890abcdef
```

### Get instance details
```bash
python3 ec2_manager.py info --instance-id i-1234567890abcdef
```

### Filter by tags
```bash
python3 ec2_manager.py filter --tag-key Environment --tag-value Production
```

### Batch operations
```bash
python3 ec2_manager.py start-multiple --instance-ids i-111 i-222 i-333
python3 ec2_manager.py stop-multiple --instance-ids i-111 i-222 i-333
```

## Technologies Used

- **Python 3** - Programming language
- **boto3** - AWS SDK for Python
- **colorama** - Colored terminal output
- **argparse** - Command-line argument parsing

## Project Structure
```
ec2-manager/
├── ec2_manager.py    # Main application
└── README.md         # Documentation
```

## Author

**Soraya** - Computer Science and Engineering Student

## Future Improvements

- [ ] Export instance data to CSV/JSON
- [ ] Create snapshots
- [ ] Monitor instance health
- [ ] Set up CloudWatch alarms
- [ ] Add instance tagging functionality

## License

This project is open source and available for educational purposes.
