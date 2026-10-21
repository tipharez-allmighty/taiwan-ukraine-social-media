"""Figures 1-3 of the paper.

The DB is attached READ_ONLY. Output: vector PDF (for submission) and PNG
(preview) in 5_results/figures/, 180 mm wide.
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import analyze_labels as al
from paper_checks import connect_read_only

FIG_DIR = Path(__file__).resolve().parents[2] / "5_results" / "figures"
MM = 1 / 25.4
WIDE = 180 * MM

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK_2, GRID = "#0b0b0b", "#52514e", "#e4e3df"

LABEL_NAMES = {
    "supportive_taiwan": "Supportive of Taiwan",
    "critical_taiwan": "Critical of Taiwan",
    "supportive_ukraine": "Supportive of Ukraine",
    "disappointment_with_us": "Disappointed with the US",
    "critical_ukraine": "Critical of Ukraine",
    "blame_nato_expansion": "Blames NATO expansion",
}
PHASES = ["defiance", "hope", "fatigue", "anxiety", "acceptance", "betrayal", "self-reliance"]

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.edgecolor": INK_2,
        "axes.labelcolor": INK,
        "axes.linewidth": 0.6,
        "xtick.color": INK_2,
        "ytick.color": INK_2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "savefig.dpi": 300,
    }
)


def save(fig, name):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(FIG_DIR / f"{name}.{ext}", bbox_inches="tight")
    plt.close(fig)
    print("wrote", FIG_DIR / f"{name}.pdf")


def wilson(k, n, z=1.96):
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def fig1_label_shares(con):
    df = con.execute(
        "SELECT is_simplified_zh, " + ", ".join(f"AVG(CAST({l} AS INT))*100 AS {l}" for l in LABEL_NAMES)
        + " FROM human_rows GROUP BY 1"
    ).fetchdf().set_index("is_simplified_zh")
    main, simp = df.loc[False], df.loc[True]
    labels = list(LABEL_NAMES)[::-1]
    y = np.arange(len(labels))
    h = 0.36

    fig, ax = plt.subplots(figsize=(WIDE, 70 * MM))
    ax.barh(y + h / 2 + 0.02, [main[l] for l in labels], h, color=BLUE, label="Main sample (Traditional Chinese, n = 16,810)")
    ax.barh(y - h / 2 - 0.02, [simp[l] for l in labels], h, color=ORANGE, label="Simplified Chinese (n = 7,782)")
    for yi, l in zip(y, labels):
        ax.text(main[l] + 0.4, yi + h / 2 + 0.02, f"{main[l]:.1f}", va="center", fontsize=7, color=INK_2)
        ax.text(simp[l] + 0.4, yi - h / 2 - 0.02, f"{simp[l]:.1f}", va="center", fontsize=7, color=INK_2)
    ax.set_yticks(y, [LABEL_NAMES[l] for l in labels])
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Share of comments with the label (%)")
    ax.xaxis.grid(True, color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower right")
    save(fig, "fig1_label_shares")


def fig2_cooccurrence(con):
    df = con.execute(
        "SELECT CAST(disappointment_with_us AS INT) d, CAST(critical_taiwan AS INT) c, "
        "CAST(supportive_taiwan AS INT) s FROM human_rows_excl_simplified_zh"
    ).fetchdf()
    targets = [("critical_taiwan", "c"), ("supportive_taiwan", "s")]
    x = np.arange(len(targets))
    w = 0.34

    fig, ax = plt.subplots(figsize=(88 * MM, 65 * MM))
    for offset, dval, color, name in [(-w / 2 - 0.02, 1, ORANGE, "Disappointed with the US"), (w / 2 + 0.02, 0, BLUE, "Not disappointed with the US")]:
        sub = df[df["d"] == dval]
        vals, lo, hi = [], [], []
        for _, col in targets:
            k, n = sub[col].sum(), len(sub)
            a, b = wilson(k, n)
            vals.append(k / n * 100)
            lo.append(k / n * 100 - a * 100)
            hi.append(b * 100 - k / n * 100)
        ax.bar(x + offset, vals, w, color=color, label=f"{name} (n = {len(sub):,})")
        ax.errorbar(x + offset, vals, yerr=[lo, hi], fmt="none", ecolor=INK, elinewidth=0.8, capsize=2)
        for xi, v in zip(x + offset, vals):
            ax.text(xi, v + max(hi) + 1, f"{v:.1f}", ha="center", fontsize=7, color=INK_2)
    ax.set_xticks(x, [LABEL_NAMES[t] for t, _ in targets])
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Share of comments (%)")
    ax.set_ylim(0, 62)
    ax.yaxis.grid(True, color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right", fontsize=7)
    save(fig, "fig2_cooccurrence")


def fig3_phases(con):
    rows = []
    for phase in PHASES:
        r = {}
        for topic, key in [("Ukraine", "ukraine"), ("Taiwan", "taiwan")]:
            v = con.execute(
                f"SELECT AVG(CAST(supportive_{key} AS INT))*100 - AVG(CAST(critical_{key} AS INT))*100 "
                f"FROM human_rows_excl_simplified_zh WHERE message_timeline = '{phase}' AND topic IN ('{topic}', 'Taiwan and Ukraine')"
            ).fetchone()[0]
            r[key] = v
        rows.append(r)
    df = pd.DataFrame(rows, index=PHASES)

    fig, ax = plt.subplots(figsize=(WIDE, 70 * MM))
    x = np.arange(len(PHASES))
    ax.axhline(0, color=INK_2, linewidth=0.6)
    for key, color, name in [("ukraine", BLUE, "Ukraine (Ukraine videos)"), ("taiwan", ORANGE, "Taiwan (Taiwan videos)")]:
        ax.plot(x, df[key], color=color, linewidth=2, marker="o", markersize=5, markeredgecolor="white", markeredgewidth=1, label=name)
        ax.text(x[-1] + 0.12, df[key].iloc[-1], f"{df[key].iloc[-1]:+.1f}", va="center", fontsize=7, color=INK_2)
    ax.set_xticks(x, [p.capitalize() for p in PHASES])
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Net sentiment\n(% supportive − % critical)")
    ax.yaxis.grid(True, color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower left")
    print(df.round(1))
    save(fig, "fig3_phases")


def main():
    con = connect_read_only(al.DB_PATH)
    al.build_views(con)
    fig1_label_shares(con)
    fig2_cooccurrence(con)
    fig3_phases(con)


if __name__ == "__main__":
    sys.exit(main())
