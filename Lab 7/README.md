# L6_L7_46 — Photo Print Order

## Lab 7: Fuzz Testing with Hypothesis

### About
A small Python module that parses print orders, averages file sizes, and works out the payable amount after a discount.

### Lab 7 Deliverables
| File | Description |
|------|-------------|
| `photo_print_order.py` | The application script fixed and hardened against invalid inputs |
| `test_photo_print_order.py` | Hypothesis fuzz tests that uncover crashes in the buggy code |
| `Lab7_Fuzzing_Report.pdf` | Screenshots showing the initial run, failing fuzz tests, fixed application, and passing tests |

### Results
Successfully used property-based fuzzing to identify edge-case crashes (such as `NoneType` and `ValueError`) and patched the functions to handle bad inputs gracefully without crashing.
