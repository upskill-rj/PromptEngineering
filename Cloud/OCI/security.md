
# 3PLTA = Third Party License Tracking Application

* 3rd Party liceming Information of commercials and open-source componenets that are used to develop product and services
* Include BA (business approval) workflows
* Support release traching activities.

# Basic Terminology

* Licensed Technology (LT) - For everyone
	* Licemed API's (LAs)
	* Licenced Dataset (LDs)
* Business Approval (BA) - For each Team


#3PLTA relate to the Product Life Suite

* 3PLTA's a standalone app that exchange date with various PLS apps
* Product & Release Adimin (PRA)
* Compliance Dashboard / Security Compliame Systems (SCMS)
* Report Management System (RMS)
* One LT per version of a licensed technlogy
* Don't use an older version of an LT to avoid creating a new one
* BA to pre approval procur
* All Pre-Approved BA's (as well as security reviews BAs ad Legal Review BA's) are subject to random audit.
* D&E Legal reprentative - cosult



# Gather Required Information for LT & BA

1) Identify the 3rd party content.
2) confirm that the business approval is necessary.
3) Prepare your information.
	a) Name and exact version of components and dependencies.
	b) Results of seaches for known vulnerabilities
	c) URL for the main home page for the S/W.
	d) URL for the download location.
	e) If competitive or not reasonably current, justification and competitive approvals.

4) Infomation for how it will be uned in your product.

# Approval Chain

1) Obtain concept Approvals
2) Go through legal review
3) Obtain final Approval.

# Permissive Licenser ALWAYS Best.

# CDDL Licenses 
* CDDL is almost always tied to Oracle (or Sun) own and maintained technology.


# Fouth -Party Dependencies.

- A 3rd party dependency is technlogy you used that is not owned by company - These form the basis of your requests in 3PLTA
- Fourth-party dependencers are all dependencies of a 3rd party dependency - these must be included in the 3PLTA request for the 3rd prty  itself.
- Each 3rd party dependency incorporates copyrighted materials from its 4th-party dependencies.
- Company must therefore comply with the licencing obligations of 4th-party dependencies, just as we do for 3rd Party dependencies.
- 4th party dependencies are also vital for security assessment.
- 95% of all reported vulnerabilities in commercial s/w originates in these transitive dependencies of open source software.
- No security review of 3rd party material can be considered completes without reviewing its dependencies.
- 4th party dependencies do include
	- compiles and runtime dependencies
	- the full, transitive list of dependencies.
	
	
# How to Identify 4th party dependencies.

- Using Standard build tools

1) For Java - Maven or Gradle
2) Por Python- pipgrip or pipdeptree
3) For Node- npm
4) for Scala- sbt
5) for .NET/C#- NuGet Package Manage in Visual Studio or Switch

- 4th party dependency detail need to be recorded in 3PLTA

# Licensed Technology (Public Licenses & Copyright Notice Fields)
- Dependney Name
- Licenses and copyright notices

# Business Approval (Technology usage Not Field)
- Dependency names
- Dependency versions

# Populating the LT Public Licence field.

- Company has additional tools to assist in identifying 4th party depudencies.

1) Open Source Compliance Series (OSCS)
- Supports Java, Python, Node and Go (uning Attribute helper) 
- Fetches licenses and notices, and highlights known scurity vulnerabilities

2) Attribution Helper

- Supports Go, Node (does not produce accurate results for java)
- Fetches licences and notices. (Third Party Licenen.txt)
- Required by corporate Architects for Go projects.

# Common Cases

- No Dependencies-Means No required runtime or compile time dependencies
- Nested Model.

- Less Common cases
	- Flat Model (Dependencies) - Seprate request for each LT