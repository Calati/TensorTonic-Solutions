def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """

    if strategy == "first":
        seen = set()
        out = []
        for i in records:
            key = tuple(i[col] for col in key_columns)
            if key not in seen:
                seen.add(key)
                out.append(i)

    elif strategy == "last":
        seen = set()
        latest = {}
        out = []

        for i in records:
            key = tuple(i[col] for col in key_columns)
            latest[key] = i

        for i in records:
            key = tuple(i[col] for col in key_columns)
            if key not in seen:
                seen.add(key)
                out.append(latest[key])

    elif strategy == "most_complete":
        best = {}
        seen = set()
        out = []

        for i in records:
            key = tuple(i[col] for col in key_columns)
            none_count = sum(1 for v in i.values() if v is None)

            if key not in best:
                best[key] = i
            else:
                best_none_count = sum(1 for v in best[key].values() if v is None)
                if none_count < best_none_count:
                    best[key] = i

        for i in records:
            key = tuple(i[col] for col in key_columns)
            if key not in seen:
                seen.add(key)
                out.append(best[key])

    return out
    pass