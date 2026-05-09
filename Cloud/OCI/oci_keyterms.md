
Region in cloud = A “cloud region” describes the actual, real-life geographic location where your public cloud resources are located. When you choose a cloud provider, you're also choosing a “region,” which is where your data centers physically exist.

Availability Domain(AD) = 
a) one or more fault-tolerant isolated data centers located within region but connected to each other by low latency,high bandwidth n/w.
b) It is one or more data centers located within a region. A region is composed of three availability domains. Services/Resources are either Region-Specific (like VCN) or Availability Domain Specific (like Compute).
	
Fault Domain (FD) = 
a) Grouping of hardware & infrastructure within an AD to provide anti-affinity(logical data center).Each availability domain contains three fault domains.
b) Fault domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain.

Virtual Cloud Network (VCN) = It is a customizable and private network in OCI. Just like a traditional data center network, the VCN provides you with complete control over your network environment.
	
Gateway = It is a hardware device that acts as a "gate" between two networks or a key stopping point for data on its way to or from other networks. It may be a router, firewall, server, or other device that enables traffic to flow in and out of the network. While a gateway protects the nodes within network, it also a node itself. Thanks to gateways, we are able to communicate and send data back and forth. The Internet wouldn't be any use to us without gateways (as well as a lot of other hardware and software).

Dynamic Routing Gateway(DRG) = It is a virtual router that provides a path for private traffic between VCN and destination other than the internet.

FastConnect = Oracle Cloud Infrastructure (OCI) FastConnect is a network connectivity alternative to using the public internet to connect your network to Oracle Cloud Infrastructure and other Oracle Cloud services.

Internet Gateway = IG provides a path for n/w traffic between VCN and internet.

Cloud Secure Access(CSA) = It is designed to provide secure, authorized access to Oracle Cloud Infrastructure (OCI) Tenancies via Linux and Windows Bastions.

virtual private network (VPN) = It is a programming that creates a safe, encrypted connection over a less secure network, such as the public internet. A VPN uses tunneling protocols to encrypt data at the sending end and decrypt it at the receiving end.

Bastion host = It is a special-purpose computer on a network specifically designed and configured to withstand attacks. The computer generally hosts a single application, for example a proxy server, and all other services are removed or limited to reduce the threat to the computer.

Tenancy = The tenancy is an Oracle Cloud Account given to you when you register for Oracle Public Cloud (OCI).

Identity and Access Management (IAM) Policies = In Oracle Cloud Infrastructure Identity and Access Management (IAM), a tenancy administrator can create policies to grant permissions to groups on resources in compartments in a tenancy. Oracle Data Safe administrators require a policy, but regular users do not

Tenancy in OCI = When user sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for your company, which is a secure and isolated partition where you can create, organize, and administer your cloud resources. To use any of the API operations, you must be authorized in an IAM policy.

Compartment in OCI = A compartment is a logical container, to organize and control access to the Oracle Cloud Infrastructure (OCI) Resources (Compute, Storage, Network, Load Balancer etc) created within that compartment and you impose some policies to that compartment, which restricts who can use the resources created within than.


Autoscaling = 
a) Autoscaling lets you automatically adjust the number of Compute instances in an instance pool based on performance metrics such as CPU utilization. This helps you provide consistent performance for your end users during periods of high demand, and helps you reduce your costs during periods of low demand.
b) It is a method used in cloud computing, whereby the amount of computational resources in a server farm, typically measured in terms of the number of active servers, which vary automatically based on the load on the farm.

Vertical Scaling = 
a) Vertical scaling refers to adding more resources (CPU/RAM/DISK) to your server (database or application server is still remains one) as on demand. ... Some of the reasons to scale vertically includes increasing IOPS (Input / Ouput Operations), amplifying CPU/RAM capacity, as well as disk capacity.
b) Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine

Horizontal Sacling = 
a) Horizontal Scaling is the act of changing the number of nodes in a computing system without changing the size of any individual node.
b) Horizontal scaling means that you scale by adding more machines into your pool of resources 

Socket = IP (32) + Port(16) = 48

Containerized application
OCI scheduled / periodic backups
Archive Storage Tier (Cold)

IAM = Identity and Access Management

Hypervisor = Oracle Virtual Box

LB = Load Balancer

Demilitarized zone (DMZ) = 
a) In computer networks, a DMZ (demilitarized zone), also sometimes known as a perimeter network or a screened subnetwork, is a physical or logical subnet that separates an internal local area network (LAN) from other untrusted networks -- usually the public internet.
b) It consists of the portions of a corporate network that are between the corporate intranet and the Internet. The DMZ typically hosts public services, such as Web, mail, and domain servers. Application delivery controllers usually sit in the DMZ, providing application access to the public servers. The DMZ can be a simple one segment LAN or it can be broken down into multiple regions.
c) The purpose of a DMZ is to add an additional layer of security to an organization's local area network (LAN): an external network node can access only what is exposed in the DMZ, while the rest of the organization's network is firewalled.

DMZ Subnet = for load balancer

Public Subnet = for web server

Private Subnet = for internal host such as DB


==============================================================

Tenancy in OCI = When user sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for your company, which is a secure and isolated partition where you can create, organize, and administer your cloud resources. To use any of the API operations, you must be authorized in an IAM policy.

===================================================================

On-Disk Databases

- All data stored on disk, disk I/O needed to move data into main memory when needed.
- Data is always persisted to disk.
- Traditional data structures like B-Trees designed to store tables and indices efficiently on disk.
- Virtually unlimited database size.
- Support very broad set of workloads, i.e. OLTP, data warehousing, mixed workloads, etc.


In-Memory Databases

- All data stored in main memory, no need to perform disk I/O to query or update data.
- Data is persistent or volatile depending on the in-memory database product.
- Specialized data structures and index structures assume data is always in main memory.


In-memory processing works by eliminating all slow data accesses and relying exclusively on data stored in RAM. Overall processing performance is not slowed by the latency commonly seen when accessing hard disk drives or SSDs. Software running on one or more computers manages the processing work as well as the data in memory, and in the case of multiple computers, the software divides the processing into smaller tasks which are distributed out to each computer to run in parallel. In-memory processing is often done in the technology known as in-memory data grids (IMDG).

================================================================================

API 
- Application Programming Interface, abbreviated as API, enables connection between computers or computer programs. It is a Software Interface that offers services to other software to enhance the required functionalities.

REST API
- Representational State Transfer (REST) is an architectural style to provide standards between systems on the web. REST is neither a protocol, nor library, nor a tool, so communication between systems becomes easy. REST architecture makes the implementation of Client and Server independent without affecting the operation of the other.

=======================================================================================
