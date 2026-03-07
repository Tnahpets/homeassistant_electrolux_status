# Importing the AEG washing machine catalog
from .aeg_catalog import AEGWashingMachineCatalog

# Registering the AEG washing machine catalog
CATALOG_MODEL["LR8MUNSTER"] = AEGWashingMachineCatalog()