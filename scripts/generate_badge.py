import sys

def color_for_coverage(coverage):
    if coverage >= 90:
        return "green"
    elif coverage >= 75:
        return "green"
    elif coverage >= 60:
        return "yellow"
    elif coverage >= 40:
        return "orange"
    else:
        return "red"

def generate_badge(coverage):
    color = color_for_coverage(coverage)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="130" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="130" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <rect width="70" height="20" fill="#555"/>
    <rect x="70" width="60" height="20" fill="{color}"/>
    <rect width="130" height="20" fill="url(#b)"/>
  </g>
  <g fill="#fff" text-anchor="middle"
     font-family="DejaVu Sans,Verdana,Geneva,sans-serif"
     font-size="11">
    <text x="35" y="15" fill="#010101" fill-opacity=".3">coverage</text>
    <text x="35" y="14">coverage</text>
    <text x="99" y="15" fill="#010101" fill-opacity=".3">{coverage:.0f}%</text>
    <text x="99" y="14">{coverage:.0f}%</text>
  </g>
</svg>"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_badge.py <coverage_percent> <output_file>")
        sys.exit(1)

    coverage_percent = float(sys.argv[1])
    output_file = sys.argv[2]

    badge = generate_badge(coverage_percent)
    with open(output_file, "w") as f:
        f.write(badge)
