.PHONY: all fetch process figures clean

all: fetch process figures

fetch:
	python pipeline/00_fetch/fetch_flunet.py

process:
	python pipeline/01_process/compute_alpha.py

figures:
	python pipeline/02_figures/fig1_alpha_scatter.py

clean:
	rm -rf data/raw data/processed output/figures
