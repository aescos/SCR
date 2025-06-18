Basic structure:
1.  DATA-ORIGIN:
2.  DATA-DATE:
3.  DATA-VERSION:
4.  DOWLOADED-SCRIPT
5.  SOFTWARE-VERSION:
6.  METHODS/WORKFLOWS:

# Annotation file filtering

1.  DATA-ORIGIN:
path(/Users/alejandraescos/Documents/github/SCR/data)

2.  DATA-DATE:
20250317

3.  DATA-VERSION:

4.  DOWLOADED-SCRIPT:
0002_gtf_split_atributes.py
```
def parse_attributes(attr_string):
    attrs = {}
    for attr in attr_string.strip().split(';'):
        if attr:
            key, value = attr.strip().split(' ', 1)
            # Remove surrounding quotes
            attrs[key] = value.strip('"')
    return attrs

def extr_gtf(file_path):
    gene_utrs = {}

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            fields = line.strip().split('\t')
            if len(fields) != 9:
                continue

            feature_type = fields[2]
            if feature_type != 'three_prime_utr':
                continue

            attributes = parse_attributes(fields[8])
            gene_id = attributes.get('gene_id')
            if not gene_id:
                continue

            start = int(fields[3])
            end   = int(fields[4])

            # Keep only the earliest (lowest 'start') 3' UTR per gene
            if gene_id not in gene_utrs or start < gene_utrs[gene_id]['start']:
                # Replaces the literal 'three_prime_utr' text with the gene_id
                # (If you don’t want that replacement, remove .replace() call)
                gene_utrs[gene_id] = {
                    'line': line.strip().replace("three_prime_utr", gene_id),
                    'start': start,
                    'end': end
                }

    # Print each earliest UTR line
    for utr_info in gene_utrs.values():
        print(utr_info['line'])

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 0001_gtf_split_atributes.py <input.gtf>")
        sys.exit(1)
    extr_gtf(sys.argv[1])
```
Then in bash:

```zsh 5.9 (arm64-apple-darwin24.0)
python3 /Users/alejandraescos/Documents/github/SCR/scripts/0002_gtf_s
plit_atributes.py /Users/alejandraescos/Documents/github/SCR/data/0001_dmle.gtf > /Users/alejandraescos/Documents/github/SCR/data/0002_dmle_3UTR.gtf
```

5.  SOFTWARE-VERSION:
python 3.12.4

6.  METHODS/WORKFLOWS:

