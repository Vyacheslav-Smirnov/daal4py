#*******************************************************************************
# Copyright 2014-2018 Intel Corporation
# All Rights Reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License"), the following terms apply:
#
# You may not use this file except in compliance with the License.  You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#*******************************************************************************

# daal4py SVD example for shared memory systems

import daal4py as d4p
from numpy import loadtxt, allclose

if __name__ == "__main__":

    infile = "./data/batch/svd.csv"

    # configure a SVD object
    algo = d4p.svd()
    
    # let's provide a file directly, not a table/array
    result1 = algo.compute(infile)

    # We can also load the data ourselfs and provide the numpy array
    data = loadtxt(infile, delimiter=',')
    result2 = algo.compute(data)

    # SVD result objects provide leftSingularMatrix, rightSingularMatrix and singularValues
    assert allclose(result1.leftSingularMatrix, result2.leftSingularMatrix, atol=1e-07)
    assert allclose(result1.rightSingularMatrix, result2.rightSingularMatrix, atol=1e-07)
    assert allclose(result1.singularValues, result2.singularValues, atol=1e-07)

    print('All looks good!')