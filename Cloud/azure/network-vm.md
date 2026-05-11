# Azure Networking Advanced

## Azure App Gateway & WAF

Azure Application Gateway is a web traffic load balancer that enables you to manage and route traffic to your web applications. Web Application Firewall (WAF) provides protection against web vulnerabilities. Key features include:

- **Load Balancing**: Distributes incoming traffic across multiple servers to ensure no single server is overwhelmed.

- **SSL Termination**: Offloads SSL processing, improving the efficiency of web servers.

- **Web Application Firewall (WAF)**: Protects web applications from common web vulnerabilities and exploits.

## Azure Load Balancer

Azure Load Balancer distributes incoming network traffic across multiple servers to ensure no single server is overwhelmed. Key features include:

- **Load Balancing Algorithms**: Supports different algorithms for distributing traffic, such as round-robin and least connections.

- **Availability Sets**: Works seamlessly with availability sets to ensure high availability.

- **Inbound and Outbound Traffic**: Balances both inbound and outbound traffic.

## Azure DNS

Azure DNS is a scalable and secure domain hosting service. It provides name resolution using the Microsoft Azure infrastructure. Key features include:

- **Domain Hosting**: Hosts domain names and provides name resolution within Azure.

- **Integration with Azure Services**: Easily integrates with other Azure services like App Service and Traffic Manager.

- **Global Availability**: Provides low-latency responses globally.

## Azure Firewall

Azure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. Key features include:

- **Stateful Firewall**: Allows or denies traffic based on rules and supports stateful inspection.

- **Application FQDN Filtering**: Filters traffic based on fully qualified domain names.

- **Threat Intelligence Integration**: Integrates with threat intelligence feeds for enhanced security.

## Virtual Network Peering and VNet Gateway

### Virtual Network Peering

Virtual Network Peering allows connecting Azure Virtual Networks directly, enabling resources in one VNet to communicate with resources in another. Key features include:

- **Global VNet Peering**: Peering can be established across regions.

- **Transitive Routing**: Traffic between peered VNets flows directly, improving performance.

### VNet Gateway

VNet Gateway enables secure communication between on-premises networks and Azure Virtual Networks. Key features include:

- **Site-to-Site VPN**: Connects on-premises networks to Azure over an encrypted VPN tunnel.

- **Point-to-Site VPN**: Enables secure remote access to Azure resources.

## VPN Gateway

Azure VPN Gateway provides secure, site-to-site connectivity between your on-premises network and Azure. Key features include:

- **IPsec/IKE VPN Protocols**: Ensures secure communication over the Internet.

- **High Availability**: Supports active-active and active-passive configurations for high availability.

- **BGP Support**: Allows dynamic routing between your on-premises network and Azure.


=======================

# Azure Networking

## Virtual Network

A Virtual Network (VNet) in Azure is a logically isolated network that securely connects Azure resources and extends on-premises networks. Key features include:

- **Isolation**: VNets provide isolation at the network level for segmenting resources and controlling traffic.

- **Subnetting**: Divide a VNet into subnets for resource organization and traffic control.

- **Address Space**: VNets have an address space defined using CIDR notation, determining the IP address range.

## Subnets, CIDR

### Subnets

Subnets are subdivisions of a Virtual Network, allowing for better organization and traffic management.

### CIDR (Classless Inter-Domain Routing)

CIDR notation represents IP addresses and their routing prefix, specifying the range of IP addresses for a network.

## Routes and Route Tables

### Routes

Routes dictate how network traffic is directed, specifying the destination and next hop.

### Route Tables

Route Tables are collections of routes associated with subnets, enabling custom routing rules.

## Network Security Groups (NSGs)

NSGs are fundamental for Azure's network security, allowing filtering of inbound and outbound traffic. Key aspects include:

- **Rules**: NSGs define allowed or denied traffic based on source, destination, port, and protocol.

- **Default Rules**: NSGs have default rules for controlling traffic within the Virtual Network and between subnets.

- **Association**: NSGs can be associated with subnets or individual network interfaces.

## Application Security Groups (ASGs)

ASGs group Azure virtual machines based on application requirements, simplifying network security:

- **Simplification**: ASGs allow defining rules based on application roles instead of individual IP addresses.

- **Dynamic Membership**: ASGs support dynamic membership based on tags or other attributes.

- **Rule Association**: Security rules can be associated with ASGs for intuitive and scalable network security management.

====================

# Virtualization: An In-Depth Explanation

## Background

In traditional computing, a single physical server runs a single operating system, and applications are installed directly on that OS. This approach has limitations, such as underutilization of hardware resources, difficulty in managing multiple servers, and lack of flexibility in scaling.

**Virtualization** addresses these challenges by introducing a layer of abstraction between the hardware and the operating system. It enables the creation of multiple virtual instances, each running its own operating system and applications, on a single physical server. This technology has become fundamental in modern data centers and cloud computing environments.

## Components of Virtualization

1. **Hypervisor (Virtual Machine Monitor):**
   - The hypervisor is a crucial component of virtualization. It sits between the hardware and the operating systems, managing and allocating resources to virtual machines (VMs).
   - There are two types of hypervisors: Type 1 (bare-metal) runs directly on the hardware, while Type 2 (hosted) runs on top of an existing operating system.

2. **Virtual Machines (VMs):**
   - VMs are the instances created by the hypervisor. Each VM operates as an independent computer with its own virtualized hardware, including CPU, memory, storage, and network interfaces.
   - Multiple VMs can run on a single physical server, allowing for efficient resource utilization.

## Key Concepts in Virtualization

1. **Server Virtualization:**
   - In server virtualization, a physical server is divided into multiple VMs, each running its own OS. This allows for better utilization of hardware resources and easier management of servers.

2. **Resource Pooling:**
   - Virtualization enables the pooling of physical resources, such as CPU, memory, and storage. These resources can be dynamically allocated to VMs based on demand.

3. **Isolation:**
   - VMs operate independently of each other. This isolation ensures that issues in one VM do not affect others, providing a more secure and stable environment.

4. **Snapshotting and Cloning:**
   - Virtualization allows the creation of snapshots, which capture the state of a VM at a specific point in time. This facilitates easy backup and recovery. Cloning enables the rapid duplication of VMs for scalability.

## Benefits of Virtualization

1. **Server Consolidation:**
   - Multiple VMs can run on a single physical server, reducing the need for a large number of physical machines. This leads to cost savings and energy efficiency.

2. **Flexibility and Scalability:**
   - Virtualization allows for the easy creation, modification, and scaling of VMs. This flexibility is essential in dynamic computing environments.

3. **Disaster Recovery:**
   - Virtualization simplifies disaster recovery by enabling the quick restoration of VMs from snapshots or backups.

4. **Resource Optimization:**
   - Resources can be allocated and deallocated dynamically based on workload, optimizing resource utilization.

5. **Testing and Development:**
   - Virtualization provides a sandbox for testing and development. VMs can be easily created, modified, and discarded without affecting the production environment.
  
=====================

# Types of Virtual Machines on Azure

Azure provides a variety of virtual machine (VM) offerings to cater to different workload requirements. Each VM type is designed with specific hardware configurations to meet diverse performance and scalability needs.

## General Purpose VMs

**Example: Standard_D2s_v3**

- **Description:** General-purpose VMs are well-balanced machines suitable for a variety of workloads. They offer a good balance of CPU-to-memory ratio and are suitable for development, testing, and small to medium-sized databases.

- **Use Case:** Hosting websites, lightweight applications, or development and testing environments.

## Compute Optimized VMs

**Example: Standard_F2s_v2**

- **Description:** Compute optimized VMs are designed for compute-intensive workloads that require high CPU power. They provide a high CPU-to-memory ratio, making them suitable for data analytics and computational tasks.

- **Use Case:** Batch processing, gaming applications, and other CPU-intensive workloads.

## Memory Optimized VMs

**Example: Standard_E16s_v3**

- **Description:** Memory optimized VMs are tailored for memory-intensive applications. They provide a high memory-to-CPU ratio, making them suitable for databases, in-memory caching, and analytics.

- **Use Case:** Running large databases, in-memory caching, and analytics applications.

## Storage Optimized VMs

**Example: Standard_L8s_v2**

- **Description:** Storage optimized VMs are designed for workloads that require high storage throughput and I/O performance. They provide high local disk throughput, making them suitable for big data and large databases.

- **Use Case:** Big data applications, data warehousing, and large-scale databases.

## GPU VMs

**Example: Standard_NC6s_v3**

- **Description:** GPU (Graphics Processing Unit) VMs are equipped with powerful graphics processors, suitable for graphics-intensive applications and parallel processing tasks.

- **Use Case:** Machine learning, graphics rendering, and simulations that require GPU acceleration.

## High-Performance Compute VMs

**Example: Standard_H16r**

- **Description:** High-Performance Compute VMs are designed for demanding, parallel processing and high-performance computing (HPC) applications.

- **Use Case:** Simulations, modeling, and scenarios that require massive parallel processing.

## Burstable VMs

**Example: B1s**

- **Description:** Burstable VMs provide a baseline level of CPU performance with the ability to burst above the baseline for a certain period. They are cost-effective for workloads with varying CPU usage.

- **Use Case:** Development and testing environments, small websites, and applications with variable workloads.
