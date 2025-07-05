# Professional RF Gain Block Amplifier for Wi-Fi Networks
#### Author: Bocaletto Luca

A turnkey design for a 2.4 GHz/5 GHz gain block amplifier, ideal for boosting Wi-Fi signals. Covers system specifications, device selection, biasing, impedance matching, layout guidelines, simulation and test procedures.

---

## 1. System Specifications

- Frequency Bands  
  • 2.400–2.483 GHz (802.11b/g/n)  
  • 5.150–5.825 GHz (802.11a/n/ac)  

- Gain: 20 ± 1 dB  
- Noise Figure (NF): ≤ 1.5 dB @ 2.4 GHz; ≤ 2.0 dB @ 5 GHz  
- Input/output impedance: 50 Ω  
- Input P1 dB: ≥ +10 dBm  
- Output P1 dB: ≥ +20 dBm  
- Supply Voltage: 5 V DC @ 60 mA  
- Return Loss (S11, S22): ≤ –12 dB  
- Stability: Unconditionally stable (K > 1) over 0.1–6 GHz  
- PCB Substrate: FR-4, εr ≈ 4.4, thickness 1.6 mm  

---

## 2. Active Device Selection

| Requirement               | Specification                   | Selected Device                        |
|---------------------------|---------------------------------|----------------------------------------|
| Low NF @ 2.4 GHz          | ≤ 1.5 dB                        | Qorvo QPF4219 pHEMT (QFN-16)           |
| Gain @ 2.4 GHz            | ≥ 20 dB                         | (22 dB typ.)                           |
| P1 dB @ 2.4 GHz           | ≥ +20 dBm                       | (23 dBm typ.)                          |
| S-parameters to 6 GHz     | Available                       |                                        |
| DC Bias                   | 5 V, 50 mA (Class A)            |                                        |
| NF @ 5 GHz                | ~ 2.0 dB                        |                                        |

> QPF4219 offers high gain, low noise and adequate power for Wi-Fi boost applications.

---

## 3. DC Bias Network

- **Class A bias** at drain:  
  • V<sub>DD</sub> = 5 V  
  • I<sub>DQ</sub> ≃ 60 mA  
- **Drain resistor** R<sub>D</sub> ≈ (V<sub>DD</sub>–V<sub>DSQ</sub>)/I<sub>DQ</sub> ≃ 50 Ω  
- **Gate bias**: R<sub>G</sub> = 100 kΩ to ground  
- RF chokes (L<sub>b</sub> = 220 nH) feed DC to RF nodes  
- Bypass capacitors (C<sub>b</sub> = 100 nF) on supply and gate for low impedance at RF

---

## 4. Impedance Matching Networks

### 4.1 Input Match (50 Ω → Z<sub>in</sub>)

| Component   | Value   | Function                                                  |
|-------------|---------|-----------------------------------------------------------|
| L<sub>in</sub> (series) | 2.8 nH  | Transform 50 Ω to device Z<sub>in</sub>                   |
| C<sub>in_sh</sub> (shunt) | 1.5 pF | Fine-tune input reflection, flatten S11                   |

### 4.2 Output Match (Z<sub>out</sub> → 50 Ω)

| Component    | Value   | Function                                                 |
|--------------|---------|----------------------------------------------------------|
| L<sub>out</sub> (series) | 3.2 nH  | Transform device Z<sub>out</sub> to 50 Ω                |
| C<sub>out_sh</sub> (shunt)| 1.2 pF | Fine-tune output reflection, flatten S22                  |

### 4.3 Harmonic Suppression

- **2nd-order trap**: L<sub>h2</sub>= 8.2 nH ∥ C<sub>h2</sub>= 0.5 pF tuned to 4.8 GHz  
- **3rd-order trap**: L<sub>h3</sub>= 5.6 nH ∥ C<sub>h3</sub>= 0.3 pF tuned to 7.2 GHz  

> Traps reduce distortion, improving linearity.

---

## 5. Bill of Materials

| Ref.      | Description                    | Value   | Package | Qty |
|-----------|--------------------------------|---------|---------|-----|
| Q1        | Qorvo QPF4219 pHEMT            | –       | QFN-16  | 1   |
| C1–C2     | RF Coupling Caps               | 2 pF    | 0402    | 2   |
| C<sub>in_sh</sub>  | Input match shunt          | 1.5 pF  | 0402    | 1   |
| C<sub>out_sh</sub>  | Output match shunt         | 1.2 pF  | 0402    | 1   |
| L<sub>in</sub>      | Input match series         | 2.8 nH  | 0402    | 1   |
| L<sub>out</sub>     | Output match series        | 3.2 nH  | 0402    | 1   |
| L<sub>b</sub>       | RF choke for V<sub>DD</sub>     | 220 nH  | 0603    | 1   |
| R<sub>G</sub>       | Gate bias                   | 100 kΩ  | 0603    | 1   |
| R<sub>D</sub>       | Drain bias                  | 50 Ω    | 0603    | 1   |
| C<sub>b</sub>       | DC bypass                   | 100 nF  | 0805    | 2   |
| Filters   | Dual-band bandpass (PCB)       | custom  | PCB     | 2   |

---

## 6. Simulation & Optimization

**Workflow**:
1. Import QPF4219 S-parameters into ADS.  
2. Build schematic with bias and matching networks.  
3. Run S-parameter sweep (2–6 GHz):  
   - S11, S22 ≤ –12 dB  
   - S21 = 20 ± 1 dB flat over both Wi-Fi bands  
4. Check stability (Rollett’s K > 1 across 0.1–6 GHz).  
5. Simulate Noise Figure: NF ≤ 1.5 dB @ 2.4 GHz, ≤ 2.0 dB @ 5 GHz.  
6. Verify P1 dB and OIP3 (target P1 dB ≥ +20 dBm, OIP3 ≥ +30 dBm).  
7. Use ADS optimization to refine L/C for bandwidth and flatness.  

> A well-structured flow reduces layout iterations and accelerates time-to-result.

---

## 7. PCB Layout Guidelines

- **Substrate**: FR-4, 1.6 mm, εr = 4.4  
- **50 Ω Microstrip**: Width ≃ 3 mm on top layer  
- **Ground**: Solid plane on inner layer; via stitching every 3 mm  
- **Component Placement**:  
  - RF choke and bypass caps within 0.5 mm of Q1 pins  
  - Matching L/C symmetrically around transistor  
- **RF Paths**: Keep series inductors and coupling caps close to device  
- **Via Pairs**: On shunt caps for minimal inductance  
- **RF/DC Isolation**: Wide copper pour around bias nets  

---

## 8. Measurement & Verification

- **Network Analyzer**: S-parameters, gain, return loss  
- **Spectrum Analyzer + Signal Generator**: Output power, P1 dB, harmonic levels  
- **Noise Figure Analyzer**: NF @ both bands  
- **Linearity Test**: Two-tone OIP3 and EVM under 802.11ac waveforms  
- **Temperature Drift**: Performance over –20 °C to +70 °C  

---

## 9. References

1. RF Amplifier Basics and Power Amplifier Design Guide, RF Wireless World  
2. Practical RF Amplifier Design Using the Available Gain Procedure, Keysight White Paper  
3. ANP101: RF Gain Block Amplifier with Integrated Ferrite, Würth Elektronik  
4. RF Amplifier – 5 Steps to Design an RF Amplifier, Flex PCB Guide  

---

## 10. File rf_gain.py

The script is written in Python and uses the SKiDL library to programmatically describe the RF amplifier’s electrical schematic. It begins by creating “Net” objects that represent key connection points—RF input, RF output, the transistor’s gate and drain, the supply rail, and ground. Next, individual components are instantiated, from the band-pass filters to the coupling capacitors, inductors, bias resistors, and the QPF4219 active device, each defined with its value and corresponding KiCad footprint.

Each component is then linked to the nets defined at the start using SKiDL’s aggregation operator, recreating the signal and bias paths specified in the RF design. Because connections are declared rather than manually wired, wiring errors are virtually impossible. After all connections are established, the script runs an Electrical Rules Check (ERC) to verify the design’s integrity and finally generates a KiCad-compatible netlist file.

The resulting netlist includes all the information required for automatic import into PCBNew—symbol-pin mappings, component values, footprints, and net assignments. This ensures you can immediately proceed to PCB layout with complete confidence that the schematic accurately reflects the intended design.

---

## ASCII SCHEME

                                               +-- C_shunt_out (1.2 pF) ── GND
                                               |
     RF_IN ── [BPF_IN] ── C1 (2 pF) ── L_in (2.8 nH) ──+── Gate (Q1) ── Rg (100 kΩ) ── GND
                                                       |
                                                       +── C_shunt_in (1.5 pF) ── GND

            5 V ── Lb (220 nH) ── Rd (50 Ω) ──+── Drain (Q1) ── L_out (3.2 nH) ── C2 (2 pF) ── [BPF_OUT] ── RF_OUT
                                              |                                |
                                              +── C_bypass (100 nF) ── GND     +── C_shunt_out (1.2 pF) ── GND

                                        Source (Q1) ── GND

---

[![Read Online](https://img.shields.io/badge/Read%20Online-blue)](https://bocaletto-luca.github.io/RF-Amplifier-HF/index.html)  

[![Read Online](https://img.shields.io/badge/Read%20Online-blue)](https://bocaletto-luca.github.io/RF-Amplifier-WiFi/index.html)

---

Good gain wifi, @bocaletto-luca
