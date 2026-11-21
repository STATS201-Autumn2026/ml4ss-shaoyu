# STATS201 — Beijing PM2.5 Next-Hour Prediction

**Author:** Shaoyu Feng (`sf337`).  
**Project:** Evaluating the Reliability of Next-Hour PM2.5 Forecasts Across Beijing Monitoring Stations.

## Research question
Does a pooled Random Forest predict next-hour PM2.5 more accurately than persistence in held-out 2016–2017 observations, and how does the improvement vary across 12 Beijing monitoring stations?

## Data
**Primary source:** UCI [Beijing Multi-Site Air Quality](https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data), Chen (2017), DOI: https://doi.org/10.24432/C5RK5G (CC BY 4.0). **Prepared data are released on Hugging Face**: `PENDING_HF_URL_AND_COMMIT`.

Prepared observations: 409,180 station-hour pairs, 12 sites. Target is `pm25_next_hour`, measured in µg/m³. Do **not** use the future target or target timestamp as a model predictor.

## Reproduce
1. Open [`beijing_pm25_starter.ipynb`](beijing_pm25_starter.ipynb) in Google Colab (Python 3 runtime).
2. Run the install command `!pip install -r requirements.txt` if you uploaded the requirements file, or use Colab's installed versions for pandas, numpy, requests, scikit-learn and matplotlib.
3. Execute notebook cells **in order**. Internet access is needed to download the UCI ZIP.
4. Expect `beijing_pm25_next_hour_prepared.csv`, `station_model_evaluation.csv`, and `station_mae_comparison.png` in the runtime directory.
5. Compare the latter two outputs with the committed files in [`results/`](results/).

## Method
- Global chronological cut-off: **2016-05-12 18:00:00** based on target timestamp.
- Training: **327,335** pairs; testing: **81,845**.
- Baseline: persistence (`PM2.5` at t predicts t+1).
- Random Forest: 20 trees, maximum depth 12, minimum leaf size 5, random state 42; training-only median/mode imputation and one-hot encoding for categorical columns.
- Metrics: MAE and RMSE overall and across all 12 stations.

## Pilot results (from user-provided output CSV)
| Metric | Persistence | Random Forest |
|---|---:|---:|
| Weighted site MAE (µg/m³) | 10.097 | 9.829 |

Relative MAE decrease: **2.65%**. A small improvement, not causal evidence or proof of future real-world reliability. See [`results/station_mae_comparison.png`](results/station_mae_comparison.png).

## Reproducibility caution
The notebook here is a **reconstructed copy** of the provided starter with the parameter change reported during the user's Colab run. It is **not the original executed Notebook export** and may not contain the exact saved environment metadata. Before claiming exact computational reproduction, download your executed `.ipynb` from Colab and replace this copy; rerun and check the numerical outputs. After publishing, record the GitHub commit hash and Hugging Face revision in the proposal.

## License and responsible use
Original data CC BY 4.0. Maintain attribution; this code is supplied for course reproduction. The data cover historical observations and station-level prediction accuracy; they do not measure individual exposure or estimate causal interventions.
