HemeMap
=======

Assembling and modeling the knowledge around heme pathogenicity and pathway dysregulation in the context of hemolytic
disorders. The data hosted in this repo was curated by `Farah Humayun <https://github.com/Fahumayun>`_ in context of her
Master's Thesis. The curated documents are located in the ``hememap`` directory.

Installation
------------
To install the ``hememap`` python package for programmatic access to the BEL files
in this repository, use the following code in your shell:

.. code-block:: sh

    $ git clone https://github.com/hememap/hememap.git
    $ cd hememap
    $ pip install -e .
    
Commands
--------

To see all the commands, simply run:

    $ hememap
    
Usage
-----
To get the BEL graph, use the following code:

.. code-block:: python

    import hememap
    graph = hememap.get_graph()
    graph.summarize()


Annotations
~~~~~~~~~~~
Auxiliary annotations are located in the hememap/annotations directory. These include:

1. TimePoint.
2. Species.
3. Concentration.
