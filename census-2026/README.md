# census-2026

**The global public genomic record cannot see most of the world's influenza reporting: a complete enumeration of the architecture linking WHO case reporting to public sequence deposition, and a cross-pathogen test of the sampling exponent**

Yuan S et al. · *Nature Communications*, under preparation · 2026

---

## Reproducibility

This pipeline runs entirely from public data sources. No proprietary data required.

```bash
# 1. Create environment
conda env create -f environment.yml
conda activate meridian-census

# 2. Run full pipeline
make all
```

`make all` fetches WHO FluNet data → computes sampling exponents → generates figures.

## Pipeline structure

```
pipeline/
  00_fetch/
    fetch_flunet.py       # WHO FluNet API (public, no account)
    fetch_ncbi_influenza.py   # NCBI Influenza Virus DB (public API)
  01_process/
    compute_alpha.py      # OLS regression: log(sequences) ~ log(cases)
    classify_countries.py # 183 WHO units → gap classification
  02_figures/
    fig1_alpha_scatter.py
    fig2_observability_map.py
data/
  raw/                    # fetched from APIs (gitignored)
  processed/              # intermediate outputs (gitignored)
output/
  figures/                # SVG outputs committed to repo
```

## Key results

- Pooled sampling exponent: α = 0.716 (influenza), 0.819 (RSV)
- 183 WHO reporting units classified
- 150 countries show a gap between case reporting and sequence deposition
- 113 of 183 units report influenza with zero public sequence deposition

## Data sources

| Input | Source | Access |
|-------|--------|--------|
| Case counts | [WHO FluNet](https://www.who.int/tools/flunet) | Public API, no account |
| Sequence counts | [NCBI Influenza Virus DB](https://www.ncbi.nlm.nih.gov/genomes/FLU/) | Public API via Entrez |
| Country metadata | WHO Member States | Static CSV |

## Pre-registration

Analysis plan pre-registered on OSF before data analysis: [link TBD at submission]

## License

Code: MIT. Data products derived from WHO FluNet are subject to [CC BY-NC-SA 3.0 IGO](https://creativecommons.org/licenses/by-nc-sa/3.0/igo/).
