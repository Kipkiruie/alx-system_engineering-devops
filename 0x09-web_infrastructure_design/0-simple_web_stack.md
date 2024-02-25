# Simple Web Stack

A lot of websites are powered by simple web infrastructure, often composed of a single server with a LAMP stack.

## Infrastructure Design

### Components:
- **1 Server:** The server hosts all components of the web infrastructure.
- **1 Web Server (Nginx):** Nginx serves as the web server handling HTTP requests.
- **1 Application Server:** This server runs the application logic.
- **1 Application Files (Your Code Base):** The code base contains the files comprising the website/application.
- **1 Database (MySQL):** MySQL manages the website's database.

### Domain Configuration:
- **Domain Name:** foobar.com
- **www Record:** Configured to point to the server IP 8.8.8.8

## Explanation of Components

### Server:
- A server is a computer system that provides services or resources to other computers, known as clients, over a network.

### Domain Name:
- A domain name is a human-readable address used to access websites on the Internet. It provides a more memorable way to identify a website than using its IP address.

### www DNS Record:
- The www record is a type of DNS record known as a CNAME (Canonical Name) record. It points the www subdomain of a domain to another domain name, typically the root domain or another hostname.

### Web Server:
- The web server (Nginx) is responsible for handling HTTP requests from clients (e.g., web browsers) and serving web pages and other web content.

### Application Server:
- The application server is where the actual application logic resides. It processes requests, executes the application code, and generates dynamic content to be sent back to the client.

### Database:
- The database (MySQL) stores and manages the website's data. It allows for efficient storage, retrieval, and manipulation of data required by the application.

### Communication with User's Computer:
- The server communicates with the user's computer over the Internet using the HTTP protocol. When a user requests the website, their browser sends an HTTP request to the server, which responds with the requested web page.

## Issues with the Infrastructure

### Single Point of Failure (SPOF):
- Since all components are hosted on a single server, any failure of the server could lead to downtime for the entire website.

### Downtime during Maintenance:
- Performing maintenance tasks such as deploying new code or restarting the web server may result in downtime for the website, disrupting user access.

### Scalability Limitations:
- The infrastructure may struggle to handle high levels of incoming traffic, as it's not designed to scale horizontally across multiple servers.

## Infrastructure Diagram

![Simple Web Stack Infrastructure](https://raw.githubusercontent.com/B3zaleel/0x09-web_infrastructure_design/main/0-simple_web_stack.jpg)


