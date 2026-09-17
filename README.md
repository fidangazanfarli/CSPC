# CSPC Lab A
# Report


- **Tests:** All 3 pytest unit tests passed (`test_starts_at_N0`, `test_rejects_negative_rate`, `test_matches_law`).
- **Speed Performance:**
  - Pure Python loop time: 3.7854 seconds
  - NumPy vectorized time: 0.0004 seconds
  - Speed-up factor: NumPy is 9948.35x faster.
- **Conclusion:** Vectorized operations with NumPy process large datasets much faster than standard Python loops.