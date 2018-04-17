# website-pathology

[![Build Status](https://travis-ci.org/DIAGNijmegen/website-pathology.svg?branch=master)](https://travis-ci.org/DIAGNijmegen/website-pathology)

Pilot website for Computational Pathology Group

## Usage

### Live reload

Run in main directory:

```
pelican content --autoreload  --output output --settings pelicanconf.py
```

### Running dev server

Run in output directory:

```
python -m pelican.server
```

The website should be accessible at localhost:8000. 
