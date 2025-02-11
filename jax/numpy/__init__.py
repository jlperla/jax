# Copyright 2018 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/jax-ml/jax/issues/7570

from jax.numpy import fft as fft
from jax.numpy import linalg as linalg

from jax._src.basearray import Array as ndarray  # noqa: F401

from jax._src.dtypes import (
    isdtype as isdtype,
)

from jax._src.numpy.lax_numpy import (
    ComplexWarning as ComplexWarning,
    allclose as allclose,
    angle as angle,
    append as append,
    apply_along_axis as apply_along_axis,
    apply_over_axes as apply_over_axes,
    arange as arange,
    argmax as argmax,
    argmin as argmin,
    argwhere as argwhere,
    around as around,
    array as array,
    array_equal as array_equal,
    array_equiv as array_equiv,
    array_repr as array_repr,
    array_split as array_split,
    array_str as array_str,
    astype as astype,
    asarray as asarray,
    atleast_1d as atleast_1d,
    atleast_2d as atleast_2d,
    atleast_3d as atleast_3d,
    bincount as bincount,
    block as block,
    broadcast_arrays as broadcast_arrays,
    broadcast_shapes as broadcast_shapes,
    broadcast_to as broadcast_to,
    can_cast as can_cast,
    choose as choose,
    clip as clip,
    column_stack as column_stack,
    compress as compress,
    concat as concat,
    concatenate as concatenate,
    convolve as convolve,
    copy as copy,
    corrcoef as corrcoef,
    correlate as correlate,
    cov as cov,
    cross as cross,
    delete as delete,
    diag as diag,
    diagflat as diagflat,
    diag_indices as diag_indices,
    diag_indices_from as diag_indices_from,
    diagonal as diagonal,
    diff as diff,
    digitize as digitize,
    dsplit as dsplit,
    dstack as dstack,
    dtype as dtype,
    e as e,
    ediff1d as ediff1d,
    einsum as einsum,
    einsum_path as einsum_path,
    euler_gamma as euler_gamma,
    expand_dims as expand_dims,
    extract as extract,
    eye as eye,
    fill_diagonal as fill_diagonal,
    finfo as finfo,
    fix as fix,
    flatnonzero as flatnonzero,
    flip as flip,
    fliplr as fliplr,
    flipud as flipud,
    fmax as fmax,
    fmin as fmin,
    frombuffer as frombuffer,
    fromfile as fromfile,
    fromfunction as fromfunction,
    fromiter as fromiter,
    fromstring as fromstring,
    from_dlpack as from_dlpack,
    gcd as gcd,
    geomspace as geomspace,
    get_printoptions as get_printoptions,
    gradient as gradient,
    histogram as histogram,
    histogram_bin_edges as histogram_bin_edges,
    histogram2d as histogram2d,
    histogramdd as histogramdd,
    hsplit as hsplit,
    hstack as hstack,
    i0 as i0,
    identity as identity,
    iinfo as iinfo,
    indices as indices,
    inf as inf,
    insert as insert,
    interp as interp,
    isclose as isclose,
    iscomplex as iscomplex,
    iscomplexobj as iscomplexobj,
    isreal as isreal,
    isrealobj as isrealobj,
    isscalar as isscalar,
    issubdtype as issubdtype,
    iterable as iterable,
    ix_ as ix_,
    kron as kron,
    lcm as lcm,
    linspace as linspace,
    load as load,
    logspace as logspace,
    mask_indices as mask_indices,
    matrix_transpose as matrix_transpose,
    meshgrid as meshgrid,
    moveaxis as moveaxis,
    nan as nan,
    nan_to_num as nan_to_num,
    nanargmax as nanargmax,
    nanargmin as nanargmin,
    ndim as ndim,
    newaxis as newaxis,
    nonzero as nonzero,
    packbits as packbits,
    pad as pad,
    permute_dims as permute_dims,
    pi as pi,
    piecewise as piecewise,
    place as place,
    printoptions as printoptions,
    promote_types as promote_types,
    put as put,
    put_along_axis as put_along_axis,
    ravel as ravel,
    ravel_multi_index as ravel_multi_index,
    repeat as repeat,
    reshape as reshape,
    resize as resize,
    result_type as result_type,
    roll as roll,
    rollaxis as rollaxis,
    rot90 as rot90,
    round as round,
    save as save,
    savez as savez,
    searchsorted as searchsorted,
    select as select,
    set_printoptions as set_printoptions,
    shape as shape,
    size as size,
    split as split,
    squeeze as squeeze,
    stack as stack,
    swapaxes as swapaxes,
    take as take,
    take_along_axis as take_along_axis,
    tile as tile,
    trace as trace,
    trapezoid as trapezoid,
    transpose as transpose,
    tri as tri,
    tril as tril,
    tril_indices as tril_indices,
    tril_indices_from as tril_indices_from,
    trim_zeros as trim_zeros,
    triu as triu,
    triu_indices as triu_indices,
    triu_indices_from as triu_indices_from,
    trunc as trunc,
    unpackbits as unpackbits,
    unravel_index as unravel_index,
    unstack as unstack,
    unwrap as unwrap,
    vander as vander,
    vsplit as vsplit,
    vstack as vstack,
    where as where,
)

from jax._src.numpy.array_creation import (
    empty as empty,
    empty_like as empty_like,
    full as full,
    full_like as full_like,
    ones as ones,
    ones_like as ones_like,
    zeros as zeros,
    zeros_like as zeros_like,
)

from jax._src.numpy.scalar_types import (
    bfloat16 as bfloat16,
    bool_ as bool,  # Array API alias for bool_  # noqa: F401
    bool_ as bool_,
    cdouble as cdouble,
    csingle as csingle,
    complex128 as complex128,
    complex64 as complex64,
    complex_ as complex_,
    double as double,
    float16 as float16,
    float32 as float32,
    float64 as float64,
    float8_e4m3b11fnuz as float8_e4m3b11fnuz,
    float8_e4m3fn as float8_e4m3fn,
    float8_e4m3fnuz as float8_e4m3fnuz,
    float8_e5m2 as float8_e5m2,
    float8_e5m2fnuz as float8_e5m2fnuz,
    float_ as float_,
    int4 as int4,
    int8 as int8,
    int16 as int16,
    int32 as int32,
    int64 as int64,
    int_ as int_,
    single as single,
    uint as uint,
    uint4 as uint4,
    uint8 as uint8,
    uint16 as uint16,
    uint32 as uint32,
    uint64 as uint64,
)

from jax._src.numpy.sorting import (
    argpartition as argpartition,
    argsort as argsort,
    lexsort as lexsort,
    partition as partition,
    sort as sort,
    sort_complex as sort_complex,
)

from jax._src.numpy.tensor_contractions import (
  dot as dot,
  inner as inner,
  matmul as matmul,
  matvec as matvec,
  outer as outer,
  tensordot as tensordot,
  vecdot as vecdot,
  vecmat as vecmat,
  vdot as vdot,
)

from jax._src.numpy.window_functions import (
    bartlett as bartlett,
    blackman as blackman,
    hamming as hamming,
    hanning as hanning,
    kaiser as kaiser,
)

# NumPy generic scalar types:
from numpy import (
    character as character,
    complexfloating as complexfloating,
    flexible as flexible,
    floating as floating,
    generic as generic,
    inexact as inexact,
    integer as integer,
    number as number,
    object_ as object_,
    signedinteger as signedinteger,
    unsignedinteger as unsignedinteger,
)

# TODO(slebedev): Remove the try-except once we upgrade to ml_dtypes 0.4.1.
try:
  from jax._src.numpy.scalar_types import (
    int2 as int2,
    uint2 as uint2,
  )
except ImportError:
  pass

# TODO: Remove the try-except once we upgrade to ml_dtypes 0.5.0
try:
  from jax._src.numpy.scalar_types import (
    float8_e3m4 as float8_e3m4,
    float8_e4m3 as float8_e4m3,
    float8_e8m0fnu as float8_e8m0fnu,
  )
except ImportError:
  pass

from jax._src.numpy.array_api_metadata import (
  __array_api_version__ as __array_api_version__,
  __array_namespace_info__ as __array_namespace_info__,
)

from jax._src.numpy.index_tricks import (
  c_ as c_,
  index_exp as index_exp,
  mgrid as mgrid,
  ogrid as ogrid,
  r_ as r_,
  s_ as s_,
)

from jax._src.numpy.polynomial import (
    poly as poly,
    polyadd as polyadd,
    polyder as polyder,
    polydiv as polydiv,
    polyfit as polyfit,
    polyint as polyint,
    polymul as polymul,
    polysub as polysub,
    polyval as polyval,
    roots as roots,
)

from jax._src.numpy.reductions import (
    amin as amin,
    amax as amax,
    any as any,
    all as all,
    average as average,
    count_nonzero as count_nonzero,
    cumprod as cumprod,
    cumsum as cumsum,
    cumulative_prod as cumulative_prod,
    cumulative_sum as cumulative_sum,
    max as max,
    mean as mean,
    median as median,
    min as min,
    nancumsum as nancumsum,
    nancumprod as nancumprod,
    nanmax as nanmax,
    nanmean as nanmean,
    nanmedian as nanmedian,
    nanmin as nanmin,
    nanpercentile as nanpercentile,
    nanprod as nanprod,
    nanquantile as nanquantile,
    nanstd as nanstd,
    nansum as nansum,
    nanvar as nanvar,
    percentile as percentile,
    prod as prod,
    ptp as ptp,
    quantile as quantile,
    std as std,
    sum as sum,
    var as var,
)

from jax._src.numpy.setops import (
    intersect1d as intersect1d,
    isin as isin,
    setdiff1d as setdiff1d,
    setxor1d as setxor1d,
    union1d as union1d,
    unique as unique,
    unique_all as unique_all,
    unique_counts as unique_counts,
    unique_inverse as unique_inverse,
    unique_values as unique_values,
)

from jax._src.numpy.ufuncs import (
    abs as abs,
    absolute as absolute,
    acos as acos,
    acosh as acosh,
    add as add,
    arccos as arccos,
    arccosh as arccosh,
    arcsin as arcsin,
    arcsinh as arcsinh,
    arctan as arctan,
    arctan2 as arctan2,
    arctanh as arctanh,
    asin as asin,
    asinh as asinh,
    atan as atan,
    atanh as atanh,
    atan2 as atan2,
    bitwise_and as bitwise_and,
    bitwise_count as bitwise_count,
    bitwise_invert as bitwise_invert,
    bitwise_left_shift as bitwise_left_shift,
    bitwise_not as bitwise_not,
    bitwise_right_shift as bitwise_right_shift,
    bitwise_or as bitwise_or,
    bitwise_xor as bitwise_xor,
    cbrt as cbrt,
    ceil as ceil,
    conj as conj,
    conjugate as conjugate,
    copysign as copysign,
    cos as cos,
    cosh as cosh,
    deg2rad as deg2rad,
    degrees as degrees,
    divide as divide,
    divmod as divmod,
    equal as equal,
    exp as exp,
    exp2 as exp2,
    expm1 as expm1,
    fabs as fabs,
    float_power as float_power,
    floor as floor,
    floor_divide as floor_divide,
    fmod as fmod,
    frexp as frexp,
    greater as greater,
    greater_equal as greater_equal,
    heaviside as heaviside,
    hypot as hypot,
    imag as imag,
    invert as invert,
    isfinite as isfinite,
    isinf as isinf,
    isnan as isnan,
    isneginf as isneginf,
    isposinf as isposinf,
    ldexp as ldexp,
    left_shift as left_shift,
    less as less,
    less_equal as less_equal,
    log as log,
    log10 as log10,
    log1p as log1p,
    log2 as log2,
    logaddexp as logaddexp,
    logaddexp2 as logaddexp2,
    logical_and as logical_and,
    logical_not as logical_not,
    logical_or as logical_or,
    logical_xor as logical_xor,
    maximum as maximum,
    minimum as minimum,
    mod as mod,
    modf as modf,
    multiply as multiply,
    negative as negative,
    nextafter as nextafter,
    not_equal as not_equal,
    positive as positive,
    pow as pow,
    power as power,
    rad2deg as rad2deg,
    radians as radians,
    real as real,
    reciprocal as reciprocal,
    remainder as remainder,
    right_shift as right_shift,
    rint as rint,
    sign as sign,
    signbit as signbit,
    sin as sin,
    sinc as sinc,
    sinh as sinh,
    spacing as spacing,
    sqrt as sqrt,
    square as square,
    subtract as subtract,
    tan as tan,
    tanh as tanh,
    true_divide as true_divide,
)

from jax._src.numpy.ufunc_api import (
    frompyfunc as frompyfunc,
    ufunc as ufunc,
)

from jax._src.numpy.vectorize import vectorize as vectorize

# Dynamically register numpy-style methods on JAX arrays.
from jax._src.numpy.array_methods import register_jax_array_methods
register_jax_array_methods()
del register_jax_array_methods


_deprecations = {
  # Finalized 2024-12-13; remove after 2024-3-13
  "round_": (
    "jnp.round_ was deprecated in JAX 0.4.38; use jnp.round instead.",
    None
  ),
}

import typing
if not typing.TYPE_CHECKING:
  from jax._src.deprecations import deprecation_getattr as _deprecation_getattr
  __getattr__ = _deprecation_getattr(__name__, _deprecations)
  del _deprecation_getattr
del typing
