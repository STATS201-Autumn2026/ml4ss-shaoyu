# Beijing PM2.5 forecasting reliability

STATS 201, Shaoyu Feng. Compare a pooled random forest with persistence on the same chronological holdout.

Data: https://doi.org/10.24432/C5RK5G (CC BY 4.0); prepared dataset: https://huggingface.co/datasets/DKU-STATS201-Autumn2026/Shaoyu-Feng-Beijing-Air-Quality . The notebook downloads UCI directly, builds consecutive station-hour pairs and fits preprocessing on training rows only.

## Reproduce
Open `beijing_pm25_starter.ipynb` in Colab, install packages in `requirements.txt` if needed, and run all cells. The notebook uses seed 42; package versions from the completed runtime were not recorded. Outputs in the working directory: `beijing_pm25_next_hour_prepared.csv`, `station_model_evaluation.csv`, `station_mae_comparison.png`. Expected counts: 409180 pairs; 327335 train; 81845 test. Saved rerun MAE: persistence 10.096646; RF 9.808633; RMSE 19.577366 and 18.645548. The supplied station CSV is transcribed from the six-decimal displayed notebook output; the grayscale report figure is redrawn from that table. Rerunning the notebook regenerates the full-precision CSV and original plot.

`appendix_a.drawio` is the editable workflow; `appendix_a.png` is its matching schematic rendered separately. Rolling validation and high-pollution error checks are proposed, not completed. Historical prediction only; no causal or operational deployment claim.

Before submission, record this repository commit and the dataset revision, test reviewer access and check that the hosted CSV matches the rerun.
