def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here

    # Normalize
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)

    ref_prob = [r/ref_total for r in reference_counts]
    prod_prob = [p/prod_total for p in production_counts]

    # TVD
    tvd = 0.5*sum(abs(p - q) for p,q in zip(ref_prob, prod_prob))

    # Drift?
    drift = tvd > threshold
    
    return {"score": tvd, "drift_detected": drift}
    pass