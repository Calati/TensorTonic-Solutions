def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    highest_accuracy = -1
    best_latency = float("inf")
    best_timestamp = ""
    name = None

    for i in models:
        acc = i["accuracy"]
        lat = i["latency"]
        ts = i["timestamp"]

        if acc > highest_accuracy:
            highest_accuracy = acc
            best_latency = lat
            best_timestamp = ts
            name = i["name"]

        elif acc == highest_accuracy:
            if lat < best_latency:
                best_latency = lat
                best_timestamp = ts
                name = i["name"]

            elif lat == best_latency:
                if ts > best_timestamp:
                    best_timestamp = ts
                    name = i["name"]

    return name
    pass