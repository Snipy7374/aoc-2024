# time complexity: O(n * m)
# memory complexity: O(1)
def analyze_safe_reports(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        diff = 0
        safe_report = True

        for i in range(len(report)):
            if i == len(report) - 1:
                break

            levels_diff = report[i] - report[i + 1]

            # unsafe report
            if diff * levels_diff < 0:
                safe_report = False
                break

            if not (1 <= abs(levels_diff) <= 3):
                safe_report = False
                break

            diff = levels_diff

        if safe_report:
            safe_reports += 1

    return safe_reports


# time complexity: O(n * m)
# memory complexity: O(1)
# there's an error somewhere that is making me return
# the result - 3
def analyze_safe_reports_pt2(reports: list[list[int]]) -> int:
    safe_reports = 0

    for report in reports:
        diff = 0
        safe_report = True
        unsafe_levels = 0

        for i in range(len(report)):
            if i == len(report) - 1:
                break

            levels_diff = report[i] - report[i + 1]

            # unsafe report
            if diff * levels_diff < 0:
                safe_report = False
                unsafe_levels += 1
                continue

            if not (1 <= abs(levels_diff) <= 3):
                safe_report = False
                unsafe_levels += 1
                continue

            diff = levels_diff

        if safe_report or (unsafe_levels == 1):
            safe_reports += 1

    return safe_reports
