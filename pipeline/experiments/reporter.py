"""
Experiment 001 Metrics Reporter & Analysis Engine.

Calculates:
- Valid Scene Rate (VSR = valid committed scenes / total scenes)
- Cost-Adjusted Validity (CAV = valid scenes / total tokens * 1000)
- Violation distributions (spatial, possession, epistemic, contract)
- Token economics & latency
- Search dynamics (rejection rate, repair rate, state efficiency E(c))
- Generates formatted Markdown comparison tables for publication
"""

from typing import Dict, Any, List, Optional
from pathlib import Path
import json


class ExperimentReporter:
    """Aggregates multi-system experimental logs into research metrics and reports."""

    @staticmethod
    def analyze_system_results(system_id: str, system_name: str, scene_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculates comprehensive reliability, quality, and economic metrics for a system arm."""
        total_scenes = len(scene_records)
        if total_scenes == 0:
            return {"system_id": system_id, "system_name": system_name, "total_scenes": 0}

        valid_scenes = sum(1 for s in scene_records if s.get("is_valid", False))
        vsr = (valid_scenes / total_scenes) * 100.0

        # Violation breakdowns
        total_violations = 0
        fatal_violations = 0
        error_violations = 0
        warning_violations = 0
        violation_type_counts: Dict[str, int] = {}

        for s in scene_records:
            viols = s.get("violations", [])
            total_violations += len(viols)
            for v in viols:
                sev = v.get("severity", "").upper()
                vtype = v.get("violation_type") or v.get("type", "UNKNOWN")
                if sev == "FATAL":
                    fatal_violations += 1
                elif sev == "ERROR":
                    error_violations += 1
                elif sev == "WARNING":
                    warning_violations += 1
                violation_type_counts[vtype] = violation_type_counts.get(vtype, 0) + 1

        # Token Economics
        total_prompt_tokens = sum(s.get("token_economics", {}).get("prompt_tokens", 0) for s in scene_records)
        total_completion_tokens = sum(s.get("token_economics", {}).get("completion_tokens", 0) for s in scene_records)
        total_tokens = sum(s.get("token_economics", {}).get("total_tokens", 0) for s in scene_records)
        total_latency_ms = sum(s.get("token_economics", {}).get("generation_time_ms", 0) for s in scene_records)
        total_repair_tokens = sum(s.get("token_economics", {}).get("repair_tokens", 0) for s in scene_records)

        # Cost-Adjusted Validity (CAV)
        # CAV = (valid_scenes / total_tokens) * 1000
        cav = (valid_scenes / total_tokens * 1000.0) if total_tokens > 0 else 0.0

        # Quality Metrics
        quality_scores = [s.get("quality_score", 0.0) for s in scene_records if s.get("quality_score") is not None]
        avg_quality = (sum(quality_scores) / len(quality_scores)) if quality_scores else 0.0

        efficiency_scores = [s.get("efficiency_score", 0.0) for s in scene_records if s.get("efficiency_score") is not None]
        avg_efficiency = (sum(efficiency_scores) / len(efficiency_scores)) if efficiency_scores else 0.0

        # Search Dynamics (BoN specific)
        candidates_generated = sum(s.get("gate_summary", {}).get("total_candidates", 1) for s in scene_records)
        candidates_rejected = sum(
            s.get("gate_summary", {}).get("fatal_rejected", 0) +
            s.get("gate_summary", {}).get("gate_1_failed", 0) +
            s.get("gate_summary", {}).get("gate_2_failed", 0)
            for s in scene_records
        )
        rejection_rate = (candidates_rejected / candidates_generated * 100.0) if candidates_generated > 0 else 0.0

        repair_attempts = sum(1 for s in scene_records if s.get("repair", {}).get("attempted", False))
        repair_successes = sum(
            1 for s in scene_records
            if s.get("repair", {}).get("attempted", False) and s.get("is_valid", False)
        )
        repair_rate = (repair_attempts / total_scenes * 100.0) if total_scenes > 0 else 0.0
        repair_success_rate = (repair_successes / repair_attempts * 100.0) if repair_attempts > 0 else 0.0

        return {
            "system_id": system_id,
            "system_name": system_name,
            "total_scenes": total_scenes,
            "valid_scenes": valid_scenes,
            "vsr_percent": round(vsr, 2),
            "cav_score": round(cav, 4),
            "violations": {
                "total": total_violations,
                "per_scene": round(total_violations / total_scenes, 2) if total_scenes else 0.0,
                "fatal": fatal_violations,
                "error": error_violations,
                "warning": warning_violations,
                "by_type": violation_type_counts,
            },
            "token_economics": {
                "total_prompt_tokens": total_prompt_tokens,
                "total_completion_tokens": total_completion_tokens,
                "total_tokens": total_tokens,
                "avg_tokens_per_scene": round(total_tokens / total_scenes, 1) if total_scenes else 0,
                "total_latency_ms": total_latency_ms,
                "avg_latency_ms_per_scene": round(total_latency_ms / total_scenes, 1) if total_scenes else 0,
                "total_repair_tokens": total_repair_tokens,
            },
            "quality": {
                "avg_quality_score": round(avg_quality, 4),
                "avg_efficiency_score": round(avg_efficiency, 4),
            },
            "search_dynamics": {
                "candidates_generated": candidates_generated,
                "candidates_rejected": candidates_rejected,
                "rejection_rate_percent": round(rejection_rate, 2),
                "repair_attempts": repair_attempts,
                "repair_successes": repair_successes,
                "repair_rate_percent": round(repair_rate, 2),
                "repair_success_rate_percent": round(repair_success_rate, 2),
            },
        }

    @classmethod
    def generate_full_report(
        cls,
        experiment_id: str,
        title: str,
        config: Dict[str, Any],
        system_summaries: List[Dict[str, Any]],
        output_file: Optional[Path] = None,
    ) -> str:
        """Generates publication-grade Markdown comparative analysis report with tables."""
        lines = [
            f"# Experiment 001: {title}\n\n",
            "> [!NOTE]\n",
            "> **Research Invariant:** Small Language Model (1.5B) narrative reliability governed by deterministic external compiler vs unconstrained generation.\n\n",
            "## 1. Executive Summary Table\n\n",
            "| System | Model | Search | Compiler | Valid Scene Rate (VSR) | Violations / Scene | Fatal Violations | Avg Quality | Tokens / Scene | CAV (Valid/1k Tok) |\n",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n",
        ]

        for s in system_summaries:
            s_name = s["system_name"]
            vsr = f"{s['vsr_percent']}%"
            viols_per_sc = f"{s['violations']['per_scene']}"
            fatal = f"{s['violations']['fatal']}"
            q = f"{s['quality']['avg_quality_score']}"
            toks = f"{s['token_economics']['avg_tokens_per_scene']}"
            cav = f"{s['cav_score']}"
            is_bon = "BoN" in s_name
            is_comp = "Yes" if "Stateful" in s_name or is_bon else "No"
            search_str = "Best-of-3" if is_bon else "1 (Greedy)"

            lines.append(
                f"| **{s_name}** | 1.5B | {search_str} | {is_comp} | **{vsr}** | {viols_per_sc} | {fatal} | {q} | {toks} | **{cav}** |\n"
            )

        lines.append("\n---\n\n## 2. Violation Category Breakdown\n\n")
        lines.append("| System | Epistemic Leaks | Spatial Teleportation | Possession Conflicts | Contract Breaches | Total Violations |\n")
        lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |\n")

        for s in system_summaries:
            b = s["violations"]["by_type"]
            epi = b.get("EPISTEMIC_LEAK", 0)
            loc = b.get("LOCATION_TELEPORTATION", 0)
            pos = b.get("POSSESSION_CONFLICT", 0)
            cb = b.get("CONTRACT_BREACH", 0)
            tot = s["violations"]["total"]
            lines.append(f"| **{s['system_name']}** | {epi} | {loc} | {pos} | {cb} | **{tot}** |\n")

        lines.append("\n---\n\n## 3. Token Economics & Cost-Adjusted Reliability (CAV)\n\n")
        lines.append("| System | Prompt Tokens | Completion Tokens | Total Tokens | Avg Latency (ms) | CAV (Valid Scenes / 1k Tokens) |\n")
        lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |\n")

        for s in system_summaries:
            te = s["token_economics"]
            lines.append(
                f"| **{s['system_name']}** | {te['total_prompt_tokens']} | {te['total_completion_tokens']} | {te['total_tokens']} | {te['avg_latency_ms_per_scene']}ms | **{s['cav_score']}** |\n"
            )

        # Search dynamics for BoN
        bon_sys = next((s for s in system_summaries if "BoN" in s["system_name"]), None)
        if bon_sys and bon_sys["search_dynamics"]["candidates_generated"] > 0:
            sd = bon_sys["search_dynamics"]
            lines.append("\n---\n\n## 4. BoN Search Dynamics & Repair Efficacy\n\n")
            lines.append(f"- **Total Candidates Evaluated:** {sd['candidates_generated']}\n")
            lines.append(f"- **Gate 1 & Gate 2 Rejection Rate:** {sd['rejection_rate_percent']}%\n")
            lines.append(f"- **Targeted Repair Attempts (Zero Survivors):** {sd['repair_attempts']}\n")
            lines.append(f"- **Targeted Repair Success Rate:** {sd['repair_success_rate_percent']}%\n")
            lines.append(f"- **Average State Efficiency E(c):** {bon_sys['quality']['avg_efficiency_score']}\n\n")

        report_md = "".join(lines)
        if output_file:
            Path(output_file).write_text(report_md, encoding="utf-8")
        return report_md
