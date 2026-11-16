"""Audit reporting coverage, construct agreement and unit agreement."""
import argparse
import csv
from collections import Counter
from pathlib import Path

TOPICS = ('cleaning', 'facility_condition', 'visits')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset', type=Path)
    args = parser.parse_args()
    with args.dataset.open(encoding='utf-8', newline='') as file:
        records = list(csv.DictReader(file))

    keys = Counter((row['source_id'], row['topic']) for row in records)
    source_ids = {row['source_id'] for row in records}
    expected_keys = {(source_id, topic) for source_id in source_ids for topic in TOPICS}
    if len(source_ids) != 6 or keys.keys() != expected_keys or any(n != 1 for n in keys.values()):
        raise ValueError('Expected one row per topic for each of six source reports.')

    for topic in TOPICS:
        observed = [row for row in records if row['topic'] == topic and row['reported_measure']]
        measures = {row['reported_measure'] for row in observed}
        units = {row['unit'] for row in observed}
        print(f'{topic}: {len(observed)}/6 reported, {len(measures)} measures, {len(units)} units')
        for row in observed:
            value = float(row['actual'])
            print(f"  {row['source_id']} p.{row['page']}: {row['reported_measure']} = {value:g} {row['unit']}")


if __name__ == '__main__':
    main()
