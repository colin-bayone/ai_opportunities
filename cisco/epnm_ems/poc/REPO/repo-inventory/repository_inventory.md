# Repository Inventory

## Summary

- Programming root: `/Users/cmoore/Documents/programming`
- EPNM parent: `/Users/cmoore/Documents/programming/EPNM`
- EMS-CNC parent: `/Users/cmoore/Documents/programming/EMS-CNC`
- Total Git repositories currently present: `14`
- Newly cloned in this pass: `10`
- Pre-existing before this pass: `4`

## Organization Model

### EPNM

- `core-framework/`
- `inventory/`
- `chassis/`
- `fault/`

### EMS-CNC

- `frontend/`
- `backend/inventory/`
- `backend/fault-assurance/`

## Current Inventory

| Family | Area | Repo | Status | Current Path | Desired/Target Path | Origin |
| --- | --- | --- | --- | --- | --- | --- |
| EPNM | Core Framework | `pf-framework` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/core-framework/pf-framework` | same | `https://github3.cisco.com/EPNM/pf-framework` |
| EPNM | Core Framework | `wireless` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/core-framework/wireless` | same | `https://github3.cisco.com/EPNM/wireless` |
| EPNM | Inventory | `assembly` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/inventory/assembly` | same | `https://github3.cisco.com/EPNM/assembly` |
| EPNM | Inventory | `inventory` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/inventory/inventory` | same | `https://github3.cisco.com/EPNM/inventory` |
| EPNM | Inventory | `ce-content-device-packs` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/inventory/ce-content-device-packs` | same | `https://github3.cisco.com/EPNM/ce-content-device-packs` |
| EPNM | Chassis | `chassisview` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/chassis/chassisview` | same | `https://github3.cisco.com/EPNM/chassisview` |
| EPNM | Fault | `fault` | newly cloned | `/Users/cmoore/Documents/programming/EPNM/fault/fault` | same | `https://github3.cisco.com/EPNM/fault` |
| EMS-CNC | Frontend | `infra-ui` | newly cloned | `/Users/cmoore/Documents/programming/EMS-CNC/frontend/infra-ui` | same | `https://github3.cisco.com/ROBOT/infra-ui` |
| EMS-CNC | Frontend | `common-ui` | pre-existing | `/Users/cmoore/Documents/programming/common-ui` | `/Users/cmoore/Documents/programming/EMS-CNC/frontend/common-ui` | `https://github3.cisco.com/ROBOT/common-ui.git` |
| EMS-CNC | Frontend | `unified-ems-ui` | pre-existing | `/Users/cmoore/Documents/programming/unified-ems-ui` | `/Users/cmoore/Documents/programming/EMS-CNC/frontend/unified-ems-ui` | `https://github3.cisco.com/ROBOT/unified-ems-ui.git` |
| EMS-CNC | Backend Inventory | `cw-inventory` | pre-existing, intentionally left in place | `/Users/cmoore/Documents/programming/cw-inventory` | `/Users/cmoore/Documents/programming/EMS-CNC/backend/inventory/cw-inventory` | `https://github3.cisco.com/ROBOT/cw-inventory.git` |
| EMS-CNC | Backend Inventory | `cw-inventory-collector` | pre-existing | `/Users/cmoore/Documents/programming/cw-inventory-collector` | `/Users/cmoore/Documents/programming/EMS-CNC/backend/inventory/cw-inventory-collector` | `https://github3.cisco.com/ROBOT/cw-inventory-collector.git` |
| EMS-CNC | Backend Fault/Assurance | `ems-assurance` | newly cloned | `/Users/cmoore/Documents/programming/EMS-CNC/backend/fault-assurance/ems-assurance` | same | `https://github3.cisco.com/ROBOT/ems-assurance` |
| EMS-CNC | Backend Fault/Assurance | `cw-epnm-fault` | newly cloned | `/Users/cmoore/Documents/programming/EMS-CNC/backend/fault-assurance/cw-epnm-fault` | same | `https://github3.cisco.com/ROBOT/cw-epnm-fault` |

## Notes

- `cw-inventory` was left in its current location on purpose because it is the active workspace for this session.
- `common-ui`, `unified-ems-ui`, and `cw-inventory-collector` still live at the top level of `programming/`; the target paths above show the intended steady-state organization.
- The overview file referenced two important branch contexts that are not enforced by the clone layout:
  - `EPNM/fault`: `cepnm8.1PI` and `develop`
  - `ROBOT/ems-assurance`: `cepnm8.1PI` and `develop`
- The same repository may therefore support both legacy EPNM and EMS-CNC work depending on the branch you check out.

## Suggested Next Moves

- Move `common-ui` to `/Users/cmoore/Documents/programming/EMS-CNC/frontend/common-ui` in a separate session.
- Move `unified-ems-ui` to `/Users/cmoore/Documents/programming/EMS-CNC/frontend/unified-ems-ui` in a separate session.
- Move `cw-inventory-collector` to `/Users/cmoore/Documents/programming/EMS-CNC/backend/inventory/cw-inventory-collector` in a separate session.
- Decide whether `cw-inventory` should eventually move to `/Users/cmoore/Documents/programming/EMS-CNC/backend/inventory/cw-inventory` after the current workspace is no longer active.
