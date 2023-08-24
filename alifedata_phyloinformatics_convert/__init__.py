"""Top-level package for alifedata-phyloinformatics-convert."""

__author__ = """Matthew Andres Moreno"""
__email__ = 'm.more500@gmail.com'
__version__ = '0.14.0'

from .alife_dataframe_to_biopython_tree \
    import alife_dataframe_to_biopython_tree
from .alife_dataframe_to_biopython_trees \
    import alife_dataframe_to_biopython_trees
from .alife_dataframe_to_dict_of_lists import alife_dataframe_to_dict_of_lists
from .alife_dataframe_to_dendropy_tree import alife_dataframe_to_dendropy_tree
from .alife_dataframe_to_dendropy_trees \
    import alife_dataframe_to_dendropy_trees
from .alife_dataframe_to_ete_tree import alife_dataframe_to_ete_tree
from .alife_dataframe_to_networkx_digraph \
    import alife_dataframe_to_networkx_digraph
from .anytree_tree_to_alife_dataframe \
    import anytree_tree_to_alife_dataframe
from .biopython_tree_to_alife_dataframe \
    import biopython_tree_to_alife_dataframe
from .dendropy_tree_to_alife_dataframe import dendropy_tree_to_alife_dataframe
from .ete_tree_to_alife_dataframe import ete_tree_to_alife_dataframe
from .networkx_digraph_to_alife_dataframe \
    import networkx_digraph_to_alife_dataframe
from .dendropy_tree_to_scipy_linkage_matrix \
    import dendropy_tree_to_scipy_linkage_matrix
from .scipy_linkage_matrix_to_dendropy_tree \
    import scipy_linkage_matrix_to_dendropy_tree
from .RosettaTree import RosettaTree

# adapted from https://stackoverflow.com/a/31079085
__all__ = [
    'alife_dataframe_to_biopython_tree',
    'alife_dataframe_to_biopython_trees',
    'alife_dataframe_to_dendropy_tree',
    'alife_dataframe_to_dendropy_trees',
    'alife_dataframe_to_ete_tree',
    'alife_dataframe_to_ete_trees',
    'alife_dataframe_to_networkx_digraph',
    'anytree_tree_to_alife_dataframe',
    'biopython_tree_to_alife_dataframe',
    'dendropy_tree_to_alife_dataframe',
    'dendropy_tree_to_scipy_linkage_matrix',
    'ete_tree_to_alife_dataframe',
    'networkx_digraph_to_alife_dataframe',
    'scipy_linkage_matrix_to_dendropy_tree',
    'RosettaTree',
]
