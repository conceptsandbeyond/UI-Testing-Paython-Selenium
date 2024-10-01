# Deploying Selenium Testing Code on AWS

This guide provides step-by-step instructions to deploy your Selenium testing code on AWS EC2.

## Prerequisites

- An AWS account
- Basic knowledge of AWS services
- SSH client (e.g., Terminal on macOS/Linux or PuTTY on Windows)
- Your Selenium testing code

## Step 1: Set Up an AWS EC2 Instance

1. **Log in to AWS Management Console**:
    - Go to the [AWS Management Console](https://aws.amazon.com/console/) and log in.

2. **Launch a New EC2 Instance**:
    - Go to the EC2 Dashboard.
    - Click on "Launch Instance."
    - Choose an Amazon Machine Image (AMI) (Ubuntu or Amazon Linux is recommended).
    - Choose an instance type (e.g., `t2.micro` for free tier).
    - Configure instance details, add storage, and set tags as needed.
    - Configure the security group to allow inbound traffic on necessary ports (22 for SSH).
    - Launch the instance and download the key pair for SSH access.

## Step 2: Connect to Your EC2 Instance

1. **SSH into Your EC2 Instance**:
   Open a terminal or command prompt and connect to your instance using the key pair:
   ```bash
   ssh -i path_to_your_key_pair.pem ec2-user@your_instance_public_ip
   ```

## Step 3: Install Dependencies
1. **Update Package Repository**:
   
   ```bash
   sudo apt update
   ```   
2. **Install Python and Pip**:

   ```bash
      sudo apt install python3 python3-pip
   ```
3. **Install Selenium**:

   ```bash
   pip3 install selenium
   ```
4. **Install Chrome and ChromeDriver**: Install Google Chrome and the ChromeDriver that matches your Chrome version:
   ```bash
   # Install dependencies
   sudo apt install -y wget unzip
   
   # Download and install Google Chrome
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   sudo apt --fix-broken install
   
   # Download ChromeDriver
   CHROME_VERSION=$(google-chrome --version | grep -o '[0-9]*\.[0-9]*\.[0-9]*')
   wget https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip
   unzip chromedriver_linux64.zip
   sudo mv chromedriver /usr/local/bin/
   sudo chmod +x /usr/local/bin/chromedriver
   ```
## Step 4: Transfer Your Test Code
1. **Upload Your Code**: Use scp to securely copy your test code to your EC2 instance:
   ```bash
   scp -i path_to_your_key_pair.pem path_to_your_ui_test.py ec2-user@your_instance_public_ip:/home/ec2-user/
   ```
### Step 5: Run Your Selenium Test
1. **Run Your Test**: After transferring your code, run it on your EC2 instance:

   ```bash
    python3 ui_test.py
   ```
