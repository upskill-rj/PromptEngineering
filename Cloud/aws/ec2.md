# What will you learn 

## Introduction to EC2:

What is EC2, and why is it important?

```
- Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud.
- Access reliable, scalable infrastructure on demand. Scale capacity within minutes with SLA commitment of 99.99% availability.
- Provide secure compute for your applications. Security is built into the foundation of Amazon EC2 with the AWS Nitro System.
- Optimize performance and cost with flexible options like AWS Graviton-based instances, Amazon EC2 Spot instances, and AWS Savings Plans.
```

EC2 usecases

```
Deliver secure, reliable, high-performance, and cost-effective compute infrastructure to meet demanding business needs.
Access the on-demand infrastructure and capacity you need to run HPC applications faster and cost-effectively.
Access environments in minutes, dynamically scale capacity as needed, and benefit from AWS’s pay-as-you-go pricing.
Deliver the broadest choice of compute, networking (up to 400 Gbps), and storage services purpose-built to optimize price performance for ML projects
```

EC2 Instance Types

Recommended to follow [this](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) page for very detailed and updated information.

General purpose

```
General Purpose instances are designed to deliver a balance of compute, memory, and network resources. They are suitable for a wide range of applications, including web servers,
small databases, development and test environments, and more.
```

Compute optimized

```
Compute Optimized instances provide a higher ratio of compute power to memory. They excel in workloads that require high-performance processing such as batch processing, 
scientific modeling, gaming servers, and high-performance web servers.
```

Memory optimized

```
Memory Optimized instances are designed to handle memory-intensive workloads. They are suitable for applications that require large amounts of memory, such as in-memory databases,
real-time big data analytics, and high-performance computing.
```

Storage optimized

```
Storage Optimized instances are optimized for applications that require high, sequential read and write access to large datasets. 
They are ideal for tasks like data warehousing, log processing, and distributed file systems.
```

Accelerated computing

```
Accelerated Computing Instances typically come with one or more types of accelerators, such as Graphics Processing Units (GPUs),
Field Programmable Gate Arrays (FPGAs), or custom Application Specific Integrated Circuits (ASICs). 
These accelerators offload computationally intensive tasks from the main CPU, enabling faster and more efficient processing for specific workloads.
```

![image](https://github.com/iam-veeramalla/aws-devops-zero-to-hero/assets/43399466/fc8e083c-dba5-41a6-94b9-14ebef0255c1)

Instance families

```
    C – Compute

    D – Dense storage

    F – FPGA

    G – GPU

    Hpc – High performance computing

    I – I/O

    Inf – AWS Inferentia

    M – Most scenarios

    P – GPU

    R – Random access memory

    T – Turbo

    Trn – AWS Tranium

    U – Ultra-high memory

    VT – Video transcoding

    X – Extra-large memory
```

Additional capabilities

```
    a – AMD processors

    g – AWS Graviton processors

    i – Intel processors

    d – Instance store volumes

    n – Network and EBS optimized

    e – Extra storage or memory

    z – High performance
```

## EC2 Instance Basics:

Understanding the concept of virtual servers and instances.
Key components of an EC2 instance: AMI (Amazon Machine Image), instance types, and instance states.
Differentiating between On-Demand, Reserved, and Spot instances.

## Launching an EC2 Instance:

- Step-by-step guide on launching an EC2 instance using the AWS Management Console.
- Configuring instance details, such as instance type, network settings, and storage options.
- Understanding security groups and key pairs for securing instances.

## Managing EC2 Instances:

- Starting, stopping, and terminating instances.
- Monitoring instance performance and utilization.
- Basic troubleshooting and accessing instances using SSH (Secure Shell).

==========


### 1. What is Amazon EC2?
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It allows users to create, configure, and manage virtual servers (known as instances) in the AWS cloud.

### 2. How does Amazon EC2 work?
Amazon EC2 enables users to launch instances based on pre-configured Amazon Machine Images (AMIs). These instances run within virtual private clouds (VPCs) and can be configured with various resources like CPU, memory, storage, and networking.

### 3. What are the different instance types in EC2?
Amazon EC2 offers a wide range of instance types optimized for different use cases, such as general-purpose, memory-optimized, compute-optimized, and GPU instances.

### 4. Explain the differences between on-demand, reserved, and spot instances.
- On-Demand Instances: Pay-as-you-go pricing with no upfront commitment.
- Reserved Instances: Provides capacity reservation at a lower cost in exchange for a commitment.
- Spot Instances: Allows users to bid on unused EC2 capacity, potentially leading to significantly lower costs.

### 5. How can you improve the availability of EC2 instances?
To improve availability, you can place instances in multiple Availability Zones (AZs) within a region. This helps ensure redundancy and fault tolerance.

### 6. What is an Amazon Machine Image (AMI)?
An Amazon Machine Image (AMI) is a pre-configured template that contains the information required to launch an EC2 instance. AMIs can include an operating system, applications, data, and configuration settings.

### 7. How can you secure your EC2 instances?
You can enhance the security of EC2 instances by using security groups, Network ACLs, key pairs, and configuring firewalls. Additionally, implementing multi-factor authentication (MFA) is recommended for account access.

### 8. Explain the difference between public IP and Elastic IP in EC2.
A public IP is assigned to an instance at launch, but it can change if the instance is stopped and started. An Elastic IP is a static IP address that can be associated with an instance, providing a consistent public IP even after stopping and starting the instance.

### 9. How can you scale your application using EC2?
You can scale your application horizontally by adding more instances. Amazon EC2 Auto Scaling helps you automatically adjust the number of instances based on demand.

### 10. What is Amazon EBS?
Amazon Elastic Block Store (EBS) provides persistent block storage volumes for EC2 instances. EBS volumes can be attached to instances and used as data storage.

### 11. How can you encrypt data on EBS volumes?
You can encrypt EBS volumes using Amazon EBS encryption. You can choose to create encrypted volumes during instance launch or encrypt existing unencrypted volumes.

### 12. How can you back up your EC2 instances?
You can create snapshots of EBS volumes, which serve as backups. These snapshots can be used to create new EBS volumes or restore existing ones.

### 13. What is the difference between instance store and EBS-backed instances?
Instance store instances use ephemeral storage that is directly attached to the instance, providing high I/O performance. EBS-backed instances use EBS volumes for storage, offering persistent data storage.

### 14. What are instance metadata and user data in EC2?
Instance metadata provides information about an instance, such as its IP address, instance type, and IAM role. User data is information that you can pass to an instance during launch to customize its behavior.

### 15. How can you launch instances in a Virtual Private Cloud (VPC)?
When launching instances, you can choose a specific VPC and subnet. This ensures that the instances are launched within the defined network environment.

### 16. What is the purpose of an EC2 security group?
An EC2 security group acts as a virtual firewall for instances to control inbound and outbound traffic. You can specify rules to allow or deny traffic based on IP addresses and ports.

### 17. How can you automate the deployment of EC2 instances?
You can use AWS CloudFormation to create and manage a collection of related AWS resources, including EC2 instances. This allows you to define the infrastructure as code.

### 18. How can you achieve high availability for an application using EC2?
You can use features like Amazon EC2 Auto Scaling and Elastic Load Balancing to distribute incoming traffic and automatically adjust the number of instances to handle changes in demand.

### 19. What is Amazon Machine Learning (Amazon ML)?
Amazon ML is a service that enables you to build predictive models using machine learning technology. It's used to perform predictions on data and make informed decisions.

===========================


### 1. What is AWS Lambda?
AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. It automatically scales and manages the infrastructure required to run your code in response to events.

### 2. How does AWS Lambda work?
You can upload your code to Lambda and define event sources that trigger the execution of your code. Lambda automatically manages the execution environment, scales it as needed, and provides monitoring and logging.

### 3. What are the key benefits of using AWS Lambda?
The benefits of AWS Lambda include automatic scaling, reduced operational overhead, cost efficiency (as you pay only for the compute time used), and the ability to build event-driven architectures.

### 4. What types of events can trigger AWS Lambda functions?
AWS Lambda functions can be triggered by various event sources, such as changes in Amazon S3 objects, updates to Amazon DynamoDB tables, HTTP requests through Amazon API Gateway, and more.

### 5. How is concurrency managed in AWS Lambda?
Lambda automatically handles concurrency by scaling out instances of your function in response to incoming requests. You can set a concurrency limit to control how many concurrent executions are allowed.

### 6. What is the maximum execution duration for a single AWS Lambda invocation?
The maximum execution duration for a single Lambda invocation is 15 minutes.

### 7. How do you pass data to and from AWS Lambda functions?
You can pass data to Lambda functions through event objects, which contain information about the triggering event. You can also return data by using the return statement or creating a response object.

### 8. Can AWS Lambda functions communicate with external resources?
Yes, Lambda functions can communicate with external resources such as databases, APIs, and other AWS services by using appropriate SDKs and APIs provided by AWS.

### 9. What are AWS Lambda layers?
AWS Lambda layers are a way to manage and share code that is common across multiple functions. Layers can include libraries, custom runtimes, and other function dependencies.

### 10. How can you handle errors in AWS Lambda functions?
You can handle errors by using try-catch blocks in your code. Lambda also provides CloudWatch Logs for monitoring, and you can set up error handling and retries for asynchronous invocations.

### 11. Can AWS Lambda functions access the internet?
Yes, Lambda functions can access the internet through the Virtual Private Cloud (VPC) or through public endpoints if your function is not configured within a VPC.

### 12. What are the execution environments available for AWS Lambda functions?
Lambda supports several runtimes, including Node.js, Python, Java, Go, Ruby, .NET Core, and custom runtimes using the Runtime API.

### 13. How can you configure environment variables for AWS Lambda functions?
You can set environment variables for Lambda functions when creating or updating the function. These variables can be accessed within your code.

### 14. What is the difference between synchronous and asynchronous invocation of Lambda functions?
Synchronous invocations wait for the function to complete and return a response, while asynchronous invocations return immediately, and the response is sent to a specified destination.

### 15. What is the AWS Lambda Event Source Mapping?
Event Source Mapping allows you to connect event sources like Amazon DynamoDB streams or Amazon Kinesis streams to Lambda functions. This enables the function to process events as they occur.

### 16. How can you manage the permissions and execution roles for AWS Lambda functions?
You can use AWS Identity and Access Management (IAM) roles to grant permissions to your Lambda functions. Execution roles define what AWS resources the function can access.

### 17. What is AWS Step Functions?
AWS Step Functions is a serverless orchestration service that lets you coordinate multiple AWS services into serverless workflows using visual workflows called state machines.

### 18. How can you automate the deployment of AWS Lambda functions?
You can use AWS Serverless Application Model (SAM) templates, AWS CloudFormation, or CI/CD tools like AWS CodePipeline to automate the deployment of Lambda functions.

### 19. Can AWS Lambda functions connect to on-premises resources?
Yes, Lambda functions can connect to on-premises resources by placing the function inside a VPC and using a VPN or Direct Connect connection to establish connectivity.

### 20. What is the Cold Start issue in AWS Lambda?
The Cold Start issue occurs when a Lambda function is invoked for the first time or after it has been idle for a while. The function needs to be initialized, causing a slight delay in response time.

=================================

### 1. What is AWS Elastic Beanstalk?
AWS Elastic Beanstalk is a platform-as-a-service (PaaS) offering that simplifies application deployment and management. It handles infrastructure provisioning, deployment, monitoring, and scaling, allowing developers to focus on writing code.

### 2. How does Elastic Beanstalk work?
Elastic Beanstalk abstracts the infrastructure layer, allowing you to upload your code (web application or microservices) and configuration. It then automatically deploys, manages, and scales your application based on the platform, language, and environment settings you choose.

### 3. What languages and platforms does Elastic Beanstalk support?
Elastic Beanstalk supports multiple programming languages and platforms, including Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

### 4. What is an Elastic Beanstalk environment?
An Elastic Beanstalk environment is a specific instance of your application that includes the runtime, resources, and configuration settings. You can have multiple environments (e.g., development, testing, production) for the same application.

### 5. How does Elastic Beanstalk handle updates and deployments?
Elastic Beanstalk supports both All at Once and Rolling deployments. All at Once deploys updates to all instances simultaneously, while Rolling deploys updates in batches to reduce downtime.

### 6. Can you customize the infrastructure in Elastic Beanstalk?
Yes, Elastic Beanstalk allows you to customize the environment's resources, configuration, and scaling settings through environment configuration files or the AWS Management Console.

### 7. How can you monitor the health of an Elastic Beanstalk environment?
Elastic Beanstalk provides health monitoring through CloudWatch. You can set up alarms based on metrics like CPU utilization, latency, and request count.

### 8. What is the Elastic Beanstalk Command Line Interface (EB CLI)?
The EB CLI is a command-line tool that provides an interface for interacting with Elastic Beanstalk. It enables developers to manage applications and environments using commands.

### 9. How does Elastic Beanstalk handle automatic scaling?
Elastic Beanstalk can automatically scale your application based on the configured scaling triggers, such as CPU utilization, network traffic, or other custom metrics.

### 10. Explain the difference between Single Instance and Load Balanced environments in Elastic Beanstalk.
In a Single Instance environment, your application runs on a single EC2 instance. In a Load Balanced environment, your application runs on multiple instances behind a load balancer, improving availability and scalability.

### 11. How does Elastic Beanstalk support rolling back deployments?
Elastic Beanstalk supports rolling back to a previous version if an update results in errors or issues. You can initiate a rollback through the AWS Management Console or the EB CLI.

### 12. Can Elastic Beanstalk deploy applications to multiple availability zones?
Yes, Elastic Beanstalk can automatically deploy your application to multiple availability zones within a region to enhance high availability.

### 13. How can you handle environment-specific configurations in Elastic Beanstalk?
You can use configuration files, environment variables, or Parameter Store to manage environment-specific configurations, ensuring your application behaves consistently across environments.

### 14. Describe how you would configure environment variables in Elastic Beanstalk.
Environment variables can be configured using the AWS Management Console, the EB CLI, or Elastic Beanstalk configuration files. They provide a way to pass dynamic values to your application.

### 15. Can Elastic Beanstalk deploy applications stored in containers?
Yes, Elastic Beanstalk supports deploying Docker containers. You can specify a Docker image repository and Elastic Beanstalk will handle deployment and management of the containerized application.

### 16. How can you automate deployments to Elastic Beanstalk?
You can use the AWS CodePipeline service to automate the deployment process to Elastic Beanstalk. This helps create a continuous integration and continuous delivery (CI/CD) pipeline.

### 17. What is the difference between an environment URL and a CNAME in Elastic Beanstalk?
An environment URL is a unique URL automatically generated for each Elastic Beanstalk environment. A CNAME (Canonical Name) is an alias that you can configure to map a custom domain to your Elastic Beanstalk environment.

### 18. Can Elastic Beanstalk be used for serverless applications?
While Elastic Beanstalk handles infrastructure provisioning, it is not a serverless service like AWS Lambda. It's designed to manage and scale applications on virtual machines.

### 19. What are worker environments in Elastic Beanstalk?
Worker environments in Elastic Beanstalk are used for background tasks and processing. They handle tasks asynchronously, separate from the main application environment.

### 20. How can you back up and restore an Elastic Beanstalk environment?
Elastic Beanstalk does not provide built-in backup and restore capabilities. However, you can use AWS services like Amazon RDS for database backups and CloudFormation for environment configuration versioning.

### 21. What is Amazon EC2 Instance Connect?
Amazon EC2 Instance Connect provides a simple and secure way to connect to your instances using Secure Shell (SSH). It eliminates the need to use key pairs and allows you to connect using your AWS Management Console credentials.


