"""Exact rational checks of displayed constants, not an algorithm or proof test."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
alpha2 = F(82, 81)
checks = {
    'shared_search_N_factor': 32 * 4**4 == 8192,
    'shared_search_log_factor': 4 * 64 * 16 == 4096,
    'search_hoeffding_scale': F(1, 4)**2 / 2 == F(1, 32),
    'depth_union_factor': 2 * F(1, 2) == 1,
    'gram_refit_factor': 1 + (F(1, 10) / (1 - F(1, 10))) ** 2 == alpha2,
    'norm_cap': alpha2 < 2,
    'group_variance': F(9, 4) / 144 == F(1, 64),
    'group_sign_error': F(1, 64) / F(1, 2) ** 2 == F(1, 16),
    'majority_bias_budget': 576 * alpha2 / 262144 <= F(1, 128),
    'majority_floor_budget': F(4, 512) == F(1, 128),
    'markov_budget': (F(1, 128) + F(1, 128)) / F(1, 64) == 1,
    'search_missing_energy': F(16, 9) / 64 == F(1, 36),
    'certificate_mass': 16 * F(1, 32) ** 2 == F(1, 64),
    'strict_contraction': F(1, 36) + alpha2 / 64 < F(1, 16),
    'coarse_contraction_check': F(1, 36) + F(2, 64) < F(1, 16),
    'proposal_epsilon': F(1, 2048)**2 == F(1, 16*262144),
    'proposal_four_stage_success': 1-4*F(1,16) == F(3,4),
    'conditional_progress_floor': F(3,4)-2*F(1,1600) >= F(1,2),
    'safety_union_budget': 2*8*F(1,1600) == F(1,100),
    'adaptive_tail_base': 2*F(3,4)**8 == F(6561,32768),
    'adaptive_tail_bound': F(6561,32768) < F(1,4),
    'success_margin': 1-F(1,100)-F(1,4) == F(37,50) > F(2,3),
}
if not all(checks.values()):
    raise SystemExit(json.dumps(checks, indent=2))
receipt = {
    'scope': 'Exact rational arithmetic checks only; no learner run or mathematical certification',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256': hashlib.sha256((root / 'manuscript/main.tex').read_bytes()).hexdigest(),
    'checks': checks, 'result': 'PASS',
}
(root / 'verification').mkdir(exist_ok=True)
(root / 'verification/constants.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'constants': 'PASS', 'checks': len(checks)}))
