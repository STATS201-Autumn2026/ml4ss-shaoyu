# Shanghai park reporting audit

This reproducible check uses three topics from six public park maintenance project tables. Python 3.9 or later is sufficient.

- [Hugging Face dataset, revision dfd580a](https://huggingface.co/datasets/DKU-STATS201-Autumn2026/Shaoyu-Feng-urban-park-management/tree/dfd580af03927b0368a69b6974f9af34b526d894)
- [Download the pilot CSV at this revision](https://huggingface.co/datasets/DKU-STATS201-Autumn2026/Shaoyu-Feng-urban-park-management/resolve/dfd580af03927b0368a69b6974f9af34b526d894/02_shanghai_park_ps1_pilot_2024_2025.csv)

Download the CSV to the directory containing the script, then run:

```sh
python3 pilot.py 02_shanghai_park_ps1_pilot_2024_2025.csv
```

Compare the printed output with `expected_output.txt`. It reports the number of project tables with matching entries and the number of distinct coded definitions and units for each topic. The visitor-count discrepancy between the report narrative and table is documented in the dataset card.

Pilot CSV SHA-256: `e03b2c40223c190e65b4b62a3ed10355b4a4d789d070402e6c2e83447150c7a1`.
