#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Time series of commits for a GitHub user between 2012 and 2016.

This module contains one pandas Dataframe: ``data``.

.. rubric:: ``data``

:bokeh-dataframe:`bokeh.sampledata.commits.data`

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from ..util.sampledata import package_csv

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'data',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

def _read_data():
    '''

    '''
    from ..util.dependencies import import_required
    module = 'commits'
    pd = import_required('pandas', '%s sample data requires Pandas (http://pandas.pydata.org) to be installed' % module)

    data = package_csv(module, 'commits.txt.gz', parse_dates=True, header=None, names=['day', 'datetime'], index_col='datetime')
    data.index = pd.to_datetime(data.index, utc=True,).tz_convert('US/Central')
    data['time'] = data.index.time

    return data

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

data = _read_data() 
