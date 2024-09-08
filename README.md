# Ditainer: Dependency Injection Container for Python

**Ditainer** is a lightweight and flexible Dependency Injection (DI) container for Python, designed to streamline the management of dependencies in your applications.

## Key Features

- Load dependencies (services) from YAML files.
- Inject dependencies via constructor arguments, factories, or tags.
- Easily reference other services or groups of services by tag.
- Handles circular dependencies.
- Supports importing multiple YAML files for modular configurations.

## Installation

Install **Ditainer** via PyPI:

```bash
pip install ditainer
```

## How to Use
### Service Definitions in YAML
In Ditainer, a dependency is referred to as a service. A service is typically a class that may require arguments (other services or literal values) for its initialization. Services can also be instantiated via a factory function, which can similarly receive arguments.

Additionally, services can be tagged, allowing for easy retrieval of groups of services later on.

There are three types of arguments that a service can receive:

- Literal arguments: Direct values such as strings, numbers, etc.
- References to other services: Use the prefix !ref followed by the ID of the service.
- Tagged services: Use the prefix !tagged followed by the tag to reference all services with that tag.

### Example YAML Configuration
```yaml
services:
  - id: DBSession
    module: my_module.db
    class: DBSession
    factory: create_session

  - id: UserRepository
    module: my_module.user.repository
    class: MySqlUserRepository
    arguments:
      - !ref DBSession

  - id: QueryBus
    module: my_module.query_bus
    class: InMemoryQueryBus
    arguments:
      - !tagged query_handler

  - id: UserFindByIDQueryHandler
    module: my_module.user.find_by_id_query_handler
    class: UserFindByIDQueryHandler
    arguments:
      - !ref UserRepository
    tags:
      - query_handler

  - id: UserFindByCodeQueryHandler
    module: my_module.user.find_by_code_query_handler
    class: UserFindByCodeQueryHandler
    arguments:
      - !ref UserRepository
    tags:
      - query_handler
```
In this example:
- The DBSession service is created using the create_session factory.
- The UserRepository service depends on DBSession.
- The QueryBus service aggregates all services tagged as query_handler, such as UserFindByIDQueryHandler and UserFindByCodeQueryHandler.

### Importing Multiple Service Configurations
Ditainer supports modular configuration through multiple YAML files:

```yaml
imports:
  - { resource: "./services_1.yaml" }
  - { resource: "./services_2.yaml" }
  - { resource: "./services_3.yaml" }
```

### Using Ditainer in Your Python Code
Once your YAML configuration files are ready, load them into the container as follows:

```python
import os
from ditainer.container import Container
from ditainer.loader import YAMLLoader


# Initialize container
container = Container()

# Load services from YAML
loader = YAMLLoader(container)
loader.load(os.path.join(os.path.dirname(__file__), "imports.yaml"))
```

### Accessing Services
You can now access services in your application:

```python
from my_module import container
from my_module.user import User
from my_module.user.find_by_id_query import UserFindByIdQuery


def get_user() -> User:
    query_bus = container.find("QueryBus")
    query = UserFindByIdQuery(123)

    # Dispatch query to QueryBus
    user = query_bus.ask(query)
    return user
```

### Searching for Services by Tag
If you need to retrieve all services with a specific tag:

```python
from my_module import container


query_handlers = container.search_tagged("query_handler")
```

If no services are found for the given tag, the result will be an empty list.

## Additional Examples
You can find more examples and test cases in the tests folder of the repository.

## Credits
Inspired by Node Dependency Injection (https://www.npmjs.com/package/node-dependency-injection)
