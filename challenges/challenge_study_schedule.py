def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for s, f in permanence_period:
        if (
            not all(isinstance(val, int) for val in (s, f))
            or s is None
            or f is None
        ):
            return None
        if s <= target_time <= f:
            count += 1
    return count
