import treeswift
from iterpop import iterpop as ip
import pandas as pd
import typing

from .alife_dataframe_to_treeswift_trees \
    import alife_dataframe_to_treeswift_trees


def alife_dataframe_to_treeswift_tree(
    df: pd.DataFrame,
    setattrs: typing.Optional[typing.Union[
        typing.Iterable[str],
        typing.Mapping[str, str],
    ]] = None,
    setup_edge_lengths: bool = False,
    *,
    progress_wrap: typing.Callable = lambda x, **_: x,
) -> typing.Optional[treeswift.Tree]:
    """Open a phylogeny dataframe formatted to the artificial life community
    data format standards as a treeswift tree.

    Returns None if df is empty.

    If two or more clades exist that do not share a common ancestor, an
    exception will be raised.

    See Also
    ----------
    alife_dataframe_to_treeswift_trees
    """

    return ip.poursingleton(
        alife_dataframe_to_treeswift_trees(
            df,
            setattrs=setattrs,
            setup_edge_lengths=setup_edge_lengths,
            progress_wrap=progress_wrap,
        ),
    )
