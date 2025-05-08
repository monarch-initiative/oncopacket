# Installation

The package is designed to work with Python 3.8 or later.

## Dependencies

Oncopacket has the following main dependencies:
- `phenopackets` (GA4GH Phenopacket Schema)
- `cdapython` (Cancer Data Aggregator Python library)
- `hpo-toolkit` (Tools for working with the Human Phenotype Ontology)
- `requests` (For API communication)

## Installation

### 1: Create a virtual environment (recommended)

First, create and activate a virtual environment, for example:

```shell
python3 -m venv oncopacket-venv
source oncopacket-venv/bin/activate  # On Windows: oncopacket-venv\Scripts\activate
```

### 2: Install from GitHub repository

Install the latest version directly from the GitHub repository:

```shell
# Ensure you are in the repo folder
cd oncopacket
python3 -m pip install --editable .
```

The package is installed in *editable* mode - any code updates are available after Python restart, without needing to reinstall.

## 3. Using Oncopacket in Jupyter notebooks (optional)

To use Oncopacket in Jupyter notebooks, first install Jupyter and ipykernel:

```shell
python3 -m pip install jupyter ipykernel
```

Then, create a new Jupyter kernel and register it with Jupyter:

```shell
python -m ipykernel install --user --name oncopacket_env --display-name "oncopacket"
```

Start Jupyter to work with the notebooks in the repository:

```shell
cd notebooks
jupyter-notebook
```

At this point, a Jupyter page should open in your browser. Navigate to any notebook (and 
activate the `oncopacket_env` kernel if you made one above).

## Building the documentation

To run the mkdocs server locally for documentation development:

1. Install the required packages:

```bash
pip install mkdocs-material
pip install mkdocs-material[imaging]
pip install mkdocs-material-extensions
pip install pillow cairosvg
pip install mkdocstrings[python]
```

2. Serve the documentation locally:

```bash
mkdocs serve
```

This will serve the documentation site at http://127.0.0.1:8000/ and dynamically show 
changes. Merging to the main branch will update the public documentation site.
