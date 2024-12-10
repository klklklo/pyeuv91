import functools
import xarray as xr
from importlib_resources import files


@functools.cache
def _read_coeffs(file):
    return xr.open_dataset(files('pyeuv91._coeffs').joinpath(file))


def get_euv91_bands_dataset():
    # return _read_coeffs('euv91_bands_dataset.nc').copy()
    # return _read_coeffs('full_2_bands.nc').copy()
    return _read_coeffs('full_2_complete.nc').copy()

def get_euv91_lines_dataset():
    # return _read_coeffs('euv91_lines_dataset.nc').copy()
    return _read_coeffs('full_2_lines.nc').copy()

def get_euv91_dataset():
    # return _read_coeffs('euv91_bands_dataset.nc').copy()
    return _read_coeffs('full_2_complete.nc').copy()