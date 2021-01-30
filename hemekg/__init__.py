# -*- coding: utf-8 -*-

"""HemeKG."""

import os

from pybel.repository import BELMetadata, BELRepository

__all__ = [
    'repository',
    'metadata',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by last name
AUTHORS = [
    'Farah Humayun',
    'Daniel Domingo-Fernández',
]

# All metadata is grouped here
metadata = BELMetadata(
    name='HemeKG',
    version=VERSION,
    authors=' and '.join(AUTHORS),
    contact='daniel.domingo.fernandez@scai.fraunhofer.de',
    description="Mechanistic knowledge surrounding heme and hemolytic disorders.",
    license='CC BY 4.0',
)

repository = BELRepository(
    HERE,
    metadata=metadata,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
