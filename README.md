# Datathon4Justice - Team 3 Repository

### Structure of the Repository

#### code

This folder is where you can add any code that you want to share with the team.  This can include Python scripts, Jupyter notebooks, R scipts, or whatever!

#### primary_datasets 

This folder containts the main datasets provided to all participants by the QSIDE team.  These should be downloaded and used, but _please don't overwrite anything in this folder_.  The primary datasets consist of two collections:

* `Williamstown_policing`:
  - `Logs2019.pdf`
  - `Logs2018.pdf`

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
          df = pd.read_csv("allmn.csv", dtype={45:str, 46:str}) #To avoid datatype warnings.
```

