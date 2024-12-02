# time complexity: O(n^2)
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
