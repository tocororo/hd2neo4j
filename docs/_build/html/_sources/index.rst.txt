
hd2neo4j
========

**hd2neo4j** is a tool for transforming heterogeneous data into knowledge graphs compatible with Neo4j.

Overview
--------

hd2neo4j enables the transformation of data from various sources and formats into a structured knowledge graph that can be imported into Neo4j. Its purpose is to simplify the integration and management of complex data—often originating from multiple sources—through a user-defined configuration.

Installation
------------

You can install hd2neo4j using pip:

.. code-block:: bash

    pip install hd2neo4j

How to Use
==========

To transform data into a Neo4j knowledge graph using ``hd2neo4j``, follow these steps:

1. Import Services
------------------

First, import the required classes from ``hd2neo4j.services``:

.. code-block:: python

    from hd2neo4j.services import RepositoryService, MapperService

2. Connect to Neo4j
-------------------

Create a ``RepositoryService`` instance to connect to your Neo4j database:

.. code-block:: python

    r_service: RepositoryService = RepositoryService(
        "neo4j://connection-uri:port", "user", "Neo4j_password", "database_name"
    )

3. Load Mapping Configuration and Data
--------------------------------------

You will need:

- A JSON configuration file that defines how the data should be mapped.
- An array or iterable of data entries to transform.

4. Run the Mapping
------------------

Initialize the ``MapperService`` and start the mapping process:

.. code-block:: python

    m_service: MapperService = MapperService(
        mapping_config=config, 
        repository_service=r_service, 
        data_to_map=data
    )

    m_service.start_mapping()

5. Optional: Clean the Database
-------------------------------

You can clear the contents of the database before performing a new mapping:

.. code-block:: python

    r_service.clean_graph_db()


License
-------

This project is licensed under the **GPL v3.0**.

Author
------

Jorge Luis Arencibia Rodríguez

.. toctree::
   :maxdepth: 2
   :caption: Contents:

