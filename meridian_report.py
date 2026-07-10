def generate_report(scenarios):
    report = "# Test Execution Report\n"
    for scenario in scenarios:
        report += f"## {scenario.name}\n"
        report += f"- Status: {scenario.status}\n"
    with open('report.md', 'w') as f:
        f.write(report)