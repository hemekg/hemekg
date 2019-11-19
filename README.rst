HemeKG
======
Assembling and modeling the knowledge around heme pathogenicity and pathway dysregulation in the context of hemolytic
disorders. The data hosted in this repo was curated by `Farah Humayun <https://github.com/Fahumayun>`_ in context of her
Master's Thesis. The curated documents are located in the ``hemekg`` directory. Explore HemeKG in BEL Commons at https://bel-commons-dev.scai.fraunhofer.de/network/135.

Citation
--------
If you find HemeKG useful in your work, please consider citing:

.. [1] Humayun, F., *et al.*: A computational approach for mapping heme biology in the context of hemolytic disorders. bioRxiv 804906. https://www.biorxiv.org/content/10.1101/804906v1

Installation
------------
To install the ``hemekg`` python package for programmatic access to the BEL files
in this repository, use the following code in your shell:

.. code-block:: sh

    $ git clone https://github.com/hemekg/hemekg.git
    $ cd hemekg
    $ pip install -e .
    
Commands
--------
To see all the commands, simply run:

.. code-block:: sh

    $ hemekg
    
Usage
-----
To get the BEL graph, use the following code:

.. code-block:: python

    >>> import hemekg
    >>> graph = hemekg.get_graph()
    >>> graph.summarize()

Annotations
~~~~~~~~~~~
Auxiliary annotations are located in the hemekg/annotations directory. These include:

1. TimePoint.
2. Species.
3. Concentration.
