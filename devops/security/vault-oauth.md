Vault : - a room with a strong door and thick walls in a bank, etc. that is used for keeping money and other valuable things safe.

# How to store passwords in vault?

* Developers can store encrypted data without developing their own encryption techniques and it allows security teams to define security parameters. 

* Secure Secret Storage: -  Vault encrypts the secret information (API keys, passwords or certificates) before storing it on to the persistent (secondary) storage.

* Password Vault / Manager - It is a program that stores usernames and passwords for multiple applications in a secure location and in an encrypted format. 

* Note:- that some password managers will also generate more secure, random passwords, called one-time passwords [OTPs], for the user for each site.

* OAuth (Open Authorization):-  It is an authorization framework or protocol that enables an application or service to obtain limited access to a protected HTTP resource. 

- OAuth 2.0 is a framework, not a protocol (like version 1.0)

- how unrelated servers and services can safely allow authenticated access to their assets without actually sharing the initial, related, single logon credential. In authentication parlance, this is known as secure, third-party, user-agent, delegated authorization.

- To use REST APIs with OAuth in Oracle Integration, you need to register your Oracle Integration instance as a trusted application in Oracle Identity Cloud Service.

- It is about authorization in particular and not directly about authentication. Authentication is the process of a user or subject proving its ownership of a presented identity, by providing a password or some other uniquely owned or presented factor. 

- Authorization is the process of letting a subject access resources after a successful authentication, oftentimes somewhere else. 

- OAuth stands for open authentication, but it’s more helpful to understand it by thinking about it as open AUTHorization.

- JWTs (JSON Web Token) can be used as OAuth 2.0 Bearer Tokens to encode all relevant parts of an access token into the access token itself instead of having to store them in a database.

# Below are steps How OAuth works.

* The 1st website connects to the 2nd website on behalf of the user, using OAuth, providing the user’s verified identity.
* The 2nd site generates a one-time token and a one-time secret unique to the transaction and parties involved.
* The 1st site gives this token and secret to the initiating user’s client software.
* The client’s software presents the request token and secret to their authorization provider (which may or may not be the 2nd site).
* If not already authenticated to the authorization provider, the client may be asked to authenticate. 
* After authentication, the client is asked to approve the authorization transaction to the 2nd website.
* The user approves (or their software silently approves) a particular transaction type at the 1st website.
* The user is given an approved access token (notice it’s no longer a request token).
* The user gives the approved access token to the 1st website.
* The 1st website gives the access token to the 2nd website as proof of authentication on behalf of the user.
* The 2nd website lets the 1st website access their site on behalf of the user.
* The user sees a successfully completed transaction occurring.
