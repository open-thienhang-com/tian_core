
<a id="readme-top"></a>


<br />
<div align="center">
  <a href="dev.thienhang.com">
    
  </a>

  <h3 align="center">DataOps - Multiple data platform</h3>

  <p align="center">
    open@thienhang.com
    <br />
    <a href="https://python.thienhang.com"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://pypi.org/project/tian_core/">Pypi</a>
    ·
    <a href="https://open.thienhang.com">Website</a>
  </p>
</div>



# CMS CORE

`tian_core` is a Python-based core CMS (Content Management System) library that provides foundational components for building scalable and maintainable applications. The library leverages key architectural patterns such as **CQRS (Command Query Responsibility Segregation)**, **EventBus**, **SQL Builder**, and **Unit of Work** to enable clean, efficient, and flexible management of data and operations.

## Key Features

- **CQRS (Command Query Responsibility Segregation)**: Separate command and query logic for better scalability and maintainability, allowing for distinct handling of read and write operations.
- **EventBus**: Implements an EventBus pattern for decoupled communication between components, enabling event-driven architecture and real-time updates across the system.
- **SQL Builder**: A flexible and dynamic SQL query builder that simplifies the creation of SQL queries, reducing the need for raw SQL strings and ensuring cleaner, more maintainable code.
- **Unit of Work**: A pattern that helps manage and track changes to the system’s data, ensuring that multiple operations are executed as part of a single transaction, improving consistency and reliability.

## Installation

To install `tian_core`, you can use either Poetry or pip:

### Using Poetry
```bash
poetry add tian_core


Architecture Overview
CQRS: By separating commands (write operations) and queries (read operations), tian_core allows you to design systems where reads and writes can be optimized independently.
EventBus: The EventBus enables communication between decoupled components through events, allowing you to implement event-driven patterns such as eventual consistency and asynchronous processing.
SQL Builder: Dynamically build SQL queries in a clean and reusable way, minimizing the risk of SQL injection and making your code more flexible and maintainable.
Unit of Work: Manage database transactions by grouping multiple operations into a single unit of work, ensuring that operations are either committed or rolled back as a group.