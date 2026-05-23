# Sample Queries

These examples show the type of questions an Industrial RAG Knowledge Assistant can answer using retrieved document chunks and citation-based output.

## Example 1: Alarm Troubleshooting

### User Query

`What should an operator check first when compressor alarm E-214 appears?`

### Example Retrieved Sources

- `compressor-maintenance-manual-v3.pdf`, Section 4.2, Page 18
- `field-service-troubleshooting-guide.pdf`, Section 2.1, Page 7

### Example Answer

Alarm `E-214` is associated with low lubrication pressure. The first check is to verify oil level and confirm that the lubrication pump is active before restarting the compressor. If pressure does not recover, inspect the inlet filter and pressure sensor wiring.

### Example Citations

- `[1] compressor-maintenance-manual-v3.pdf, Section 4.2, Page 18`
- `[2] field-service-troubleshooting-guide.pdf, Section 2.1, Page 7`

## Example 2: Preventive Maintenance Interval

### User Query

`How often should the hydraulic return filter be replaced for the HX-220 press?`

### Example Retrieved Sources

- `hx-220-service-schedule.pdf`, Preventive Maintenance Table, Page 11

### Example Answer

The hydraulic return filter for the `HX-220` press should be replaced every `1,000 operating hours` or earlier if contamination indicators show restricted flow.

### Example Citation

- `[1] hx-220-service-schedule.pdf, Preventive Maintenance Table, Page 11`

## Example 3: Safety Procedure

### User Query

`Before servicing the conveyor drive, what lockout steps are required?`

### Example Retrieved Sources

- `conveyor-safety-sop.pdf`, Lockout/Tagout Procedure, Page 3
- `plant-electrical-isolation-standard.pdf`, Section 5.1, Page 9

### Example Answer

Before servicing the conveyor drive, isolate electrical power at the main disconnect, apply a personal lock and tag, verify zero-energy state at the motor controller, and confirm that stored mechanical motion has been released before work begins.

### Example Citations

- `[1] conveyor-safety-sop.pdf, Lockout/Tagout Procedure, Page 3`
- `[2] plant-electrical-isolation-standard.pdf, Section 5.1, Page 9`

## Example 4: Unsupported Answer Handling

### User Query

`What is the exact torque value for the revised 2026 spindle assembly?`

### Example Answer

I could not find a supported torque value for the revised 2026 spindle assembly in the retrieved sources. A current revision-controlled service document should be checked before maintenance is performed.

### Expected Behavior

- No fabricated torque value
- Clear statement of missing evidence
- Recommendation to verify against current approved documentation
