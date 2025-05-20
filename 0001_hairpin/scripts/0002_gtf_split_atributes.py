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
        print("Usage: python3 0002_gtf_split_atributes.py <input.gtf>")
        sys.exit(1)
    extr_gtf(sys.argv[1])

