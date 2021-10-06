# Datathon4Justice - Team 3 Repository

### Structure of the Repository

#### primary_datasets 

This folder containts the main datasets provided to all participants by the QSIDE team.  These should be downloaded and used, but _please don't overwrite anything in this folder_.  The primary datasets consist of two collections:

* `Williamstown_policing`:

* `MN_sentencing`: 
  - `2019-Drug.pdf`
  - `2019-Sex.pdf`
  - `2019-Standard.pdf`
  - `countycodes.csv`
  - `grids.csv`
  - `MNCodebook.xlxs`
  - `allmn.csv`.  To load this file:
```
          import pandas as pd
          df = pd.read_csv("allmn.csv", dtype={45:str, 46:str}) #TO avoid datatype warnings.
```

